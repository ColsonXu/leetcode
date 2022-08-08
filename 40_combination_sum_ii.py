class Solution:
    def combinationSum2(self, nums, target):
        res = []
        nums.sort()

        def dfs(curr, i, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(curr, i + 1, total + nums[i])
            
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(curr, i + 1, total)

        dfs([], 0, 0)
        return res
