grid = [[2,4,1], [3,1,2], [1,1,1], [3,3,2]]

def reorder(grid_in):
    sums={}
    for i, line in enumerate(grid_in):
        for j in range(len(grid_in[0])):
            line.sort() # je dois le faire moi-même? # je dois faire le time sort?
            sums[sum(line)] = line

    new_grid = []
    for key in sorted(list(sums.keys())):
        new_grid.append(sums[key])
    return new_grid

print(reorder(grid))

#print(grid)
