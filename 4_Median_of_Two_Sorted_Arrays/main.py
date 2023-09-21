# LeetCode
# Problem List No.4 (Hard)
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        Merged_Arrays = []
        x = (len(nums1) + len(nums2)) // 2
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] <= nums2[0]:
                Merged_Arrays.append(nums1.pop(0))
            else:
                Merged_Arrays.append(nums2.pop(0))
        while len(nums1) > 0:
            Merged_Arrays.append(nums1.pop(0))
        while len(nums2) > 0:
            Merged_Arrays.append(nums2.pop(0))
        if len(Merged_Arrays) % 2 == 1:
            return Merged_Arrays[x]
        else:
            return (Merged_Arrays[x - 1] + Merged_Arrays[x]) / 2

