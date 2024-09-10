# 有一個城鎮有 n 棟高樓，樓高分別為 h1, h2, ..., hn，市長想要在城鎮中心舉辦高空特技表演，
# 該特技表演會從某棟大樓上朝右側滑翔至地面。 為了表演人員的安全，滑翔的路徑樓高必須越來越低，請你找出一個最長的滑翔路徑。

# Input
# 第一行有一個正整數 n(5 <= n < = 100)。
# 第二行有個正整數h1, h2, ..., hn (1 < hi < 1000) 代表樓高。

# (60 分): n = 5
# (40 分): 無限制

# Output
# 輸出最長的滑翔路徑長度。

# Sample Input #1
# 5
# 6 2 5 3 1

# Sample Output #1
# 3

# Sample Input #2
# 10
# 31 41 97 93 23 89 59 26 15 58

# Sample Output #2
# 4

# Hint ：
# 範例 1: 選擇 5, 3, 1, 滑翔長度為3。
# 範例 2: 選擇 89, 59, 26, 15, 滑翔長度為4。


# Basically solving LDS


# def main():
#     n = int(input())
#     heights = list(map(int, input().split()))

#     dp = [0] * n

#     for i in range(n - 2, -1, -1):  # from right to left
#         for j in range(i + 1, n):  # check all to the right
#             if heights[i] > heights[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)

#     print(max(dp))


def main():
    n = int(input())
    heights = list(map(int, input().split()))
    res = 0
    i = 0
    while i < len(heights) - 2:
        j = i + 1
        while j < len(heights) and heights[j] < heights[j - 1]:
            j += 1
        res = max(res, j - i)
        i = j

    print(res)


if __name__ == "__main__":
    main()
