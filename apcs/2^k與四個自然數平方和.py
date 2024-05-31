# 請寫一程式找出將指數2k表示成四個正整數的平方和的所有表示法。例如當k=2時，可以表示為22=12+12+12+12。這些正整數請以由小到大的順序列出，數字與數字中間以一個空格隔開；若無此種表示法，則輸出0。

# Input
# 輸入為一個正整數k，表示這一筆測資需計算 2k  的表示法。

# Output
# 請輸出將指數2k表示成四個自然數的平方和的所有表示法，四個正整數請以由小到大的順序列出，數字間以一個空白字元區隔；若有多個可能請依照字典順序全部輸出；若沒有合法組合，則輸出0。
# 字典順序：從第一個字元開始進行比較，值小的先輸出，若第一個字元的值相當，則繼續比較下一個字元。

# Sample Input #1
# 2

# Sample Output #1
# 1 1 1 1
# Sample Input #2
# 3
# Sample Output #2
# 0


# def find_four_squares(k):
#     target = 2 ** k
#     solutions = []

#     # We only need to check up to the square root of the target value
#     max_limit = int(target**0.5) + 1

#     # Try all combinations of a, b, c, d such that a^2 + b^2 + c^2 + d^2 = target
#     for a in range(1, max_limit):
#         a2 = a * a
#         if a2 > target:
#             break
#         for b in range(a, max_limit):
#             b2 = b * b
#             if a2 + b2 > target:
#                 break
#             for c in range(b, max_limit):
#                 c2 = c * c
#                 if a2 + b2 + c2 > target:
#                     break
#                 for d in range(c, max_limit):
#                     d2 = d * d
#                     if a2 + b2 + c2 + d2 > target:
#                         break
#                     if a2 + b2 + c2 + d2 == target:
#                         solutions.append((a, b, c, d))

#     # Sort solutions in lexicographical order
#     solutions.sort()

#     if solutions:
#         for sol in solutions:
#             print(" ".join(map(str, sol)))
#     else:
#         print(0)

# https://www.youtube.com/watch?v=o4kAzV1mdrg

import math

n = [1] * 5
found = False

def sqrt4(i, k):
    global found
    if i < 4:
        kk = int(math.sqrt(k / (5 - i)))
        for n[i] in range(n[i - 1], kk + 1):
            sqrt4(i + 1, k - n[i] * n[i])
        return

    n[4] = int(math.sqrt(k))
    if n[4] * n[4] == k:
        print(n[1], n[2], n[3], n[4])
        found = True

def find_four_squares(k):
    global found
    found = False
    sqrt4(1, 1 << k)
    if not found:
        print(0)

if __name__ == "__main__":
	k = int(input())
	find_four_squares(k)
