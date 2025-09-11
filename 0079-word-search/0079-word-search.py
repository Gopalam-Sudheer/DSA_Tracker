class Solution:
    def isValid(self,i,j,board):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return False
        return True
    def helper(self,board,i,j,word,ind):
        if ind==len(word):
            return True
        if not self.isValid(i,j,board) or board[i][j]=="" or board[i][j]!=word[ind]:
            return False
        temp=board[i][j]
        board[i][j]=''
        ans=(self.helper(board,i-1,j,word,ind+1) or self.helper(board,i,j-1,word,ind+1) or self.helper(board,i+1,j,word,ind+1) or self.helper(board,i,j+1,word,ind+1))
        board[i][j]=temp
        return ans
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.helper(board,i,j,word,0):
                        return True
        return False