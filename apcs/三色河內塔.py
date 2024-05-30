# 下圖為河內塔問題(Towers of Hanoi)的一種，共有A、B、C三個柱子，一開始A柱子可以放個數為3倍數的套環，都是花白灰相間的三種不同顏色套環，每種大小的套環都有三個，花色在上，白色在中，灰色在下。套環依序由上到下的編號分別為1~N，假設每次的移動都只能從柱子的頂端移動一個套環，搬到其他柱子放，而且編號較大的套環永遠都不能放在較小套環的上方。最後要將所有花套環移動到A，白套環移動到B，以及所有灰套環移動到C。請寫出一個程式，輸入套環總數(為 3的倍數，包含花白灰三種套環)，計算並輸出所有套環的最佳移動順序(移動次數最少)及其移動次數。

# Input
# 由鍵盤輸入一個整數n，n為3的倍數。

# Output
# 請在螢幕中依序輸出每個移動，包括套環(ring)編號(1~n)，從一個柱名稱移動(=>)到另一個柱名稱(A、B、或C)。最後一列輸出總移動次數。

# Sample Input #1
# 3
# Sample Output #1
# ring 1 : A => C
# ring 2 : A => B
# ring 1 : C => B
# ring 3 : A => C
# ring 1 : B => A
# 共需5個移動

import sys
import io

# Set default encoding to UTF-8 because test env is in ASCII
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

move_count = 0

def hanoi(n, start, target):
	global move_count
	if n == 0: return
	temp = 3 - start - target
	hanoi(n - 1, start, temp) # move discs above to temp
	print(f"ring {n} : {chr(ord('A') + start)} => {chr(ord('A') + target)}")
	move_count += 1
	hanoi(n - 1, temp, target)

def main():
	global move_count

	# Tower 1 to 3 and color 1 to 3 are represented using 0, 1, 2
	n = int(input())
	start = 0

	while(n):
		n = n - 1
		if n < 0:
			break

		target = n % 3
		temp = 3 - start - target

		if (start == target):
			continue # if the color is already at the position, skip

		# Move discs above to temp
		hanoi(n, start, temp)

		# Output
		print(f"ring {n + 1} : {chr(ord('A') + start)} => {chr(ord('A') + target)}")

		move_count += 1

		# Since we moved all the discs to temp earlier
		start = temp

	print(f"共需{move_count}個移動")

if __name__ == "__main__":
	main()
