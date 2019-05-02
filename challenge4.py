def solve(e):
    p=[[[],[]]];n=[];o=[]
    for c in e:
        if c=='(':p+=[[n,o]];n=[];o=[]
        elif c.isdigit():n+=[c]
        elif c==')':p[-1][0]+=[n[0]];n,o=p.pop()
        elif c==' ':pass
        else:o+=[c]
        if len(n)==2and o:n+=[n.pop(0)+' '+n.pop(0)+' '+o.pop(0)]
    return n[0]
