class Solution:
     def removeOuterParentheses(self, s):
          i=0
          j=0
          count=0
          result=''
          while j<len(s):
               if s[j]=='(':
                    count+=1
               if s[j]==')':
                    count-=1
               if count==0:
                    result=result+s[i+1:j]
                    i=j+1
               j+=1
          return result