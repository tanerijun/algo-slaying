# 象棋中馬走動的方法是直橫並行，即先橫向或直向走一格，然後再直向或橫向走兩格。如下圖範例，位於棋盤中間的馬，走一步時可以到達的位置(8種)
# 給定棋盤的大小 3xn，寬為3列、長為n行，假設馬從棋盤的左上角出發，是否可走到棋盤上的任意一格? n=3時3x3 方格中走訪順序如下表，棋盤內的數字代表棋子馬走的順序，中間方格無法到達，故無解。
# 1 6 3
# 4   8
# 7 2 5
# n=4 時3x4 方格中走訪順序如下表，可以走完。
# 1 4 7 10
# 8 11 2 5
# 3 6 9 12
# 其走法可能不只一種，另一個走法如下表
# 1 4 7 10
# 12 9 2 5
# 3 6 11 8
#
# 當有多個答案時，請先將這3xn的格子所代表的解排成一維陣列後，由左至右依字典排序(lexicographical order)比較，再挑選字典排序最小的一個方法輸出。所謂字典排序法，對於兩個一維陣列 1 2 4 5 3和1 2 5 4 3，先由左邊第一位開始比較，左邊第一位都是1，不能分辨大小；則再比左邊第二位，都是2；再比左邊第三位，後者是5較大，所以後者排列較大，其後的幾位也不用再比較，亦即1 2 4 5 3小於1 2 5 4 3。
# 於n=4 馬步走法的輸出兩種方法中，左邊第五位資料比較時第一個方法為8比第二個方法的12小，故輸出第一個。
# 1 4 7 10 8 11 2 5 3 6 9 12
# 或
# 1 4 7 10 12 9 2 5 3 6 11 8
#
# Input
# 一個大於或等於 3 且小於或等於 10 的正整數 (3 ≤ n ≤ 10)
# Output
# 若無法走訪3xn棋盤上的任一格則輸出0，若可以走訪3xn棋盤的任一格，則輸出找到所有可能的走法中字典排序 (lexicographical order) 最小的一個方法。將每一格被走訪的順序，共有3xn個數字輸出於同一列，數字間以一個空格分開。
# Sample Input #1
# 3
# Sample Output #1
# 0
# Sample Input #2
# 4
# Sample Output #2
# 1 4 7 10 8 11 2 5 3 6 9 12
# Sample Input #3
# 7
# Sample Output #3
# 1 4 7 18 15 10 13 6 19 2 9 12 21 16 3 8 5 20 17 14 11


def main():
    n = int(input())

    # All the possible moves the knight can make
    # Ex: (move_x[0], move_y[0]): knight move one square up and two square right
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board = [[0 for _ in range(n)] for _ in range(3)]
    board[0][0] = 1  # Knight start from (0, 0)

    result = []  # contains all valid solution

    # Check if index is correct and the square is not yet visited
    def is_valid_move(row, col):
        return 0 <= row < 3 and 0 <= col < n and board[row][col] == 0

    def knight_tour(row, col, move_i):
        # Filled all squares
        if move_i == 3 * n:
            # Add board state as 1D array
            result.append([board[i][j] for i in range(3) for j in range(n)])
            return

        for i in range(8):  # possible moves for the Knight = 8
            next_row = row + move_x[i]
            next_col = col + move_y[i]
            if is_valid_move(next_row, next_col):
                board[next_row][next_col] = move_i + 1
                knight_tour(next_row, next_col, move_i + 1)
                board[next_row][next_col] = 0  # backtrack

    knight_tour(0, 0, 1)

    if not result:
        print(0)
    else:
        lexicographically_smallest = min(result)
        print(" ".join(map(str, lexicographically_smallest)))


if __name__ == "__main__":
    main()
