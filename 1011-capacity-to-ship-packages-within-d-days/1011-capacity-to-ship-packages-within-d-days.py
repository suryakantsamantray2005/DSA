class Solution:
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while low<=high:
            total_weight=0
            count=0
            mid=(low+high)//2
            for i in weights:
                total_weight+=i
                if total_weight>mid:
                    total_weight=i
                    count+=1
            if count<days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans