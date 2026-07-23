class Solution:
    def longestCommonPrefix(self, strs):
        result = ''
        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if i>=len(strs[j]):
                    return result
                elif strs[j][i]!=strs[0][i]:
                    return result
            result=result+strs[0][i]
        return result 