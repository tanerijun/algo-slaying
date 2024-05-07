# 賓果遊戲是可以在宴會多人一起玩的遊戲。我們以3x3賓果遊戲為例來說明：
# 有A,B,C三個人一起玩賓果遊戲，他們拿到的盤面如下：
# 以A的盤面為例，可以改用以下字串表示：A 1 6 7 4 2 8 9 5 3
# 每回合由主持人抽出一個號碼，依據抽出的號碼玩家在自己的盤面上連成直線者獲勝(包括橫線、直線、斜線)，並喊出賓果。
# 例如主持人依序抽出號碼為：2, 3, 6, 7, 1, 4, 8, 9, 5，在第四回合，抽出 7 號時 B 與 C 同時賓果。
# 聰明的你，請幫忙設計一個4x4賓果遊戲程式。

# Input
# 第1行包含一個英文字母 N 與一個數字，代表玩家人數(玩家人數 <= 20)
# 第2至N+1行，每行代表一位玩家的盤面，第一個字母為玩家姓名代碼(A,B,C...)，接著有16個數值，以空格隔開
# 第N+2行，為主持人抽出的號碼序列，包含一個英文字母P，接著有16個數值，以空格隔開。

# Output
# 印出抽出的號碼與賓果者

# Sample Input #1
# N 3
# A 10 1 2 9 5 4 11 3 13 12 6 14 8 7 15 16
# B 3 13 12 6 9 5 4 11 14 8 16 7 15 10 1 2
# C 2 12 6 9 5 16 4 11 14 8 3 13 7 15 10 1
# P 4 1 2 3 13 7 15 10 12 16 6 9 5 11 14 8
# Sample Output #1
# 4 1 2 3 13 7 15 10 B C

SIZE = 4


def build_board(flat_board):
    board = []
    for i in range(0, len(flat_board), SIZE):
        board.append(flat_board[i : i + SIZE])
    return board


def update_board(board, n):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == n:
                board[i][j] = 0  # mark it
                return


def is_bingo(board):
    # Columns
    for i in range(SIZE):
        marked = 0
        for j in range(SIZE):
            if board[i][j] == 0:
                marked += 1
            else:
                continue
        if marked == SIZE:
            return True

    # Rows
    for i in range(SIZE):
        marked = 0
        for j in range(SIZE):
            if board[j][i] == 0:
                marked += 1
            else:
                continue
        if marked == SIZE:
            return True

    # Diagonal (TL - BR)
    marked = 0
    for i in range(SIZE):
        if board[i][i] == 0:
            marked += 1
        else:
            break
    if marked == SIZE:
        return True

    # Diagonal (TR - BL)
    marked = 0
    for i in range(SIZE - 1, -1, -1):
        if board[SIZE - 1 - i][i] == 0:
            marked += 1
        else:
            break
    if marked == SIZE:
        return True

    return False


def bingo_game():
    players_count = int(input().split(" ")[1])
    players = {}
    for _ in range(players_count):
        data = input().split(" ")
        player_id, player_board = data[0], build_board(list(map(int, data[1:])))
        players[player_id] = player_board

    nums = list(map(int, input().split(" ")[1:]))
    for num in nums:
        print(num, end=" ")

        winners = []
        for player_id, player_board in players.items():
            update_board(player_board, num)
            if is_bingo(player_board):
                winners.append(player_id)

        if len(winners) > 0:
            print(" ".join(winners))
            return


if __name__ == "__main__":
    bingo_game()
