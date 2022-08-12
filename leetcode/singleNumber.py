# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant 
# extra space.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        doubleSum = 0
        diffSum = 0
        numSet = set()
        for num in nums:
            diffSum += num
            numSet.add(num)
        for x in numSet:
            doubleSum += (2*x)

        return doubleSum - diffSum