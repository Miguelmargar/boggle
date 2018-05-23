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
def all_grid_neighbours(grid):
    return {pos: [ n for n in get_neighbours(pos) if n in grid] for pos in grid}
#we use get_neighbours(pos) in the dictionary comprenhension and not neighbours as above as neighbours is specified above before needing it whereas in the dictionary comprenhension is used before it is created due to the syntax.    
    
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
    return set(words) 
    # set is a different data structure which quickly says if something is in the dataset. a set data structure also removes duplicates. a list is slow in checking if something is included in the list specially if it is a big list as here we run into exponential growth in time needed to find all the posibilities if we increase the grid size so "set" helps with this. set makes it O1 and a list would be O n. 
 
#this function searches    
def search(grid, wordlist):
    all_neighbours = all_grid_neighbours(grid)

    def do_search(path, positions):
        # If no more positions to search, there won't be any more words    
        if positions == []:
            return []
        
        # Extend the path by the first position and check if it's a word    
        this_position = positions[0]
        this_path = path + [this_position]
        this_word = path_to_word(grid, this_path)
        # Either it was a word, or it wasn't
        if this_word in wordlist:
            words = [this_word]
        else:
            words = []

        # Find which neighbours of the current position, have not been used
        # Search on extending the current path by the neighbours
        neighbours = [n for n in all_neighbours[this_position] if n not in path]
        words += do_search(this_path, neighbours)
        
        # Search on from the last path, using the siblings of the current position
        words += do_search(path, positions[1:])
        
        # Return all the words found on this branch
        return words
            
    return do_search([], list(grid.keys()))   


#displays the words
def display(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))

#main function putting everthing together
def main():
    grid = make_grid(3, 3)
    dictionary = read_wordfile("bogwords.txt")
    words = set(search(grid, dictionary))
    display(words)

if __name__ == "__main__": 
    main()
    