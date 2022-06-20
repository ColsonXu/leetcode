class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counter = {}
        res = 0
        most_common = 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            most_common = max(most_common, counter[s[r]])

            if (r + 1 - l) - most_common > k:
                counter[s[l]] -= 1
                l += 1

            res = max(r + 1 - l, res)

        return res
