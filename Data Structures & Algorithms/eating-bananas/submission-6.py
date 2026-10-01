class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best_rate = r

        while l <= r:
            rate = (l+r)//2
            time = 0
            for p in piles:
                time += -round(-p // rate)
                if time > h:
                    break
            
            if time <= h: # fast enough, try lower rate
                best_rate = min(best_rate, rate)
                r = rate - 1
            else: # too slow
                l = rate + 1
        
        return best_rate
