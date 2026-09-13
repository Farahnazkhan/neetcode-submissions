class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashSet = {}
        
        for i in range(len(s)):
            hashSet[s[i]] = hashSet.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if t[i] not in hashSet:
                return False
            elif hashSet[t[i]] == 1:
                hashSet.pop(t[i])
            else:
                hashSet[t[i]] = hashSet[t[i]] - 1
        return len(hashSet) == 0
        