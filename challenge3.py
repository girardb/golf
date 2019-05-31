from threading import Timer
def t(a):
    p,s=[],[]
    for e in a:
        o=Timer(0.01*e,lambda x:s.append(x),args=(e,))
        p+=[o]
        o.start()
    [t.join()for t in p]
    return s
def r(g):
    s={sum(t(l)):t(l)for l in g for j in range(len(g[0]))}
    return[s[k]for k in t([*s])]
