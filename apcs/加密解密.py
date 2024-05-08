# 很久以前,法國人 Felix 設計了一套加密系統,此系統由四組矩陣組成,首先將欲加密的字串進行反轉(反轉是把字串中的字母出現順序前後對調,例如’bca’變成’acb’)。接下來從前面開始,每次取連續的兩個字母一組 (c1,c2),從矩陣 A 中找到第一個字母 c1 的出現位置(i1, j1),並從矩陣 D 中找到第二個字母 c2 的出現位置(i2, j2)。再將兩個矩陣的位址對應到矩陣 B 的位置(i1, j2)及矩陣 C 的位置(i2, j1),依序得到兩個字母當作密文傳送。接收方依照相同模式,查詢矩陣 B 及矩陣 C,再對應到矩陣 A 及矩陣 D,就可以還原解出原始明文。
# 現在有明文或密文,請透過上述敘述寫出一套加解密程式,並得出加解密後的資料為何。

# Matrix used
# A = D = [
#     ['a', 'b', 'c', 'd', 'e'],
#     ['f', 'g', 'h', 'i', 'j'],
#     ['k', 'l', 'm', 'n', 'o'],
#     ['p', 'r', 's', 't', 'u'],
#     ['v', 'w', 'x', 'y', 'z']
# ]
# B = C = [
#     ['E', 'X', 'A', 'M', 'P'],
#     ['L', 'B', 'C', 'D', 'F'],
#     ['G', 'H', 'I', 'J', 'K'],
#     ['N', 'O', 'R', 'S', 'T'],
#     ['U', 'V', 'W', 'Y', 'Z']
# ]

# Input
# 第一行輸入一個正整數N，表示英文字母字串長度。
# 第二行輸入一個長度N的英文字母字串。已知若是明文輸入，則字串全部都是小寫字母，若是密文輸入，則字串全部都是大寫字母。

# Output
# 請根據測試資料提供給你的明文或密文，輸出一行，顯示其對應密文或明文。

# Sample Input #1
# 12
# happynewyear
# Sample Output #1
# NXMZZXJYNNAL
# Sample Input #2
# 10
# XJTHZHHHAF
# Sample Output #2
# helloworld


A = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'r', 's', 't', 'u'],
    ['v', 'w', 'x', 'y', 'z']
]

B = [
    ['E', 'X', 'A', 'M', 'P'],
    ['L', 'B', 'C', 'D', 'F'],
    ['G', 'H', 'I', 'J', 'K'],
    ['N', 'O', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'Y', 'Z']
]


def reverse_str(s):
	return s[::-1]


def encrypt(txt):
	res = ""
	txt = reverse_str(txt)
	for i in range(0, len(txt), 2):
		c1, c2 = txt[i], txt[i + 1]
		i1, i2, j1, j2 = 0, 0, 0, 0
		for row in range(len(A)):
			for col in range(len(A[row])):
				if A[row][col] == c1:
					i1, j1 = row, col
				if A[row][col] == c2:
					i2, j2 = row, col
		res += B[i1][j2] + B[i2][j1]
	return res

def decrypt(txt):
	res = ""
	for i in range(0, len(txt), 2):
		c1, c2 = txt[i], txt[i + 1]
		i1, i2, j1, j2 = 0, 0, 0, 0
		for row in range(len(B)):
			for col in range(len(B[row])):
				if B[row][col] == c1:
					i1, j2 = row, col
				if B[row][col] == c2:
					i2, j1 = row, col
		res += A[i1][j1] + A[i2][j2]
	return reverse_str(res)

if __name__ == "__main__":
	_ = input() # discard text's length
	txt = input()

	if txt[0].isupper():
		print(decrypt(txt))
	else:
		print(encrypt(txt))
