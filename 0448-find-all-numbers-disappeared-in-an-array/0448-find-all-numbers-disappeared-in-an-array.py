class Solution:
    def findDisappearedNumbers(self, nums):
        last_int=len(nums)
        S=set(nums)
        L=[]
        for i in range(1,last_int+1):
            if i not in S:
                L.append(i)
        return L