class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining = target - nums[i]
            for j in range(len(nums)):
                if not i == j and nums[j] == remaining:
                    return [i, j]
