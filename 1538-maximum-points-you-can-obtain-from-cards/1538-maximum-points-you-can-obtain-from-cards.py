class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score=sum(cardPoints[:k])
        ans=score
        for i in range(k):
            score=score-cardPoints[k-1-i]+cardPoints[len(cardPoints)-1-i]
            ans=max(ans,score)
        return ans