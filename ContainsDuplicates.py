
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Data structure used to solve this problem : Sets
# defination of a Set - An unordred collection of unique elements
# typically implemented using a hashtable

# As, we have an array that contains unique elements and this makes it easier to solve the problem.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      # defining nums to a set removes duplicates
        unique = set(nums)
      # if teh length is NOT equal to a set there are dulicates
        if len(unique) != len(nums):
            return True
          # if equal there are no duplicates
        else:
            return False
