# Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and 
# you may not use the same element twice.

# You can return the answer in any order.

# first solution; kinda slow
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for index in range(len(nums)):
        if nums[index] in hashmap.keys():
            return [hashmap[nums[index]], index]
        hashmap[target - nums[index]] = index
  
  
# # test cases     
# nums = [2, 11, 7, 15]
# print(twoSum(nums, 9))
# nums2 = [3, 2, 4] # original solution returned [0,0], needed to account for doubles that make the target
# print(twoSum(nums2, 6))


# potential hashmap mapping solutions:
# nums = [2, 7, 11, 15]; target = 9
# hashmap = {2:7, 7:2, 11:-2, 15:-6}
# hashmap = {0:7, 1:2, 2:-2; 3:-6}
# then you can return [hashmap[key], index]

# quicker; this one maps the value to its original index in the list. 
def twoSumv2(nums, target):
    hashmap = {}
    for index in range(len(nums)):
        difference = target - nums[index]
        if difference in hashmap:
            return [index, hashmap[difference]]
        hashmap[nums[index]] = index


# test cases     
nums = [2, 11, 7, 15]
print(twoSumv2(nums, 9))
nums2 = [3, 2, 4] # original solution returned [0,0], needed to account for doubles that make the target
print(twoSumv2(nums2, 6))


    