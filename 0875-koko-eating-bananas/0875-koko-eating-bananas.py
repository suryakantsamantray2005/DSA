class Solution:
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        while low<=high:
            ceil=0
            mid=(low+high)//2
            for i in piles:
                j = (i + mid - 1) // mid
                ceil=ceil+j
            if ceil<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans