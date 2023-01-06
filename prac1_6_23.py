# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order

class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # loop through the nums list 
        # enumerate function lets us see the index and value of that index in one go. 
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and i != j:
                    return (i, j)

# print(Solution.twoSum([2,7,11,15], 9))

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

print(Solution.isPalindrome(122))
