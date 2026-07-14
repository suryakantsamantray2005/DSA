class Solution:
    def maxDepth(self, s):
        current_depth=0
        maximum_depth=0
        for i in s:
            if i=='(':
                current_depth+=1
                if current_depth>maximum_depth:
                    maximum_depth=current_depth
            elif i==')':
                current_depth-=1
        return maximum_depth