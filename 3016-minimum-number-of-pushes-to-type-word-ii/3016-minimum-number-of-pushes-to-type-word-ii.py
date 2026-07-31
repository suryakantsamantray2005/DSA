class Solution:
    def minimumPushes(self, word):
        freq={}
        for i in word:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        count=0
        adder=1
        a=sorted(freq.values(),reverse=True)
        iterative_num=0
        for j in a:
            iterative_num+=1
            if iterative_num%8!=0:
                count=count+adder*j
            else:
                count=count+adder*j
                adder+=1
        return count