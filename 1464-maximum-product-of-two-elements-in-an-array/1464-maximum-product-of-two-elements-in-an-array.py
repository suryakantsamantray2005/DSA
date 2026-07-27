class Solution:
    def maxProduct(self, nums):
        first_max=float('-inf')
        sec_max=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]>first_max:
                sec_max=first_max
                first_max=nums[i]
            elif nums[i]<=first_max and nums[i]>sec_max:
                sec_max=nums[i]
        return (first_max-1)*(sec_max-1)