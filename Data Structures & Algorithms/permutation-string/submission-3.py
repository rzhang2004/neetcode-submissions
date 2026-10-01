class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        if len(s1) > len(s2):
            return False
        s1_letters = {alpha[i]:0 for i in range(26)}
        s2_letters = {alpha[i]:0 for i in range(26)}

        for i in range(len(s1)):
            s1_letters[s1[i]] += 1
        
        l = 0
        r = len(s1)-1

        for i in range(len(s1)):
            s2_letters[s2[i]] += 1

        while r < len(s2) - 1:
            if s1_letters == s2_letters:
                return True
            r += 1
            s2_letters[s2[l]] -= 1
            l += 1
            s2_letters[s2[r]] += 1
        if s1_letters == s2_letters:
            return True
        
        return False