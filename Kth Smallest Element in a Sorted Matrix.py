# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2

# Think about what data structure to use before juming into solving this problem
# Solution whith comments

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # getting the number of rows and columns in a matrix. 
        n = len(matrix)
        
    # using a min heap - smallest element is always on the top
    # each parent node is smaller than its child nodes 
    # we are uisng this to keep track of the smallest eleamts in the matrix

        min_heap = []

    # Adding the elemnets in each row into the min_heap
    #  only adding elemenst upto K rows (no need to add more  if K< n)
        for row in range(min(k,n)):
            heapq.heappush(min_heap, (matrix[row][0], row, 0))

        # counting how many elemnts have we popped (removed) form the heap
        count = 0

        while min_heap:
            # pop the smallest value from the heap
            # val below means the value that we are instrested in the matrix
            val, row, col = heapq.heappop(min_heap)
            # incrementing pop count
            count += 1 

            # K is our target value 
            if count == k:
                return val
            
            # If there is a next column in the same row, 
            # push that value into the heap

            if col + 1 < n:
                next_val = matrix[row][col + 1]
                heapq.heappush(min_heap, (next_val, row, col +1))





 
