class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()

        if len(nums3) % 2 != 0:
            return nums3[int(len(nums3)/2)]
        else:
            return (nums3[int(((len(nums3) / 2) - 1))] + nums3[int(((len(nums3) / 2)))]) / 2

s= Solution()
print(s.findMedianSortedArrays([1,2,6,5],[3,8,9]))