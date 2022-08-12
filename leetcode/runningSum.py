# Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.


class Solution(object):
    def runningSum(self, nums):
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        total = 0
        for num in nums:
            total += num
            res.append(total)
        return res