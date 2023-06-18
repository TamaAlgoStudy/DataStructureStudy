nums = [2, 7, 11, 15]
target = 9

# 1
class Solution(object):
    def twoSum(self, nums, target):
      nums_list = []
      for x in range(len(nums)):
        for y in range(len(nums)):
          if nums[x] + nums[y] == target:
            nums_list.extend([nums[x],nums[y]])
            return nums_list
          
Solution = Solution()
result = Solution.twoSum(nums, target)
print(result)
# [2, 7]

# 2
class Solution(object):
    def twoSum(self, nums, target):
        nums_list = [(x, y) for x in nums for y in nums if x + y == target]
        return nums_list

solution = Solution()
result = solution.twoSum(nums, target)
print(result)
# [(2, 7), (7, 2)] ????