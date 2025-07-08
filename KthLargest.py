
# Leetcode 215. Kth Largest Element in an Array
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # yes we can solve it without sorting by using min heap
        # to keep track of the smallest elemens

        # we will use min heap so we can remove the smallest elements
        min_heap = []

        for num in nums:
            # adds the current number of elements to the heap
            heapq.heappush(min_heap, num)

            # If the size of the heap exceeds k, remove the smallest element
            # This ensures that we are only keeping the k largest elements in the heap
            if len(min_heap) > k:

                # popping the heap means removing the largest element
                heapq.heappop(min_heap)
                # After processing all numbers, the heap contains the k largest elements,
                # and the smallest among them (i.e., the kth largest overall) is at the top
        return min_heap[0]
