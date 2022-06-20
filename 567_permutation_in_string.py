from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        for r in range(len(s1), len(s2) + 1):
            if s1_counter == Counter(s2[r-len(s1):r]):
                return True
        return False
