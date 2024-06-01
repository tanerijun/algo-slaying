# 某電腦將算術運算的格式安排為 (第一運算元,第二運算元,運算子)，其中可使用的運算子共有四種分別為： 加 (+)、減 (-)、乘(*)、除 (/)；所有運算元必須是0或正整數，且若運算子為除(/)，則第二運算元不可為0。
# 寫一個程式，能辨識上述的格式並輸出正確的運算結果(本題輸出不需考慮浮點數，假設除法運算皆可剛好整除)。

# Input
# 輸入第一行為一個整數 n，表示接下來會有n組測試資料。

# 接下來有 n 行，每行是由多個運算子及運算元組成的算術運算式，運算子及運算元間皆以一個半形逗號區隔。

# Output
# 輸出每個測試資料的運算結果，每個測試資料輸出一行，若格式錯誤或是不合法的運算元則輸出-1。

# Sample Input #1
# 2
# ((3,5,*),((2,4,*),6,-),+)
# ((3,0,*),((2,4.5,*),6,-),+)

# Sample Output #1
# 17
# -1

# Sample Input #2
# 2
# (8,((1,1,+),(2,2,*),*),/)
# (5,(1,1,+),(1,1,-),/)
# Sample Output #2
# 1
# -1


# def evaluate_expression(exp, idx):
#     if idx >= len(exp):
#         raise ValueError("Unexpected end of expression")

#     token = exp[idx]
#     res = 0

#     if token.isdigit():
#         res = token
#     elif token == "(":
#         a, idx = evaluate_expression(exp, idx + 1)
#         if idx >= len(exp) or exp[idx] != ",":
#             raise ValueError("Comma expected")
#         b, idx = evaluate_expression(exp, idx + 1)
#         if idx >= len(exp) or exp[idx] != ",":
#             raise ValueError("Comma expected")

#         operator = exp[idx + 1]
#         if operator == "+":
#             res = a + b
#         elif operator == "-":
#             res = a - b
#         elif operator == "*":
#             res = a * b
#         elif operator == "/":
#             if b == 0:
#                 raise ValueError("Division by 0")
#             res = a / b
#         else:
#             raise ValueError("Operator expected")

#         idx += 2  # move past the comma and the operator
#         if idx >= len(exp) or exp[idx] != ")":
#             raise ValueError("Right parentheses expected")
#     else:
#         raise ValueError("Open parentheses or number expected")

#     return int(res), idx + 1


# def main():
#     n = int(input())
#     expressions = []
#     for _ in range(n):
#         expressions.append(input())

#     res = []
#     for expression in expressions:
#         try:
#             result, idx = evaluate_expression(expression, 0)
#             if idx != len(expression):  # Ensure the entire expression is consumed
#                 res.append(-1)
#             else:
#                 res.append(result)
#         except ValueError:
#             res.append(-1)

#     for r in res:
#         print(r)


# if __name__ == "__main__":
#     main()


def evaluate_expression(exp, idx):
    if idx >= len(exp):
        raise ValueError("Unexpected end of expression")

    token = exp[idx]
    if token.isdigit():
        num = ""
        while idx < len(exp) and exp[idx].isdigit():
            num += exp[idx]
            idx += 1
        return int(num), idx
    elif token == "(":
        a, idx = evaluate_expression(exp, idx + 1)
        if idx >= len(exp) or exp[idx] != ",":
            raise ValueError("Comma expected after first operand")
        b, idx = evaluate_expression(exp, idx + 1)
        if idx >= len(exp) or exp[idx] != ",":
            raise ValueError("Comma expected after second operand")

        operator = exp[idx + 1]
        res = 0
        if operator == "+":
            res = a + b
        elif operator == "-":
            res = a - b
        elif operator == "*":
            res = a * b
        elif operator == "/":
            if b == 0:
                raise ValueError("Division by 0")
            res = a // b
        else:
            raise ValueError("Operator expected")

        idx += 2  # Move past the operator and the comma
        if idx >= len(exp) or exp[idx] != ")":
            raise ValueError("Right parentheses expected")
        return res, idx + 1
    else:
        raise ValueError("Open parentheses or number expected")


def main():
    n = int(input())
    expressions = []
    for _ in range(n):
        expressions.append(input())

    res = []
    for expression in expressions:
        try:
            result, idx = evaluate_expression(expression, 0)
            if idx != len(expression):  # Ensure the entire expression is consumed
                res.append(-1)
            else:
                res.append(result)
        except ValueError:
            res.append(-1)

    for r in res:
        print(r)


if __name__ == "__main__":
    main()
