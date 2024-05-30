# 後序運算式(postfix)有別於我們習慣的中序算式寫法(infix)，是把運算子寫在運算元之後，雖然對人類而言可讀性很低，可是對電腦來說卻是很方便的運算式。運算式用後序表示法的好處是不用考慮中序式的先乘除後加減問題還能夠免除所有的括號。
# 比如我們所熟習的1 + 2，其實就是中序運算式，同一個式子改成後序寫法即為1 2 +
# 現在給你一個後序運算式，請求出這個式子的計算結果

# Input
# 有多筆測資，每筆測資包含一個後序運算式，這個運算式中包含數個運算子及運算元

# 運算子共有五種：  + - * / %
# 運算元則為0~9 之間的整數
# Output
# 輸出該後序運算式運算結果

# Sample Input #1
# 35+
# 63/14-*3+8-
# Sample Output #1
# 8
# -11

import sys

def calculate_postfix_notation(s):
	stack = []
	for ch in s:
		stack.append(ch)

		if not stack[-1].isdigit():
			operator = stack.pop()
			b, a = int(stack.pop()), int(stack.pop())

			if operator == "+":
				stack.append(a + b)
			elif operator == "-":
				stack.append(a - b)
			elif operator == "*":
				stack.append(a * b)
			elif operator == "/":
				stack.append(a // b)
			elif operator == "%":
				stack.append(a % b)
			else:
				raise ValueError("Unexpected value")

	return stack.pop()

if __name__ == "__main__":
	input = sys.stdin.read
	data = input().strip().split()
	for s in data:
		print(calculate_postfix_notation(s))
