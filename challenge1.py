#List comprehension, Map-filter, reduce

#f=input()
#s=input()
def c(f,s):
    #3 caractères de plus pour initialiser o, peut-être que je peux les perdre en changeant la ligne du if
    o=" "*4;s=s.replace(' ', '');j=0
    for i in range(len(f)):
        d=int(f[i].lower()==s[j].lower())
        o+=f'[{f[i]}]'*d or f[i];j+=d
        if o[-4]==']'and d:o=o[:-4]+o[-2:] ##
    return o.strip()

#Jsuis pas mal certain qu'il y a quelque chose de pas efficace là-dedans

print(c("She believed", "He lied"))
