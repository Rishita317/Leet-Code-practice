class Solution:

    def findMin(self, nums: List[int]) -> int:
        # initialize lower and upper bound 
        left,right = 0, len(nums) - 1

        # continue searching if  the search space has more than one element
        while left < right: 
            # floor division to find the middle
            mid = (left + right)//2

            # if middle element is greater than the rightmost 
            # element means the smallest value is towards the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # move towards the left if mid is <= nums right
                right = mid

        return nums[left]


        
