def c(f,s):
    o='';j=0;x=0
    for i in f:
        if s[j]==' ':j+=1
        d=i.lower()==s[j].lower()
        o+='['*d*(x^1)+']'*x*(d^1)+i;j+=d;x=d
    return o+']'*d
