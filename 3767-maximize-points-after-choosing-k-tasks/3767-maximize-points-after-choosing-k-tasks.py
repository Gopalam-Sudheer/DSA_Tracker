class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        s=0
        game=[]
        for i in range(len(technique1)):
            s+=technique2[i]
            game.append(technique1[i]-technique2[i])
        game.sort(reverse=True)
        for i in range(k):
            s+=game[i]
        for i in range(k,len(technique1)):
            if game[i]>0:
                s+=game[i]
            else:
                break
        return s

        