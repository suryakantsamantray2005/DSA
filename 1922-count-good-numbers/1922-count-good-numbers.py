class Solution:
    def countGoodNumbers(self, n):
        if n%2==1:
            pow_raised=n//2
            a=self.pow(5,n-pow_raised)
            b=self.pow(4,pow_raised)
            return (a*b)%(10**9+7)
        else:
            pow_raised=n//2
            a=self.pow(5,pow_raised)
            b=self.pow(4,pow_raised)
            return (a*b)%(10**9+7)
    def pow(self,x,n):
        ans=1
        k=n
        if n==0:
            return 1
        while n>0:
            if n%2==0:
                x=(x*x)%(10**9+7)
                n=n//2
            else:
                ans=(ans*x)%(10**9+7)
                n=n-1
        return ans