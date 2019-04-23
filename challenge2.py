import copy
"""
first -> (0,0)
second -> (0,1), (1,0)
third -> (0,2), (1,1), (2,0)
fourth -> (0,3), (1,2), (2,1), (3,0)
...
"""
"""
# 1. Faire le dictionnaire des positions
# 2. Trouver les différentes permutations
# 3. Évaluer l'aire et le périmètre des permutations
# 4. Choisir elle qui minimise l'aire et le périmètre
# 5. Return un cadre avec ces dimensions là avec les mots en input
"""
list_of_words=['1','2','3','4']
o_matrix = [[list_of_words[0]]]

def permut(words, matrix, index):
    if index == len(words):
        max_length = max([len(' '.join(row)) for row in matrix])
        x=copy.deepcopy(matrix) # pourquoi est-ce que j'ai besoin de ca, ahhhhhhhhhh

        # ca maximise l'aire mais pas le périmètre

        return ((2*(max_length+4) + 2*len(matrix)+2) + ((len(matrix)+2)*(max_length+4)), x)
    else:
        # same line
        matrix[-1].append(words[index])
        print('same_line', matrix)
        same_line = permut(words, matrix, index+1)

        # revert the same_line thingy
        matrix[-1].pop()

        # descendre d'une ligne
        matrix.append([words[index]])
        print('next_line', matrix)
        next_line = permut(words, matrix, index+1)
        # Remove the empty bracket caused by popping from a bracket with 1 element
        matrix.pop()
        print(same_line, next_line)
        return min(same_line, next_line)

def print_in_a_frame(words, matrix):
    size = max([len(' '.join(row)) for row in matrix[1]])
    print('*' * (size + 4))
    for row in matrix[1]:
        words_in_row = ' '.join(row)
        print(f'* {words_in_row:{size}} *')
    print('*' * (size + 4))

print_in_a_frame(list_of_words, permut(list_of_words[1:], o_matrix, 0))
