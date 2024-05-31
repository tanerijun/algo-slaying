# 小明要解決一大堆的數字加減乘除運算，好在小明有一個好用的電腦程式，只要輸入問題，程式即輸出答案。例如小明輸入 3×((3+5)×4-(2×2))，程式輸出84。但是，這個程式只能用來計算「正確」的輸入，也就是式子中的括號必須成對而且先出現左括號再出現右括號。請你寫一個程式判斷一個式子中的括號是否正確，若正確的話，請輸出式子中有幾對括號，若錯誤的話，請輸出0。

# Input
# 每組輸入只有一列，代表一個式子。為了簡化問題，式子中的數字與加、減、乘、除等運算元皆已移除，只留下括號，中間沒有空白。每筆輸入的括號符號數最多20個。

# Output
# 根據每列資料，輸出式子中的括號是否正確（成對且先出現左括號再出現右括號）。若正確的話，請輸出式子中有幾對括號，若不正確請輸出0。

# Sample Input #1
# (()())
# Sample Output #1
# 3
# Sample Input #2
# ((()())
# Sample Output #2
# 0

def count_bracket_pair(s):
	stack = []
	count = 0
	for ch in s:
		if ch == "(":
			stack.append(")")
		if ch == ")":
			if len(stack) == 0:
				return 0
			stack.pop()
			count += 1

	if len(stack) > 0:
		return 0

	return count

def main():
	s = input()
	res = count_bracket_pair(s)
	print(res)

if __name__ == "__main__":
	main()
