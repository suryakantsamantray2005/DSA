class Solution:
    def findMissingElements(self, nums):
        S=set(nums)
        result=[]
        a=min(nums)
        b=max(nums)
        for i in range(a,b+1):
            if i not in S:
                result.append(i)
        return result