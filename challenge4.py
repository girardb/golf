def s(e):
    p=[[[],[]]];n=[];o=[];x=0;l=''
    for c in e:
        d=c.isdigit()
        if not d and x:n+=[l];l=''
        if len(n)==2and o:n+=[n.pop(0)+' '+n.pop(0)+' '+o.pop(0)]
        if c=='(':p+=[[n,o]];n=[];o=[]
        elif d:l+=c
        elif c==')':p[-1][0]+=[n[0]];n,o=p.pop()
        elif c==' ':pass
        else:o+=[c]
        x=d
    if len(n)==2:n+=[n.pop(0)+' '+n.pop(0)+' '+o.pop(0)]
    elif x:n+=[l];n+=[n.pop(0)+' '+n.pop(0)+' '+o.pop(0)]
    return n[0]
