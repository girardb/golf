import copy

list_of_words=['1','2','3']
o_matrix = [[list_of_words[0]]]

def permut(words, matrix, index):
    if index == len(words):
        max_length = max([len(' '.join(row)) for row in matrix])
        x=copy.deepcopy(matrix) # pourquoi est-ce que j'ai besoin de ca, ahhhhhhhhhh

        # ca maximise l'addition de l'aire et du périmètre
        # si c'est pas correct il faudrait que je compare en premier l'aire et si elles sont égales, ensuite le périmètre

        return ((2*(max_length+4) + 2*len(matrix)+2) + ((len(matrix)+2)*(max_length+4)), x)
    else:
        # same line
        matrix[-1].append(words[index])
        same_line = permut(words, matrix, index+1)

        # revert the same_line thingy
        matrix[-1].pop()

        # descendre d'une ligne
        matrix.append([words[index]])
        next_line = permut(words, matrix, index+1)

        # Remove the empty bracket caused by popping from a bracket with 1 element
        matrix.pop()

        return min(same_line, next_line)

def print_in_a_frame(words, matrix):
    size = max([len(' '.join(row)) for row in matrix[1]])
    print('*' * (size + 4))
    for row in matrix[1]:
        words_in_row = ' '.join(row)
        print(f'* {words_in_row:{size}} *')
    print('*' * (size + 4))

#print_in_a_frame(list_of_words, permut(list_of_words[1:], o_matrix, 0))
