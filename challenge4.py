"""
Input: (3 * 4) * 2 + 1
>>> 3 4 * 2 * 1 +

Input: (5 - 6) * 2 / (1 + 3)
>>> 5 6 - 2 * 1 3 + /

Input: (4 - 1) / (2 - 3)
>>> 4 1 - 2 3 - /

Input: ((5 - 3) * ((4 / 2 - 1) * 2))
>>> 5 3 - 4 2 / 1 - 2 * *

Input: (4 ^ 2) * 3
>>> 4 2 ^ 3 *

Input: 4 ^ (3 - 1)
>>> 4 3 1 - ^
"""

# Ca ressemble à quelque chose qui peut être fait recursivement. Peut-être avec moins de lignes de code?
def solve(e):
    e=e.replace(' ', '')
    p=[([],[])] # il y a probablement une manière plus clean de faire ca
    n=[];o=[]
    for c in e:
        if c=='(':
            p+=[(n,o)];n=[];o=[]
        elif c.isdigit():
            n+=[c]
        elif c==')':
            p[-1][0].append(n[0]);n,o=p.pop()
        else:
            o+=[c]
        if len(n)==2and o:
            n+=[n.pop(0).strip()+' '+n.pop(0).strip()+' '+o.pop(0)+' ']
    return n[0][:-1]

#print(solve('(5 - 6) * 2 / (1 + 3)'))


"""
levels = equation.count('(')
def solve2(equation, index):
    if index ==len(equation):
        return #...
"""















#print(c('(5 - 6) * 2 / (1 + 3)'))
#print(c('((5 - 3) * ((4 / 2 - 1) * 2))'))
