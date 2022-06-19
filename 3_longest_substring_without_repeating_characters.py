class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r = 0, 1
        seen = {s[0]}
        res = 0

        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])

        return res
