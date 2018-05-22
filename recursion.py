#recursion has to call itself within it, needs a stop(will in most cases be an if statement), and needs to move you towards the stop statement.
def sumlist(l):
    if l == []:
        return 0
    else:
        first = l[0]
        rest = l[1:]
        return first + sumlist(rest)

    
print(sumlist([1, 4, 13, 34, 56]))

# look for the highest number in thelist with recursion
def maxlist(l):
   if len(l) == 1:
        return l[0] 
   else:
        first = l[0]
        rest = l[1:]
        max_of_rest = maxlist(rest)
        if first > max_of_rest:
            return first
        else:
            return max_of_rest
                
                
print(maxlist([2, 13, 5, 7, 8]))