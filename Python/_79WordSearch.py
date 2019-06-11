from collections import Counter
from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        count = Counter(x for rows in board for x in rows)
        for c, cnt in Counter(word).items():
            if cnt > count[c]:
                return False

        r = len(board)
        c = len(board[0])
        length = len(word)

        def go(x, y, index):
            if index == length:
                return True

            w = word[index]

            prev = board[x][y]
            board[x][y] = ''

            if x > 0 and board[x - 1][y] == w and go(x - 1, y, index + 1):
                return True
            if x + 1 < r and board[x + 1][y] == w and go(x + 1, y, index + 1):
                return True
            if y > 0 and board[x][y - 1] == w and go(x, y - 1, index + 1):
                return True
            if y + 1 < c and board[x][y + 1] == w and go(x, y + 1, index + 1):
                return True

            board[x][y] = prev
            return False

        candidates = ((x, y) for x in range(r) for y in range(c) if board[x][y] == word[0])
        return any(go(x, y, 1) for x, y in candidates)


if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCED'
    s = Solution()
    print(s.exist(board, word))