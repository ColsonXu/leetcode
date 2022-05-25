class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        postfix = [None] * len(nums)
        
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        res = [postfix[1]]
        for i in range(1, len(nums) - 1):
            res.append(prefix[i-1] * postfix[i+1])
        res.append(prefix[-2])
        
        return res
