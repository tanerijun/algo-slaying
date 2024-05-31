# 一般使用的數學運算式稱為中置式(infix)，是將運算子(operator)置於兩個運算元(operand)中間，以A*(B+C)－D*E+F為例，A、B、C、D、E、F為運算元，*、+、－為運算子，運算的優先順序為括號>乘除>加減，運算子優先順序相同時則由左至右依序運算。另有一種後置式(postfix) 是將運算子(operator)置於兩個運算元(operand)的後面，例如B+C的後置式為BC+。將中置式依照運算的優先順序轉為後置式後，可以去除掉括號，例如A*(B+C)－D*E+F轉為後置式是ABC+*DE*－F+。

# Input
# 由鍵盤輸入一個中置式的運算式，運算元用A~Z等26個單一字母表示，運算子只包含+、－、*、/ 等4個運算子，運算式中可以有任意多個括號 ‘(‘ 和 ‘)’。

# Output
# 請在螢幕中輸出中置式轉換成的後置式。

# Sample Input #1
# (A+B*(C-D)+E)*((F+G)/(H*I)+J)
# Sample Output #1
# ABCD-*+E+FG+HI*/J+*

# Solution using Shunting-yard algorithm by Edsger Dijkstra
# Read more: https://brilliant.org/wiki/shunting-yard-algorithm/

operators = {
		"+": 0,
		"-": 0,
		"*": 1,
		"/": 1
	}

def peek(stack):
	return stack[-1]

def higher_precedence(op1, op2):
	return operators[op1] > operators[op2]

def equal_precedence(op1, op2):
	return operators[op1] == operators[op2]

def infix_to_postfix(s):
	stack = []
	output = []
	for ch in s:
		if ch in operators:
			# put operators with higher or equal precedence in output
			while (stack and peek(stack) != "(" and (higher_precedence(peek(stack), ch) or equal_precedence(peek(stack), ch))):
				output.append(stack.pop())
			stack.append(ch)
		elif ch == "(":
			stack.append(ch)
		elif ch == ")":
			while peek(stack) != "(":
				output.append(stack.pop())
			stack.pop() # discard the "("
		else:
			output.append(ch)

	while stack:
		output.append(stack.pop())

	return "".join(output)

def main():
	infix = input()
	postfix = infix_to_postfix(infix)
	print(postfix)

if __name__ == "__main__":
	main()
