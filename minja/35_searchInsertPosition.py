class Solution(object):
    def searchInsert(self, nums, target):
        if nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            for i in range(1,len(nums)):
                if nums[i] >= target:
                    return i

sol = Solution()

print(sol.searchInsert([1, 3, 5, 6], 5))