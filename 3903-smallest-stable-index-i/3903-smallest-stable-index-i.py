class Solution:
    def firstStableIndex(self, nums, k):
        maximum_array=[]
        minimum_array=[]
        maximum=nums[0]
        minimum=nums[-1]
        for i in range(0,len(nums)):
            maximum=max(maximum,nums[i])
            maximum_array.append(maximum)
        for j in range(len(nums)-1,-1,-1):
            minimum=min(minimum,nums[j])
            minimum_array.append(minimum)
        for l in  range(0,len(nums)):
            if maximum_array[l]-minimum_array[len(nums)-l-1]<=k:
                return l
        return -1