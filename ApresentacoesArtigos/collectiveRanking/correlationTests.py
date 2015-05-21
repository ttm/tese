import numpy as n

vp=     n.random.randint(0,1000000,100000)
vn=     n.random.randint(0,1000000,100000)
puladas=n.random.randint(0,1000000,100000)
eta=vp+vn+puladas

alpha=(vp-vn)/eta
gamma=(vp+vn)/eta

etaM=eta.max()
etam=eta.min()
etaM_=etaM-eta
etam_=eta-etam
etaFoo=n.vstack((etaM_,etam_))

eta_=etaFoo.max(0) # max de cada entre etaM_ e etam_

# comparar os alphas_
alpha_=(10000000*alpha)/eta_
alpha__=(vp-vn)/eta_
c1=n.correlate(alpha_,alpha__)
from scipy import stats
c2=stats.pearsonr(alpha_,alpha__)
c3=stats.spearmanr(alpha_,alpha__)
