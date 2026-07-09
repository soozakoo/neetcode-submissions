class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # value -> index
        for j, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], j]
            seen[x] = j