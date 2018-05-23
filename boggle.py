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

#this is the above but in dictionary comprenhension  
# def make_grid_dc(cols, rows):
#     return {(c, r): choice(ascii_uppercase) 
#                     for c in range(cols) 
#                     for r in range(rows)}


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
# def all_grid_neighbours(grid):
#     neighbours_of = {}
#     for pos in grid:
#         neighbours = get_neighbours(pos)
        
#         real_neighbours = []
#         for n in neighbours:
#             if n in grid:
#                 real_neighbours.append(n)
            
#         neighbours_of[pos] = real_neighbours

#     return neighbours_of

# # this is the above in dictionay comprenhension   
def all_grid_neighbours_dc(grid):
    return {pos: [ n for n in neighbours if n in grid] for pos in grid}
    
def path_to_word(grid, path):
    word = ""
    for pos in path:
        word += grid[pos]  #this is the same as saying word = word + grid[pos] - grid[pos] gets the value of grid which is a dictionary in each of pos which pos is each item in the path.
    return word
    #if we did the above in a list comprenhension we will end up with a list of letters and then have to join the list of letters to make a string
 
#this is to get the words list so that they can be compared  
def read_wordfile(filename):
    f = open(filename, "r") # opens file
    words = f.read().split("\n") # reads file
    words = [ w.upper() for w in words] #this is to make all words uppercase
    f.close() # closes file
    return words
    