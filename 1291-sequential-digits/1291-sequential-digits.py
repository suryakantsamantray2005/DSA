class Solution:
    def sequentialDigits(self, low, high):
        s="123456789"
        L=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if low<=int(s[i:j])<=high:
                    L.append(int(s[i:j]))
                elif int(s[i:j])>high:
                    break
        L.sort()
        return L