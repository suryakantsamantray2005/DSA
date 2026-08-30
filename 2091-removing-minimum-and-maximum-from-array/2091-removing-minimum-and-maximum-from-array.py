class Solution:
    def minimumDeletions(self, nums):
        max_int=float('-inf')
        min_int=float('inf')
        for i in range(0,len(nums)):
            if nums[i]>max_int:
                max_int=nums[i]
                max_int_index=i
        for j in range(0,len(nums)):
            if nums[j]<min_int:
                min_int=nums[j]
                min_int_index=j
        #deletions from left
        count_left=max(max_int_index,min_int_index)+1
        #deletion from right
        count_right=len(nums)-min(max_int_index,min_int_index)
        #deletion from left and right
        count=0
        for k in range(0,min(max_int_index,min_int_index)+1):
            count+=1
        for l in range(len(nums),max(min_int_index,max_int_index),-1):
            count+=1
        return min(count_left,count_right,count)