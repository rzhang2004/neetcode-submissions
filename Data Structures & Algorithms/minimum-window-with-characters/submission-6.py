class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = ""

        if len(t) > len(s):
            return best
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz'
        t_letters = {c:0 for c in alpha}
        s_letters = {c:0 for c in alpha}

        need = 0
        have = 0

        for i in range(len(t)):
            if t_letters[t[i]] == 0:
                need += 1
            t_letters[t[i]] += 1

        l = r = 0
        while r < len(s):
            if t_letters[s[r]] > 0: # if r points at a letter in t
                s_letters[s[r]] += 1
                if s_letters[s[r]] == t_letters[s[r]]:
                    have += 1
                
            # new best
            if have == need:
                if not best or r-l+1 < len(best):
                    best = s[l:r+1]
                
                while have == need:
                    if r-l+1 < len(best):
                        best = s[l:r+1]
                    if t_letters[s[l]] > 0:
                        s_letters[s[l]] -= 1
                        if s_letters[s[l]] < t_letters[s[l]]:
                            have -= 1
                    l += 1
            r += 1
        
        while have == need:
            best = s[l:]
            if t_letters[s[l]] > 0:
                s_letters[s[l]] -= 1
                if s_letters[s[l]] < t_letters[s[l]]:
                    have -= 1
            l += 1
        
        return best
