# You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the 
# ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that 
# you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no 
# limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree 
# (including the start tree) while moving to the right. The picked fruits must fit in one of 
# your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    right = 0
    left = 0
    hashmap = {}
    maxCount = 0
    length = len(fruits)
    while right < length:
        # print(hashmap)
        if len(hashmap) <= 2:
            hashmap[fruits[right]] = right
            right += 1
        if len(hashmap) > 2:
            farthest = min(hashmap.values())
            del hashmap[fruits[farthest]]
            left = farthest + 1
        # print("right:", right)
        # print("left:", left)
        maxCount = max(maxCount, right - left)
    return maxCount
    
 

fruits = [3,3,3,1,2,1,1,2,3,3,4]
'''
[3,3,3,1]
      [1,2,1,1,2]
               [2,3,3]
                 [3,3,4]
keep adding to the count until we hit something different. in that case, go back to the last occurence of the most 
recent value in the list. left = right now 

'''
print(totalFruit(fruits))
fruits1 = [1, 2, 1]
totalFruit(fruits1)
fruits2 = [0,1,2,2]
print(totalFruit(fruits2))
fruits3 = [0,1,6,6,4,4,6]
print(totalFruit(fruits3))
fruits4 = [1,0,1,4,1,4,1,2,3]
print(totalFruit(fruits4))