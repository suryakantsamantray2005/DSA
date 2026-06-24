class Solution:
    def searchRange(self,nums,target):
        low=0
        high=len(nums)-1
        ans=-1
        L=[]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        low=0
        high=len(nums)-1
        ans1=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans1=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        L.append(ans)
        L.append(ans1)
        return L