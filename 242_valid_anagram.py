class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = dict()
        for char in s:
            if char not in lookup.keys():
                lookup[char] = 1
            else:
                lookup[char] += 1

        for char in t:
            if char not in lookup.keys():
                return False
            else:
                lookup[char] -= 1
        
        for val in lookup.values():
            if not val == 0:
                return False
        
        return True

