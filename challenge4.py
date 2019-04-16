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


def c(operations):
    # Rajouter un truc pour les parenthèses
    # resolve les parenthèses
    #collections -> popleft pour que l'algo soit plus rapide

    print(operations)
    operations = operations.replace(' ', '')
    operation_stack = []
    numbers_stack = []
    for character in operations:
        if character.isdigit():
            numbers_stack.append(character)
        else:
            operation_stack.append(character)

        print(operation_stack, numbers_stack)

        if len(numbers_stack) == 2 and len(operation_stack) > 0 and operation_stack[-1]!='(' and operation_stack[-1]!=')':
            numbers_stack.append(numbers_stack.pop(0) + ' ' + numbers_stack.pop(0)+ ' ' + operation_stack.pop())
        print(operation_stack, numbers_stack)
        print()

    print(operation_stack, numbers_stack)
    return numbers_stack[0]


def c_recursif(operations): #operations en liste
    operation_stack = []
    numbers_stack = []

    if operations[0] == '(':
        #rentre un niveau plus loin
        pass
    elif operations[0] == ')':
        #monte d'un niveau
        pass
    else:
        if operations[0].isdigit():
            number_stack.append(operations.pop(0))
        else:
            operation_stack.append(operations.pop(0))

    #continue tant que ...

    # pogne (, rentre dans un scope
    # pogne ), sort du scope
    pass



print(c('(5 - 6) * 2 / (1 + 3)'))
#print(c('((5 - 3) * ((4 / 2 - 1) * 2))'))
