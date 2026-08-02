class Solution:
    def stoneGame(self, piles):
        left=0
        right=len(piles)-1
        alice=0
        bob=0
        while left<right:
            if piles[left+1]>piles[left] and piles[left+1]>piles[right]:
                alice=alice+piles[right]
                bob=bob+piles[left]
                left+=1
                right-=1
            elif piles[right-1]>piles[left] and piles[right-1]>piles[right]:
                alice=alice+piles[left]
                bob=bob+piles[right]
                left+=1
                right-=1
            elif piles[left]>piles[right]:
                alice=alice+piles[left]
                bob=bob+piles[right]
                left+=1
                right-=1
            else:
                alice=alice+piles[right]
                bob=bob+piles[left]
                left+=1
                right-=1
        if alice>bob:
            return True
        else:
            return False