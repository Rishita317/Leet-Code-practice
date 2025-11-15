class Solution:
    def isMajorityElement(self, nums, target):
        n = len(nums)

        # 1. binary search for first index with nums[i] >= target
        left, right = 0, n  # [left, right)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        first = left

        # 2. target not present
        if first == n or nums[first] != target:
            return False

        # 3. check index first + n//2
        check_index = first + n // 2
        if check_index >= n:
            return False

        return nums[check_index] == target
