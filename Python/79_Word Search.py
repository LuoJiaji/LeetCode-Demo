
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        alpha = []
        flag = [[0 for _ in board[0]] for _ in board]
        print(flag)
        x = 0 
        y = 0

        flag[0][0] = 1
        print(flag)
        state, flag = self.exist_check(board, flag, word[1])
        print(state, flag)
        state, flag = self.exist_check(board, flag, word[2])
        print(state, flag)
        state, flag = self.exist_check(board, flag, word[3])
        print(state, flag)
        state, flag = self.exist_check(board, flag, word[4])
        print(state, flag)
        state, flag = self.exist_check(board, flag, word[5])
        print(state, flag)
    def exist_check(self, board, flag, word):
        x = 0
        y = 0
        for i in range(len(flag[0])):
            for j in range(len(flag)):
                # print('i',i,'j',j)
                if flag[j][i] == 1:
                    x = max(i-1,0)
                    y = j
                    if board[y][x] == word and flag[y][x] != 1:
                        flag[y][x] = 1
                        # print('left',x,y)
                        return True, flag
                    x = min(i+1,len(flag[0])-1)
                    y = j
                    if board[y][x] == word and flag[y][x] != 1:
                        flag[y][x] = 1
                        # print('right',x,y)
                        return True, flag                    
                    x = i
                    y = max(j-1,0)
                    if board[y][x] == word and flag[y][x] != 1:
                        flag[y][x] = 1
                        # print('up',x,y)
                        return True, flag
                    x = i
                    y = min(j+1, len(flag)-1)
                    # print(x,y)
                    if board[y][x] == word and flag[y][x] != 1:
                        flag[y][x] = 1
                        # print('down',x,y)
                        return True, flag
        return False, flag





data = [['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]
word = 'ABCCED'
result = Solution().exist(data, word)
print(result)

# word = 'SEE'
# result = Solution().exist(data, word)
# print(result)

# word = 'ABCB'
# result = Solution().exist(data, word)
# print(result)
