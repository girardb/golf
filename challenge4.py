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
def solve(equation):
    equation=equation.replace(' ', '')
    parentheses_levels=[([],[])] # il y a probablement une manière plus clean de faire ca
    numbers_stack = []
    operations_stack = []
    for character in equation:
        if character == '(':
            # save les queues du niveau plus haut
            # solve cette parenthèse là
            parentheses_levels.append((numbers_stack,operations_stack))
            numbers_stack = [] #clean queue
            operations_stack = [] #clean queue

        elif character.isdigit():
            numbers_stack.append(character)

        elif character == ')':
            # move up a level and restore the queues
            #print(parentheses_levels[-1][0], numbers_stack, operations_stack)
            parentheses_levels[-1][0].append(numbers_stack[0])
            numbers_stack, operations_stack = parentheses_levels.pop()

        else: #caractere est une opération
            operations_stack.append(character)

        #print(operations_stack, numbers_stack, character)
        if len(numbers_stack) ==2 and operations_stack:
            #print(numbers_stack, operations_stack, character)
            #print()
            #concaténer les deux nombres pis l'opération et remettre dans numbers
            numbers_stack.append(numbers_stack.pop(0).strip() + ' ' + numbers_stack.pop(0).strip() + ' ' + operations_stack.pop(0) + ' ')
        #print(numbers_stack, operations_stack, character)

    return numbers_stack[0][:-1] # ou .strip() pour enlever le dernier ' '

print(solve('(5 - 6) * 2 / (1 + 3)'))



#print(c('(5 - 6) * 2 / (1 + 3)'))
#print(c('((5 - 3) * ((4 / 2 - 1) * 2))'))
