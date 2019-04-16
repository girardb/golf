#List comprehension, Map-filter, reduce
"""
def c1(f,s):
    z=T=True
    s=s.replace(' ', '')
    j=0
    o=''
    F=False
    for i in range(len(f)):
        if f[i].lower()==s[j].lower():
            j+=1
            if z is T:
                o+='['
                z=F
        else:
            if z is F:
                z=T
                o+=']'
        o+=f[i]
    if z is F:
        o+=']'
    return o
"""
#f=input()
#s=input()
def c(f,s):
    o="    "
    s=s.replace(' ', '')
    j=0
    for i in range(len(f)):
        d = int(f[i].lower()==s[j].lower())
        o+=f'[{f[i]}]'*d or f[i]
        j+=d
        if o[-4] == ']'and d:
            o=o[:-4]+o[-2:]
        #o=(o[:-4]+o[-2:]*int(o[-4] == ']' and d))or o
    return o.strip()

"""
def c3(f,s):
    s=s.replace(' ', '')
    i=0
    j=0
    o=list(f)
    while i<len(s):
        if s[i].lower() == f[j].lower():
            o.insert(j, '[')
            o.insert(j+2, ']')
            i+=1
        j+=1
    print(o)
"""

#print(c1("She believed", "He lied"))
print(c("She believed", "He lied"))
#c3("She believed", "He lied")
