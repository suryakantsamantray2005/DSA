class Solution:
    def  validStrings(self, n):
        ans=['0','1']
        if n==1:
            return ans
        for i in range(2,n+1):
            new_ans=[]
            for j in range(0,len(ans)):
                if ans[j][-1]=='1':
                    new_ans.append(ans[j]+'0')
                    new_ans.append(ans[j]+'1')
                else:
                    new_ans.append(ans[j]+'1')
            ans=new_ans
        return ans       