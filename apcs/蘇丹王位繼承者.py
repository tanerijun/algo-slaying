# 努比亞的蘇丹沒有子女，所以他要從一些有資格的繼承者中挑選一個出來繼承王位。他希望這個繼承者是夠聰明的，所以他決定用一個遊戲來測試這些人。
# 他準備了一個西洋棋盤，上面的每個格子中均有一個1到99的數字。他又準備了8個皇后棋子。每位參加遊戲的人必須將8個皇后放置到棋盤中，且各皇后 彼此不可互相攻擊。可以想像，這樣有不只一種的放置方式。而蘇丹要挑選的繼承者就是那位可以放置8個皇后，並且放置皇后的8個位置中的數的和為最大的那一 個人。
# 你的任務就是讀入棋盤上的數，幫蘇丹算出可以放置8個皇后的最大的和是多少。

# Input
# 輸入的第一列有一個整數k(k≦20)，代表以下有幾組測試資料(就是幾個棋盤)
# 每組測試資料有8列，每列有8個整數(介於0到99)。代表棋盤中格子的資料

# Output
# 對每一組測試資料，輸出可以放置8個皇后的最大的和是多少。輸出長度為5，靠右對齊

# Sample Input #1
# 2
#  1  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32
# 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48
# 48 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64
# 99 92 53 74 69 76 87 98
#  9 12 11 12 19 14 15 16
# 17 14 19 20 29 22 23 24
# 25 26 57 28 29 30 31 32
# 33 34 36 76 39 58 39 40
#  1 42 43 44 85 46 47 48
# 58 60 71 82 53 34 55 56
# 57 58 39 90 61 32 23 44

# Sample Output #1
#   260
#   429


# Check if it's safe to place a queen at (row, col) on board.
# We only need to check to the left of the current position because we're placing queens from left to right.
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def backtrack_queens(board, col, values, current_sum):
    if col >= 8:
        return current_sum

    max_sum = 0
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            sum = backtrack_queens(board, col + 1, values, current_sum + values[i][col])
            max_sum = max(max_sum, sum)
            board[i][col] = 0

    return max_sum


def solve_n_queens(values):
    board = [[0 for _ in range(8)] for _ in range(8)]
    return backtrack_queens(board, 0, values, 0)


def main():
    k = int(input().strip())
    results = []

    for _ in range(k):
        values = []
        for _ in range(8):
            row = list(map(int, input().strip().split()))
            values.append(row)

        max_sum = solve_n_queens(values)
        results.append(max_sum)

    for result in results:
        print(f"{result:>5}")  # width 5, align right


if __name__ == "__main__":
    main()
