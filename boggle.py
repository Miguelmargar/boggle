from string import ascii_uppercase
from random import choice

def check():
    return True
    
def make_grid(cols, rows):
    grid = {}
    for c in range(cols): # if cols is 5 c will be 0 to 4
        for r in range(rows): # if rows is 3 r will be 0 to 2
            grid[(c, r)] = choice(ascii_uppercase) # for dictionary this is used instead of .append - we have imported ascii_uppercase and random choice so we just make it choice(upper_case) and it will give a random choice of letters
    return grid

# positions to letters    
def get_neighbours(pos):
    col, row = pos
    return [
            (col-1, row-1),
            (col, row-1),
            (col+1, row-1),
            (col+1, row),
            (col+1, row+1),
            (col, row+1),
            (col-1, row+1),
            (col-1, row)
            ]
    
#postition of neighbours that are inside the grid. this are the ones from the function above get_neighbours minus the ones that are not in the grid   
def all_grid_neighbours(grid):
    neighbours_of = {}
    for pos in grid:
        neighbours = get_neighbours(pos)
        
        real_neighbours = []
        for n in neighbours:
            if n in grid:
                real_neighbours.append(n)
            
        neighbours_of[pos] = real_neighbours

    return neighbours_of