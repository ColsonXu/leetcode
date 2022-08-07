class Solution:
    def permute(self, nums):
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in nums:
            n = nums.pop(0)
            perms = self.permute(nums)
        
            for perm in perms:
                perm.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res
