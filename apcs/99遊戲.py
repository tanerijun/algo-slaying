# 在眾多的撲克牌遊戲中，「99」是一種簡單的數學遊戲，利用牌面上的數字依序累加最多到99，讓數字超過99的出牌者即為輸家。當然不只是數字累加這麼簡單，在A到K這13張牌中，有7張特殊牌如下所示
# A為歸零牌(即為累加數字歸零，重新計算)
# 4為迴轉牌(出此牌不用累加數字，出牌順序顛倒，如原本4位玩家ABCD依序出牌，輪到B時出了迴轉牌，本應輪到C出牌則因迴轉牌效果輪A出牌)
# 5為指定牌(出此牌不用累加數字，換下一位出牌者出牌)
# 10為加減10牌(將累加數字加10，但如累加數字加10會超過99則減10)
# J為跳過牌(出此牌不用累加數字，輪下一位出牌者出牌)
# Q為加減20牌(將累加數字加20，但如累加數字加20會超過99則減20)
# K為99牌(出此牌不管累加數字為何，直接累加到99，當累加數字已為99時可以再出K，累加數字保持99)
# 其餘數字的牌按照牌面上的數字做累加。有4位出牌者以英文字母(A、B、C、D)代表出牌者，依序ABCD輪流出牌，當累加數字大於99時出牌者就輸了，如果有人將手上的牌率先出完則為贏家。產生輸家或贏家時遊戲立即結束。

# Input
# 總共有四行輸入，表示4位出牌者依序出牌，每一行用一個英文字母(A、B、C、D)代表出牌者，後面接續13個數字或英文(J、Q、K)，以空白隔開。

# Output
# 共兩行。如有輸家則第一行輸出輸家的代號、第二行輸出輸家手上剩餘牌的張數；如有贏家則第一行輸出贏家的代號、第二行輸出最後累加的數字。

# Sample Input #1
# A 8 9 K 7 5 J Q 2 A 10 4 J 5
# B 2 3 J 5 7 4 4 10 7 9 8 J A
# C 7 3 4 A 9 10 9 6 8 K 10 Q 2
# D 6 3 Q 9 8 3 5 K Q K 2 A 10
#
# Sample Output #1
# A
# 9

def play_99_game():
	players = {}
	for i in range(4):
		player_input = input().split()
		player_name = player_input[0]
		player_cards = player_input[1:]
		players[player_name] = player_cards

	player_order = list(players.keys())
	curr_player_idx = 0
	total = 0
	dir = 1

	while True:
		curr_player = player_order[curr_player_idx]
		card = players[curr_player][0]
		players[curr_player] = players[curr_player][1:] # remove the first card

		if card == 'A':
			total = 0
		elif card == '4':
			dir *= -1
		elif card == '5' or card == 'J':
			pass
		elif card == '10':
			total += 10 if (total + 10 <= 99) else -10
		elif card == 'Q':
			total += 20 if (total + 20 <= 99) else -20
		elif card == 'K':
			total = 99
		else:
			total += int(card)

		# Found a loser
		if total > 99:
			print(curr_player)
			print(len(players[curr_player]))
			break

		# Found a winner
		if len(players[curr_player]) == 0:
			print(curr_player)
			print(total)
			break

		curr_player_idx = (curr_player_idx + dir + 4) % len(player_order)

if __name__ == "__main__":
	play_99_game()
