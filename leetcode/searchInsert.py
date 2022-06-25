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

