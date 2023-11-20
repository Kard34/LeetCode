class Solution(object):
    def maxFrequency(self, nums, k):
        diff = [], count = 1
        for i in range(0, len(nums) - 1):
            diff.append(abs(nums[i + 1] - IN[i]))
        diff = sorted(diff, reverse = True)
        while(True):
            x = diff.pop()
            if k > x:
                count += 1
                k -= x
            if k < x or k <= 0 or len(diff) <= 0:
                break
        return count