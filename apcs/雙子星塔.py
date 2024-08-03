# 古老的王國中有兩座形狀不同的塔聳立在兩個不同的城市裡，兩座塔皆以圓形磚瓦堆疊而成，每塊磚瓦的高度皆相同且圓半徑均為整數。因此，儘管兩座塔形狀不同，卻包含了許多大小形狀相同的磚瓦。
# 當今國王命令建築師從塔上移除部分磚瓦，以使兩座塔的形狀和大小變為完全相同，並且要盡量讓塔的高度保持越高越好。由於此次工程，只有移除部分磚瓦而非重建，磚瓦的順序必須保持與原始建築相同。
# 國王認為這項工程可以象徵兩個城市的和諧與平等，並將這兩座塔命名為「雙子星塔」，而你被賦予一個重要的任務：找出最多可以留下多少磚瓦。

# Input
# 包含多筆測資，每筆測資代表一對雙子星塔，其中第一行有兩個整數 N1 及 N2 (1 ≤ N1, N2 ≤ 100) 分別代表兩座塔的磚瓦數。
# 第二行包含 N1 個正整數，代表第一座塔由上而下每片磚瓦的半徑。
# 第三行包含 N2 個正整數，代表第二座塔由上而下每片磚瓦的半徑。
# 當N1 及 N2 為 0 代表輸入結束。

# Output
# 對於每一對雙子星塔，請輸出它的編號及最多可保留的磚瓦數，兩組測資間請空一行。

# Sample Input #1
# 7 6
# 20 15 10 15 25 20 15
# 15 25 10 20 15 20
# 8 9
# 10 20 20 10 20 10 20 10
# 20 10 20 10 10 20 10 10 20
# 0 0

# Sample Output #1
# Twin Towers #1
# Number of Tiles : 4
#
# Twin Towers #2
# Number of Tiles : 6


# Count longest common subsequence between tower1 and tower2
def count_lcs(tower1, tower2):
    m, n = len(tower1), len(tower2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if tower1[i - 1] == tower2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def main():
    cases = []
    while True:
        N1, N2 = map(int, input().split())
        if N1 == N2 == 0:
            break
        tower1 = list(map(int, input().split()))
        tower2 = list(map(int, input().split()))
        cases.append((tower1, tower2))

    for i, case in enumerate(cases, 1):
        tower1, tower2 = case
        max_tiles = count_lcs(tower1, tower2)
        print(f"Twin Towers #{i}")
        print(f"Number of Tiles : {max_tiles}")
        print()


if __name__ == "__main__":
    main()
