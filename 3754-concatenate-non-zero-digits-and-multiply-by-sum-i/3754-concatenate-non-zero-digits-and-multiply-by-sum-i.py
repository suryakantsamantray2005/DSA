class Solution:
    def sumAndMultiply(self, n):
        digit_sum=0
        unit_place=1
        result=0
        if n==0:
            return 0
        while n!=0:
            last_digit=n%10
            if last_digit!=0:
                result=last_digit*unit_place+result
                unit_place=unit_place*10
                digit_sum=digit_sum+last_digit
            n=n//10
        return result*digit_sum