class Solution:
    def searchMatrix(self, matrix, target):
        low=0
        high=len(matrix)-1
        while low<=high:
            mid=(low+high)//2
            if matrix[-1][-1]<target:
                return False
            elif matrix[mid][0]<=target<=matrix[mid][-1]:
               break
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                low=mid+1
        low1=0
        high1=len(matrix[mid])-1
        while low1<=high1:
            mid1=(low1+high1)//2
            if matrix[mid][mid1]==target:
                return True
            elif matrix[mid][mid1]>target:
                high1=mid1-1
            else:
                low1=mid1+1
        return False