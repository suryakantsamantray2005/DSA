class Solution:
    def firstStableIndex(self, nums, k):
        i=0
        j=1
        l=0
        while j<=len(nums):
            if max(nums[i:j])-min(nums[l:len(nums)])<=k:
               return l
            j+=1
            l+=1
        return -1
