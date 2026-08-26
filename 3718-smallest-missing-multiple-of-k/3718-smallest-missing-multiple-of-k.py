class Solution:
    def missingMultiple(self, nums, k):
        S=set(nums)
        i=1
        while True:
            if i*k not in S:
                return i*k
            else:
                i+=1
