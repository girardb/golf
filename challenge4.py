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

# Il y a une erreur d'espaces dans la string finale, je suspecte que c'est quand je change de niveau avec les parenthèses
def solve(equation):
    equation=equation.replace(' ', '')
    parentheses_levels=[([],[])]
    numbers_stack = []
    operations_stack = []
    for character in equation:
        if character == '(':
            # save les stacks du niveau plus haut
            # solve cette parenthèse là
            parentheses_levels.append((numbers_stack,operations_stack))
            numbers_stack = [] #clean stack # reinitialise au niveau de la fonction?
            operations_stack = [] #clean stack #reinitialise au niveau de la fonction?

        elif character.isdigit():
            numbers_stack.append(character)

        elif character == ')':
            # get the stacks from the previous level
            if numbers_stack[0]: # s'il y a un chiffre dans numbers_stack
                #print(parentheses_levels[-1], parentheses_levels[-1][0])
                parentheses_levels[-1][0].append(numbers_stack[0])
                numbers_stack = parentheses_levels[-1][0]
            else:
                numbers_stack = parentheses_levels[-1][0]
            # operations est supposé être vide si c'est une équation qui marche
            operations_stack = parentheses_levels[-1][1] #
            parentheses_levels.pop()

            #Jpourrais essayer de mettre ca plus court avec
            # numbers_stack,operations_stack = parentheses_levels.pop(-1)
            # mais il faut que je trouve une manière de rajouter le chiffre qui peut être dans le numbers_stack courant



        else: #caractere est une opération
            operations_stack.append(character)

        #print(operations_stack, numbers_stack, character)
        if len(numbers_stack) ==2 and operations_stack:
            #concaténer les deux nombres pis l'opération et remettre dans numbers
            numbers_stack.append(numbers_stack.pop(0).strip() + ' ' + numbers_stack.pop(0).strip() + ' ' + operations_stack.pop(0) + ' ')
        #print(numbers_stack, operations_stack, character)

    return numbers_stack[0][:-1] # ou .strip() pour enlever le dernier ' '

#print(solve('(5 - 6) * 2 / (1 + 3)'))



#print(c('(5 - 6) * 2 / (1 + 3)'))
#print(c('((5 - 3) * ((4 / 2 - 1) * 2))'))
