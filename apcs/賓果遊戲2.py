# 賓果遊戲是一種兩人（或多人）進行的遊戲，遊戲盤大小通常為 5 x 5，每位玩家會在遊戲盤中填入 1, 2, …, 25 這25 個號碼，填入的位置由玩家自行決定。遊戲開始後，每位玩家輪流叫號，每叫一個號碼，所有玩家就會在自己的遊戲盤上標記該號碼。若同一列、同一行或對角線上的五個號碼均被標記，即可得到一分，先得到五分的玩家為勝利者。

# 瑞奇最近才接觸到這個遊戲，他希望有一個程式能幫助他決定每次叫號時該選擇哪個號
# 碼。他的策略如下：
# (1) 從未標記的號碼中選擇標記該號碼後，該盤面的分數最高者；
# (2) 如果有多於一個可選擇的號碼，選擇數值最小的。

# 盤面1
# 01* 09 23 17 18
# 10 24* 08* 16* 02*
# 11* 13 03 07 19*
# 12* 04 15 06 20*
# 25* 14 05 22 21*

# 盤面2
# 01* 09 23 17* 18
# 10 24* 08* 16* 02*
# 11* 13 03* 07* 19
# 12* 04 15 06 20
# 25* 14 05 22* 21*

# 盤面1 中，共有14 個號碼可選擇，其中選擇10 可讓盤面分數為2，選擇18 可讓盤面分數為1，而其它選擇則都得不到分數，因此瑞奇的策略會選擇10。盤面2 中，選擇6 和10 都可得到2 分，其它選擇都得不到分數，瑞奇會選擇較小的值6。

# 請你撰寫一個程式，讀入一個起始盤面和玩家叫過的號碼，輸出瑞奇應該選擇的號碼。

# Input
# 每一筆測試資料會先有五列，每一列有五個數字，以空白隔開。已知這25 個數字為由1到25 的相異數字。接著有N 列 (1 <= N <= 24)，每列僅有一個數字，代表玩家叫過的號碼。最後以-1 表示結束。

# Output
# 根據瑞奇的策略，輸出瑞奇應該選擇的號碼。

# Sample Input #1
# 1 9 23 17 18
# 10 24 8 16 2
# 11 13 3 7 19
# 12 4 15 6 20
# 25 14 5 22 21
# 1
# 17
# 24
# 8
# 16
# 2
# 11
# 3
# 7
# 12
# 25
# 22
# 21
# -1
# Sample Output #1
# 6

# -------------------------INITIAL SOLUTION (FAIL ON SOME TEST CASES)-----------------------
# BOARD_SIZE = 5

# def best_bingo_move():
# 	# Create and fill board
# 	board = []
# 	for _ in range(BOARD_SIZE):
# 		board.append(list(map(int, input().split())))

# 	# Keep track of numbers of checked tiles
# 	count_row = [0 for _ in range(BOARD_SIZE)]
# 	count_col = [0 for _ in range(BOARD_SIZE)]
# 	count_diag_tl_br = 0
# 	count_diag_tr_bl = 0

# 	# Check board
# 	while True:
# 		number_to_cross = int(input())
# 		if number_to_cross == -1: # -1 indicates end of inputs
# 			break

# 		for i in range(BOARD_SIZE):
# 			for j in range(BOARD_SIZE):
# 				if board[i][j] == number_to_cross:
# 					count_row[i] += 1
# 					count_col[j] += 1
# 					if i == j: # the number is in the diagonal from tl to br
# 						count_diag_tl_br += 1
# 					if i + j == 4: # the number is in the diagonal from tr to bl
# 						count_diag_tr_bl += 1
# 					# Cross the number
# 					board[i][j] = 0

# 	# Find answer
# 	max_score, ans = 0, 0
# 	for i in range(BOARD_SIZE):
# 		for j in range(BOARD_SIZE):
# 			if board[i][j] == 0:
# 				continue # we can't choose crossed number

# 			# The value is 1 for each True condition
# 			score = (
# 				int(count_row[i] == 4) +
# 				int(count_col[j] == 4) +
# 				int((count_diag_tl_br == 4 and i == j)) +
# 				int((count_diag_tr_bl == 4 and i + j == 4))
# 			)

# 			if score > max_score:
# 				max_score = score
# 				ans = board[i][j]
# 			elif score == max_score: # in case where we have multiple answers with the same score, we choose the smaller number
# 				ans = min(ans, board[i][j])

# 	print(ans)

# if __name__ == "__main__":
# 	best_bingo_move()
# ---------------------------------------------------------------------------------------
#
# The cpp solution converted to py
#
BOARD_SIZE = 5

def best_bingo_move():
    # Initialize position tracking arrays
    pr = [-1] * 26  # Position row of number
    pc = [-1] * 26  # Position column of number

    # Read the board and fill pr, pc
    for i in range(BOARD_SIZE):
        row = list(map(int, input().split()))
        for j in range(BOARD_SIZE):
            num = row[j]
            pr[num] = i
            pc[num] = j

    # Initialize row, column and diagonal counters
    cr = [0] * BOARD_SIZE
    cc = [0] * BOARD_SIZE
    c1 = c2 = 0

    # Read the called numbers
    while True:
        n = int(input())
        if n == -1:
            break
        if pr[n] != -1:  # If the number has a valid position
            cr[pr[n]] += 1
            cc[pc[n]] += 1
            if pr[n] == pc[n]:
                c1 += 1
            if pr[n] + pc[n] == BOARD_SIZE - 1:
                c2 += 1
            pr[n] = pc[n] = -1  # Mark the number as called

    # Find the best move
    mxc = -1
    mxn = -1
    for n in range(1, 26):
        if pr[n] == -1:  # Skip already called numbers
            continue
        r, c = pr[n], pc[n]
        score = (cr[r] == 4) + (cc[c] == 4) + (r == c and c1 == 4) + (r + c == BOARD_SIZE - 1 and c2 == 4)
        if score > mxc or (score == mxc and (mxn == -1 or n < mxn)):
            mxc = score
            mxn = n

    print(mxn)

if __name__ == "__main__":
    best_bingo_move()
