
def LM(r=2.5,x0=.2,it=5):
    l=[x0]
    for i in range(it):
        l.append(r*l[-1]*(1-l[-1]))
    return l
