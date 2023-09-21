# LeetCode
# Problem List No.9 (Easy)
# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution(object):
    def isPalindrome(self, x):
        if x < 0: # Handle negative numbers, which cannot be palindromes
            return False
        Original, Reversed = x, 0
        while x > 0: # Reverse the digit of x
            Reversed = (Reversed + (x % 10)) * 10
            x = x // 10
        Reversed /= 10
        return Original == Reversed # Check if the original number and reversed number are the same

