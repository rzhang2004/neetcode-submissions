class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # min eating speed is 1
        # max is max(piles)

        l = 1
        r = max(piles)
        k = r

        while l <= r:
            rate = (l+r)//2

            # find time
            time = sum([-(pile // -rate) for pile in piles])

            if time <= h:
                k = min(k, rate)
                r = rate - 1 # try smaller rate
            else:
                # try bigger rate
                l = rate + 1
        
        return k
            