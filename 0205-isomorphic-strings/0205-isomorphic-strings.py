class Solution:
    def isIsomorphic(self, s, t):
        hash={}
        hash_reverse={}
        for i in range(0,len(s)):
            if s[i] in hash:
                if hash.get(s[i])!=t[i]:
                    return False
            else:
                hash[s[i]]=t[i]
        for j in range(0,len(t)):
            if t[j] in hash_reverse:
                if hash_reverse.get(t[j])!=s[j]:
                    return False
            else:
                hash_reverse[t[j]]=s[j]
        return True