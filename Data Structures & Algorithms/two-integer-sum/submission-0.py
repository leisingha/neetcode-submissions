class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return sorted([index, dict[complement]])
            else:
                dict[num] = index
            