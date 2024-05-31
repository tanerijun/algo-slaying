# 醜數是指不能被 2, 3, 5 以外的其他質數整除的數字。醜數由小到大為：
# 1, 2, 3, 4, 5, 6, 8, 9, 10, ...

# Input
# 一個整數 n (n<=1000)

# Output
# 第 n 個醜數

# Sample Input #1
# 1000
# Sample Output #1
# 51200000

def get_nth_ugly_number(n):
	ugly = [0] * n # store ugly number

	# 1 is the first ugly number
	ugly[0] = 1

	# i2, i3, i5 indicates 2, 3, 5 respectively
	i2 = i3 = i5 = 0

	# Initial values
	next_multiple_of_2 = 2
	next_multiple_of_3 = 3
	next_multiple_of_5 = 5

	for i in range(1, n):
		# The next ugly is the minimum of the multiples
		ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

		# Increment the value of index accordingly
		if ugly[i] == next_multiple_of_2:
			i2 += 1
			next_multiple_of_2 = ugly[i2] * 2
		if ugly[i] == next_multiple_of_3:
			i3 += 1
			next_multiple_of_3 = ugly[i3] * 3
		if ugly[i] == next_multiple_of_5:
			i5 += 1
			next_multiple_of_5 = ugly[i5] * 5

	return ugly[-1]

def main():
	n = int(input())
	res = get_nth_ugly_number(n)
	print(res)

if __name__ == "__main__":
	main()
