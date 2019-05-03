import copy
def p(w,m,i):
    if i==len(w):
        l=max([len(' '.join(r)) for r in m])
        x=copy.deepcopy(m)
        return 2*(l+4)+2*len(m)+2+(len(m)+2)*(l+4),x
    else:
        m[-1]+=[w[i]]
        s=p(w,m,i+1)
        m[-1].pop()
        m+=[[w[i]]]
        n=p(w,m,i+1)
        m.pop()
        return min(s,n)
def f(w):
    w=w.split()
    m=p(w[1:],[[w[0]]],0)
    s=max([len(' '.join(r)) for r in m[1]])
    print('*'*(s+4))
    for r in m[1]:
        k=' '.join(r)
        print(f'* {k:{s}} *')
    print('*'*(s+4))
