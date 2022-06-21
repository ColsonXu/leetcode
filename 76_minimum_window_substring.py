class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_dict, t_dict = {}, {}
        
        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)

        need = len(t_dict)
        have = 0
        res = ""

        l = 0
        for r in range(len(s)):
            c = s[r]
            window_dict[c] = 1 + window_dict.get(c, 0)
            
            if c in t_dict and window_dict[c] == t_dict[c]:
                have += 1
            
            while have == need:
                if r + 1 - l < len(res) or res == "":
                    res = s[l:r+1]
                window_dict[s[l]] -= 1
                if s[l] in t_dict and window_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1

        return res
