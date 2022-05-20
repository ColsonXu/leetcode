class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {num: 0 for num in nums}
        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in count.keys() and count[complement] >= 1 and not nums.index(complement) == i:
                return [i, nums.index(complement)]

