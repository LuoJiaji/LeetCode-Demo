class Solution(object):


    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def check(p):
            flag = ''
            for i in range(3):
                if p[i][0] == p[i][1] == p[i][2] and p[i][0] != ' ':
                    flag = p[i][0]
            for i in range(3):
                if p[0][i] == p[1][i] == p[2][i] and p[0][i] != ' ':
                    flag = p[0][i]
            if p[0][0] == p[1][1] == p[2][2] and p[0][0] != ' ':
                flag = p[0][0]
            if p[2][0] == p[1][1] == p[0][2] and p[2][0] != ' ':
                flag = p[2][0]
            return flag

        p = [[' ']*3 for _ in range(3) ]
        for i,[x,y] in enumerate(moves):
            if i%2 == 0:
                p[x][y] = 'X'
            else:
                p[x][y] = 'O'

            flag = check(p)
            if flag != '':
                if flag ==  'X':
                    return 'A'
                elif flag == 'O':
                    return 'B'
        # print(flag , p,p[0][1] == p[1][1] == p[2][1] and p[0][1]!= ' ')
        for i in p:
            print(i)
            if ' ' in i:
                return "Pending"
        return "Draw"    
        
        

# moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# res = Solution().tictactoe(moves)
# print(res)

# moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# res = Solution().tictactoe(moves)
# print(res)

# moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# res = Solution().tictactoe(moves)
# print(res)

# moves = [[0,0],[1,1]]
# res = Solution().tictactoe(moves)
# print(res)

moves = [[1,0],[0,2],[0,1],[0,0]]
res = Solution().tictactoe(moves)
print(res)

moves = [[1,2],[2,1],[0,0],[0,1],[2,0],[0,2],[2,2],[1,1]]
res = Solution().tictactoe(moves)
print(res)