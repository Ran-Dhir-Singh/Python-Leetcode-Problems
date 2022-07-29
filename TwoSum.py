class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i

list1=[2,5,7,9,4,1]
s= Solution()
print(s.twoSum(list1,8))