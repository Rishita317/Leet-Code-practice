# This problem also uses hashmaps but the varible names are much better in the other file
# called Two Sum with Hashmaps. So for simplicity refer to the other file if you are beginner

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dir = {}

        for i, c_value in enumerate(nums):
            Complement = target - c_value

            if Complement in num_dir:
                return [num_dir[Complement], i]

            # This line should not be indented under the if statement
            num_dir[c_value] = i

        # This return statement should be outside the for loop
        return []
