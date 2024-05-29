# 寫一個程式，輸入整數 k (0 < k ≤ 10)，找出 k 位數中，所有數字均為偶數的完全平方數中最小的一個數。例如當 k = 5，五位數中所有數字均為偶數的完全平方數中最小的數為 26244 (26244 = 1622) 。

# Input
# 輸入第一行為一個整數 n，表示接下來會有 n 組測試資料。

# 接下來有 n 行，每行有一個整數 k，代表數字的位數。

# Output
# 輸出 k 位數中，所有數字均為偶數的完全平方數中最小的一個數，每個測試資料輸出一行。

# Sample Input #1
# 2
# 5
# 2
# Sample Output #1
# 26244
# 64

def is_all_even_digits(num):
	while num > 0:
		digit = num % 10
		if digit % 2 != 0:
			return False
		num //= 10
	return True

def find_min_even_digit_square(k):
	# A k-digit number lies in the range [10^(k-1), 10^k). For example, for k=3, the range is [100, 1000)
	# So in this case, we just have to check from start = 10 (because 10 * 10 = 100), to end = 31 (because 31 * 31 = 961)
	start = int(10**((k-1)/2))  # smallest possible integer square root
	end = int(10**(k/2))        # largest possible integer square root

	for i in range(start, end+1):
		square = i * i
		if is_all_even_digits(square):
			return square
	return -1  # shouldn't happen

def main():
	n = int(input().strip())
	for _ in range(n):
		k = int(input())
		print(find_min_even_digit_square(k))

if __name__ == "__main__":
	main()
