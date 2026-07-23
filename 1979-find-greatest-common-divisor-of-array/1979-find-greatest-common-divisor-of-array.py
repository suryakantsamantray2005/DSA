class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest=min(nums)
        greatest=max(nums)
        while greatest!=0:
           smallest, greatest=greatest,              smallest%greatest
        return smallest