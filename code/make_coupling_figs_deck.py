import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
C="/Users/giulio/Claude/NE TNs and Blogs/TN0484/code/"
NEBLUE,NERED,NEGRAY,NEGREEN="#1f4e79","#c0392b","#7f8c8d","#1a9850"
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
# ---- figure 1: response vs coupling, JR (pinned detector) and NMM2 PING
j=np.load(C+"jcurve_main.npz"); n=np.load(C+"nmm2_jcurve.npz")
fig,ax=plt.subplots(1,2,figsize=(10.5,4.0))
a=ax[0]; a.semilogy(j['C'],j['Acl'],"o-",color=NEBLUE,ms=4,lw=1.8,label="beat response $A_\\Omega$ (closed loop)")
a.semilogy(j['C'],j['Aop'],"--",color=NEGRAY,lw=1.4,label="open-loop detector (pinned)")
a.axvline(float(j['Chopf']),color=NERED,lw=1.0,ls=":"); a.text(float(j['Chopf'])-1.0,a.get_ylim()[0]*1.6 if False else float(np.min(j['Aop']))*1.3,"Hopf $C^*$",color=NERED,rotation=90,ha="right",va="bottom",fontsize=10)
a.set_xlabel("connectivity $C$ (Jansen–Rit coupling)"); a.set_ylabel("response at the beat (mV)")
a.set_title("(a) Jansen–Rit: detector pinned, connectivity swept",fontsize=11,loc="left"); a.legend(frameon=False,fontsize=9,loc="upper left")
g=j['Acl'][-1]/j['Acl'][0]; a.text(0.98,0.06,f"×{g:.0f} from far to near criticality",transform=a.transAxes,ha="right",fontsize=9,color=NEBLUE)
b=ax[1]; b.semilogy(n['C'],n['Acl'],"s-",color=NEGREEN,ms=4,lw=1.8,label="beat response of $r_E$")
b.axvline(float(n['C'][-1])+0.5*(n['C'][-1]-n['C'][-2]),color=NERED,lw=1.0,ls=":"); b.text(float(n['C'][-1])+0.5*(n['C'][-1]-n['C'][-2])-0.1,float(np.min(n['Acl']))*1.3,"Hopf $J^*$",color=NERED,rotation=90,ha="right",va="bottom",fontsize=10)
b.set_xlabel("synaptic weight $J$ (exact mean field, PING)"); b.set_ylabel("response at the beat (a.u.)")
b.set_title("(b) exact mean field: no pinning needed",fontsize=11,loc="left"); b.legend(frameon=False,fontsize=9,loc="upper left")
fig.tight_layout(); fig.savefig("response_vs_coupling.png",dpi=160); fig.savefig("response_vs_coupling.pdf")
print("jcurve C range",j['C'].min(),j['C'].max(),"Chopf",float(j['Chopf']),"growth",g,"| nmm2 C",n['C'].min(),n['C'].max(),"gamma",n['gamma'].min(),n['gamma'].max())
# ---- figure 2: timing vs coupling
t=np.load(C+"timing_not_rate.npz")
fig,ax=plt.subplots(1,2,figsize=(10.5,4.0))
a=ax[0]; a.semilogy(t['Cs'],1e3*t['AC'],"o-",color=NEBLUE,ms=4,lw=1.8,label="beat-locked rate modulation")
a.semilogy(t['Cs'],1e3*np.abs(t['DC']),"s-",color=NERED,ms=4,lw=1.8,label="|mean-rate shift|")
a.set_xlabel("connectivity $C$ → Hopf"); a.set_ylabel("pyramidal rate (mHz)"); a.legend(frameon=False,fontsize=9,loc="upper left")
a.set_title("(a) modulation and mean shift vs connectivity",fontsize=11,loc="left")
b=ax[1]; b.plot(t['Cs'],t['AC']/np.abs(t['DC']),"o-",color=NEBLUE,ms=4,lw=1.8)
b.set_xlabel("connectivity $C$ → Hopf"); b.set_ylabel("modulation / |mean shift|"); b.set_title("(b) the ratio grows toward criticality",fontsize=11,loc="left")
b.set_ylim(0,None)
fig.tight_layout(); fig.savefig("timing_vs_coupling.png",dpi=160); fig.savefig("timing_vs_coupling.pdf")
print("timing C range",t['Cs'].min(),t['Cs'].max(),"ratio",(t['AC']/np.abs(t['DC'])).min(),(t['AC']/np.abs(t['DC'])).max())
