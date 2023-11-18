# LeetCode
# Problem List No.4 (Hard)
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge_list = sorted(nums1 + nums2)
        half = (len(nums1) + len(nums2)) // 2
        

