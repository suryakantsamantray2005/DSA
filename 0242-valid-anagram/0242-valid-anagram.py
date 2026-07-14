class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for j in t:
            if j in freq:
                freq[j]-=1
                if freq[j]<0:
                    return False
            else:
                return False
        for k in freq.values():
            if k!=0:
                return False
        return True