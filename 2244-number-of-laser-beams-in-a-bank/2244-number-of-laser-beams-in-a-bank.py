class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=[]
        ans=0
        for i in bank:
            ones=0
            for j in i:
                if j=='1':
                    ones+=1
            if ones>0:
                res.append(ones)
        if len(res)<=1:
            return 0
        for i in range(len(res)-1):
            ans+=res[i]*res[i+1]
        return ans