#List comprehension, Map-filter, reduce

#f=input()
#s=input()
def c(f,s):
    #4 caractères de plus pour initialiser o, peut-être que je peux les perdre en changeant la ligne du if
    for i in range(len(f)):
    o="    ";s=s.replace(' ', '');j=0
        d=int(f[i].lower()==s[j].lower())
        o+=f'[{f[i]}]'*d or f[i];j+=d
        if o[-4]==']'and d:o=o[:-4]+o[-2:] ##
    return o.strip()

print(c("She believed", "He lied"))
