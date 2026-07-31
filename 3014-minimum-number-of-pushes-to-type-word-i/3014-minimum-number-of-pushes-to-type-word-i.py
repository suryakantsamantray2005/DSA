class Solution:
    def minimumPushes(self, word):
        count=0
        adder=1
        for i in range(1,len(word)+1):
            if i%8!=0:
                count=count+adder
            else:
                count=count+adder
                adder+=1
        return count