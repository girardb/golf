from threading import Timer
from time import sleep

def time_sort(array):
    threads=[]
    sorted_array = []
    for elem in array:
        thread=Timer(elem, lambda x: sorted_array.append(x), args=(elem,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    return sorted_array

grid = [[2,4,1], [3,1,2], [1,1,1], [3,3,2]]

def reorder(grid_in):
    sums={}
    for i, line in enumerate(grid_in):
        for j in range(len(grid_in[0])):
            line = time_sort(line) # je dois le faire moi-même? # je dois faire le time sort?
            sums[sum(line)] = line

    new_grid = []
    for key in time_sort(list(sums.keys())): # algo de sort ici aussi
        new_grid.append(sums[key])
    return new_grid





print(reorder(grid))

#print(grid)
