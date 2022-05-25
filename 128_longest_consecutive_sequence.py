class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consec = 0

        for x in num_set:
            if x - 1 not in num_set:
                consec = 1
                while x + consec in num_set:
                    consec += 1
                max_consec = max(max_consec, consec)

        return max_consec
