# 在數學上，費波那契數列是以遞迴的方法來定義：
# F(0)=0
# F(1)=1
# F(n) = F(n-1)+ F(n-2), 當n≧2時
# 請定義一個遞迴函式，計算費波那契數列

# Input
# 包含多筆資料，每筆資料包含一個整數n (0<=n<=30)

# Output
# 請針對每筆資料，輸出F(n)的值

# Sample Input #1
# 1
# 2
# 3
# Sample Output #1
# 1
# 1
# 2

import sys

def fibonacci(n):
	if n == 0: return 0
	if n == 1: return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

def main():
	input = sys.stdin.read
	data = map(int, input().strip().split())
	for n in data:
		print(fibonacci(n))

if __name__ == "__main__":
	main()
