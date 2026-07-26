class Solution:
    def  maximumProduct(self, nums):
        first_max=float('-inf')
        sec_max=float('-inf')
        third_max=float('-inf')
        first_min=float('inf')
        sec_min=float('inf')
        for i in nums:
            if i>first_max:
                third_max=sec_max
                sec_max=first_max
                first_max=i
            elif i<=first_max and sec_max<i:
                third_max=sec_max
                sec_max=i
            elif i<=first_max and i<=sec_max and i>third_max:
                third_max=i
        for i in nums:
            if i<first_min:
                sec_min=first_min
                first_min=i
            elif i>=first_min and i<sec_min:
                sec_min=i
        return max(first_max*sec_max*third_max,first_min*sec_min*first_max)