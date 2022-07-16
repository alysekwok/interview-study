
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index 
# where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int(low + (high - low)/2) 
            # print(low)
            if target < nums[mid]:
                high = mid - 1
                # print(low)
            elif target > nums[mid]:
                low = mid + 1
                # print(low)
            else:
                return mid
        return low

