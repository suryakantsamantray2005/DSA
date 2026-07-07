class Solution:
    def findDisappearedNumbers(self, nums):
        L=[]
        for i in nums:
            index=abs(i)-1
            nums[index]=-abs(nums[index]) # always make the element negative
        for i in range(0,len(nums)):
            if nums[i]>0:
                L.append(i+1)
        return L  
# optimal solution