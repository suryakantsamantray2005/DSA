class Solution:
    def smallestNumber(self, n, t):
        while n<=100:
            rev=1
            i=n
            while i!=0:
                rev=rev*(i%10)
                i=i//10
            if rev%t==0:
                return n
            else:
                n+=1