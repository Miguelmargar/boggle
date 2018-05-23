
# l = [1, 3, 5]
# p = [n*2 for n in l]
# print(p)

# # the above is the same as the below - this is a list conprenhension

# p = []
# for n in l:
#     p.append(n * 2)
# print(p)


# chanllenge

# print([ i*2 for i in range(7)])


# List Comprehension Challenges
# Example:
# Question 
#                 range(10) 
#                 -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Answer
#                 [n * 2 for i in range(10)]
                
# 1. range(5) 
# -> ["*", "*", "*", "*", "*"]
# ["*" for i in range(5)]

# 2. ["Hi", "There", "Everyone"] 
# -> [2, 5, 8]
# words = ["Hi", "There", "Everyone"]
# [len(i) for i in words] 

# 3. range(8) 
# -> [0, 1, 4, 9, 16, 25, 36, 49]
# [i**2 #i*i# for i in range(8)]

# 4. range(5) 
# -> [(0,1), (1,2), (2,3), (3,4), (4,5)]
# [(x, x+1) for x in range(5)]

# 5. 'woohoo' 
# -> ['w', 'o', 'o', 'h', 'o', 'o']
# word = "woohoo"
# [i for i in "woohoo"]

# 6. ['car', 'cat', 'maps', 'if', 'level'] 
# -> [('car', 3), ('cat', 3), ('maps', 4), ('if', 2), ('level', 5)]
# words = ['car', 'cat', 'maps', 'if', 'level']
# [(i, len(i)) for i in words]

# 7. [(False, False), (False, True), (True, False), (True, True)]
# ->[False, False, False, True]
# tuples = [(False, False), (False, True), (True, False), (True, True)]
# [(i and j) for i,j in tuples]

# 8. [(False, False), (False, True), (True, False), (True, True)]
# ->[False, True, True, True]
# tuples = [(False, False), (False, True), (True, False), (True, True)]
# [(i or j) for i, j in tuples]

Dictionary Comprehension Challenges
Example:
Question 
                range(5) 
                -> { 0: "", 1:"*", 2:"**", 3:"***", 4:"****" }
Answer
                { i:"*" * i for i in range(5)}
                
# 1. ['Hi', 'There', 'Everyone'] 
# -> {'Hi':2, 'There':5, 'Everyone':8}
# list = ['Hi', 'There', 'Everyone']
# {i:len(i) for i in list}

# 2. 'code'
# -> {'c': 99, 'e': 101, 'd': 100, 'o': 111}
# word = "code"
# d = { c:ord(c) for c in word}

3. ['car', 'cat', 'maps', 'if', 'level'] 
-> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}


def maxlist(l):
    if len(l) == 1:
        return l[0]
    else:
        first = l[0]
        maxrest = maxlist(l[1:])
        if first > maxrest:
            return first
        else:
            return maxrest