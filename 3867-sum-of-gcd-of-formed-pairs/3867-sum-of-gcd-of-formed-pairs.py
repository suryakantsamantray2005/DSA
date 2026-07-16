class Solution:
    def gcdSum(self, nums):
        prefixGcd=[]
        max_element=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]>max_element:
                max_element=nums[i]
            result=self.calculategcd(nums[i],max_element)
            prefixGcd.append(result)
        prefixGcd.sort()
        j=0
        k=len(prefixGcd)-1
        sum_gcd=0
        while j<k:
            final_result=self.calculategcd(prefixGcd[j],prefixGcd[k])
            sum_gcd+=final_result
            j+=1
            k-=1
        return sum_gcd
    def calculategcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a