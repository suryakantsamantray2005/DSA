class Solution:
    def magneticballstobeplaced(self, position, force,m):
        force_=1
        lastposition=position[0]
        for i in range(1,len(position)):
            if position[i]-lastposition>=force:
                force_+=1
                lastposition=position[i]
        if force_>=m:
            return True
        else:
            return False
    def  maxDistance(self, position, m):
        position.sort()
        low=1
        high=position[-1]-position[0]
        while low<=high:
            mid=(low+high)//2
            if self.magneticballstobeplaced(position,mid,m)==True:
                low=mid+1
            else:
                high=mid-1
        return high