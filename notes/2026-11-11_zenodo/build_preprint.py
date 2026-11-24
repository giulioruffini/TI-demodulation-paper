#!/usr/bin/env python3
"""Combine the article and supplement, resolving links between their pages.

Stage the current article and supplement under build/zenodo_2026-11-11.
Requires pypdf and PyMuPDF for PDF assembly and checks.
The separate reading PDFs remain unchanged.
"""
import hashlib
import json
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, NameObject

BUILD = Path(__file__).resolve().parents[2] / "build/zenodo_2026-11-11"


def main():
    paths = [BUILD / f"TN0484_jne{suffix}.pdf"
             for suffix in ("", "_supplement")]
    readers = [PdfReader(path) for path in paths]
    offsets = [0, len(readers[0].pages)]
    writer = PdfWriter()
    def copy_outline(items, reader, offset, parent):
        previous = parent
        for item in items:
            if isinstance(item, list):
                copy_outline(item, reader, offset, previous)
            else:
                page_index = offset + reader.get_destination_page_number(item)
                previous = writer.add_outline_item(item.title, page_index, parent=parent)

    for reader, offset, title in zip(readers, offsets, ("Article", "Supplementary material")):
        for page in reader.pages:
            writer.add_page(page)
        parent = writer.add_outline_item(title, offset)
        copy_outline(reader.outline, reader, offset, parent)

    def destination(reader_index, name):
        reader = readers[reader_index]
        target = reader.named_destinations[str(name)]
        page_index = offsets[reader_index] + reader.get_destination_page_number(target)
        return ArrayObject([writer.pages[page_index].indirect_reference,
                            *target.dest_array[1:]])

    converted = 0
    for source_index, reader in enumerate(readers):
        for page_index, source_page in enumerate(reader.pages):
            page = writer.pages[offsets[source_index] + page_index]
            original = source_page.get("/Annots", [])
            copied = page.get("/Annots", [])
            assert len(original) == len(copied)
            for original_ref, copied_ref in zip(original, copied):
                annotation = original_ref.get_object()
                target_annotation = copied_ref.get_object()
                action = annotation.get("/A")
                if action:
                    target_action = target_annotation["/A"]
                    if action.get("/S") == "/GoToR":
                        filename = Path(str(action["/F"])).name
                        target_index = [p.name for p in paths].index(filename)
                        target_action[NameObject("/S")] = NameObject("/GoTo")
                        target_action[NameObject("/D")] = destination(target_index, action["/D"])
                        target_action.pop("/F", None)
                        target_action.pop("/NewWindow", None)
                        converted += 1
                    elif action.get("/S") == "/GoTo" and isinstance(action.get("/D"), str):
                        target_action[NameObject("/D")] = destination(source_index, action["/D"])
                elif isinstance(annotation.get("/Dest"), str):
                    target_annotation[NameObject("/Dest")] = destination(source_index, annotation["/Dest"])

    writer.add_metadata({
        "/Title": "The cortical column as a tuned receiver: a network mechanism for temporal-interference stimulation",
        "/Author": "Giulio Ruffini; Ricardo Salvador; Borja Mercadal; Raul de Palma Aristides; Francesca Castaldo; Nir Grossman; Santiago Canals; Claudio Mirasso",
        "/Subject": "Preprint with supplementary material; CC BY 4.0; not peer reviewed",
    })
    output = BUILD / "TN0484_v0.15.0-draft29_preprint.pdf"
    with output.open("wb") as handle:
        writer.write(handle)

    merged = PdfReader(output)
    page_ids = {page.indirect_reference.idnum for page in merged.pages}
    local_links = 0
    for page in merged.pages:
        for ref in page.get("/Annots", []):
            annotation = ref.get_object()
            action = annotation.get("/A", {})
            assert action.get("/S") != "/GoToR", "Unresolved inter-document link"
            target = action.get("/D") if action.get("/S") == "/GoTo" else annotation.get("/Dest")
            if target is not None:
                assert isinstance(target, ArrayObject), "Unresolved named link"
                assert target[0].idnum in page_ids, "Link points outside the combined PDF"
                local_links += 1

    # Rewriting links must not change any page's visible content.
    combined = fitz.open(output)
    checked = 0
    for source_index, path in enumerate(paths):
        source = fitz.open(path)
        for index, page in enumerate(source):
            a = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
            b = combined[offsets[source_index] + index].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
            assert (a.width, a.height, a.samples) == (b.width, b.height, b.samples)
            checked += 1
        source.close()
    combined.close()
    report = {"output": str(output), "pages": len(merged.pages),
              "cross_document_links_resolved": converted, "local_links_verified": local_links,
              "pages_with_identical_rendering": checked,
              "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
