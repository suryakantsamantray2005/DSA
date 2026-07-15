class Solution:
    def gcdOfOddEvenSums(self, n):
        even=n**2
        odd=n*(n+1)
        while odd!=0:
            even,odd=odd,even%odd
        return even