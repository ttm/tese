import numpy as n, pylab as p

R=1.
Ts=[0.05,0.07,.1,1,5,7,10]

RT=[R/T for T in Ts]
p.subplot(211)
p.plot(Ts,RT,"ro")
p.plot(Ts,RT,"b")
p.xlabel(r"T $\rightarrow$",size=15)
p.ylabel(r"$\frac{R}{T}\;\;\rightarrow$",size=18)
p.xlim(min(Ts)-1,max(Ts)+1)
p.ylim(min(RT)-1,max(RT)+1)
p.subplot(212)
p.xlabel(r"log(T) $\rightarrow$",size=15)
p.ylabel(r"$log(\frac{R}{T})\;\;\rightarrow$",size=18)
p.plot(n.log(Ts),n.log(RT),"ro")
p.plot(n.log(Ts),n.log(RT),"b")
p.xlim(min(n.log(Ts))-.6,max(n.log(Ts))+.6)
p.ylim(min(n.log(RT))-1,max(n.log(RT))+1)
p.suptitle(u"Relação básica da lei de potência",size=25)
p.subplots_adjust(left=0.10,bottom=0.11,right=0.97,top=0.86,wspace=0.20,hspace=0.5)
p.savefig("figs/rt.png")
