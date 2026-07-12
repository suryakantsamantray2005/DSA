class Solution:
    def arrayRankTransform(self, arr):
        L=[]
        old_arr=list(arr)
        arr.sort()
        hash={}
        rank=1
        i=0
        while i<len(arr):
            if arr[i] not in hash:
                hash[arr[i]]=rank
                rank+=1
            i+=1
        for j in old_arr:
            L.append(hash.get(j))
        return L