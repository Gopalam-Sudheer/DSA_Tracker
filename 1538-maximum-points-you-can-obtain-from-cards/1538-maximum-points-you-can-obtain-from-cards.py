class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score=0
        ans=0
        for i in range(k):
            score+=cardPoints[i]
        ans=score
        for i in range(k-1,-1,-1):
            score-=cardPoints[i]
            score+=cardPoints[len(cardPoints)-(k-i)]
            ans=max(ans,score)
        return ans