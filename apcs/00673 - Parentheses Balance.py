# 在本題中，題目會先給你一個包含小括號（）及中括號〔〕的字串。當字串符合下列條件時我們稱他為正確的運算式：
#     該字串為一個空字串
#     如果Ａ和Ｂ都為正確的運算式，則ＡＢ也為正確的運算式，
#     如果Ａ為正確的運算式，則（Ａ）及〔Ａ〕都為正確的運算式。
# 現在，請你寫一支程式可以讀入這類字串並檢查它們是否為正確的運算式。字串的最大長度為128個字元。

# Input
# 輸入的第一列為正整數n，代表接下來有n列待測資料。

# Output
# 檢查每列待測資料，如果正確輸出Yes，否則輸出No。

# Sample Input #1
# 3
# ([])
# (([()])))
# ([()[]()])()

# Sample Output #1
# Yes
# No
# Yes

def is_balanced(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(")")
        elif ch == "[":
            stack.append("]")
        else:
            if len(stack) == 0 or stack.pop() != ch:
                return False
    return len(stack) == 0

def main():
    n = int(input())
    for _ in range(n):
        inp = input()
        if is_balanced(inp):
            print("Yes")
        else:
            print("No")

main()
