class Solution:
    def isPowerOfTwo(self, n):
        for i in range(0,33):
            if self.mypow(2,i)==n:
                return True
        return False
    def mypow(self,x,n):
        ans=1
        k=n
        if n==0:
            return 1
        if n<0:
            n=-n
        while n>0:
            if n%2==0:
                x=x*x
                n=n//2
            else:
                ans=ans*x
                n=n-1
        if k<0:
            return 1/ans
        else:
            return ans