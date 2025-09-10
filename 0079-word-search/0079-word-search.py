class Solution:
    def fun(self,board,word,index,i,j):
        if index==len(word):
            return True
        if board[i][j]=="" or board[i][j]!=word[index]:
            return False
        temp=board[i][j]
        board[i][j]=""
        ans=False
        if i-1>=0:
            ans= ans or self.fun(board,word,index+1,i-1,j)
        if i+1<=len(board)-1:
            ans= ans or self.fun(board,word,index+1,i+1,j)
        if j-1>=0:
            ans= ans or self.fun(board,word,index+1,i,j-1)
        if j+1<=len(board[0])-1:
            ans= ans or self.fun(board,word,index+1,i,j+1)
        board[i][j]=temp
        return ans
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if len(word)==1:
                        return True
                    if self.fun(board,word,0,i,j):
                        return True
        return False