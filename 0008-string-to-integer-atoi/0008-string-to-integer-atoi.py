class Solution:
    def myAtoi(self,s):
        count=0
        result=0
        negative_sign=False
        count_plus=0
        count_minus=0
        for i in s:
            if i==' ' and count==0:
                continue
            elif i=='+' and count==0:
                count_plus+=1
                if count_plus>1:
                    return 0
                elif count_minus==1:
                    return 0
                count=1
                continue
            elif i=='-' and count==0:
                count=1
                count_minus+=1
                if count_minus>1:
                    return 0
                elif count_plus==1:
                    return 0
                else: 
                    negative_sign=True
            elif 48<=ord(i)<=57 :
                if count==0:
                    count=1
                result=result*10+int(i)
            else:
                break
        if negative_sign==True:
            result=-result
        if result<(-(2**31)):
            return -(2**31)
        if result>(2**31-1):
            return 2**31-1
        return result