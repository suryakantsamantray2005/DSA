class Solution:
    def findPeakGrid(self, mat):
        low=0
        high=len(mat)-1
        while low<=high:
            max_element=float('-inf')
            mid=(low+high)//2
            for i in range(0,len(mat[mid])):
                if mat[mid][i]>max_element:
                    max_element=mat[mid][i]
                    index=i
            if mid==0:
                if mat[mid][index]>mat[mid+1][index]:
                    return [mid,index]
                else:
                    low=mid+1
            elif mid==len(mat)-1:
                if mat[mid][index]>mat[mid-1][index]:
                    return [mid,index]
                else:
                    high=mid-1
            else:
                if mat[mid][index]>mat[mid+1][index] and mat[mid][index]>mat[mid-1][index]:
                    return [mid,index]
                elif mat[mid][index]<mat[mid+1][index]:
                    low=mid+1
                else:
                    high=mid-1