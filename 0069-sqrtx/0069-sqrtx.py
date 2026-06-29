class Solution:
    def mySqrt(self,n):
        if n==0:
            return 0
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            if (mid*mid)==n:
                return mid
            elif (mid*mid)>n:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans