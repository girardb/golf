def c(f,s):
    o="";j=0;x=0
    for i in range(len(f)):
        if s[j]==' ':j+=1
        d=int(f[i].lower()==s[j].lower())
        o+='['*d*(x^1)+']'*x*(d^1)+f[i];j+=d;x=d
    return o +']'*d


print(c("She believed", "He lied"))
