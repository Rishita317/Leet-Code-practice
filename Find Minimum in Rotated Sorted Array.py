class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initilize lower and upper bound 
        left,right = 0, len(nums) - 1

        # continue srecahing if  the search space has mor ethan one element
        while left < right: 
            # floor devision to find the middle
            mid = (left + right)//2

            # if middle element is greater than the rightmost 
            # element means the smallest vlue is towerds the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # move towrds the left if mid is <= nums right
                right = mid

        return nums[left]


        
