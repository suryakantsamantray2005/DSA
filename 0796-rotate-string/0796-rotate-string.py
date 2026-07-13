class Solution:
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        if s==goal:
            return True
        result=s+s
        if goal in result:
            return True
        return False