class Solution:
    def missingInteger(self, nums):
        i=0
        j=1
        count=nums[0]
        if len(nums)==1:
            return nums[0]+1
        while j<len(nums):
            if nums[j]-nums[i]==1:
                count=count+nums[j]
            else:
                break
            i+=1
            j+=1
        while True:
            if count not in nums:
                return count
            else:
                count+=1