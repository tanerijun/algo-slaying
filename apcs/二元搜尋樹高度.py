# 根據使用者輸入的資料，建立一顆二元搜尋樹，並輸出二元搜尋樹高度

# Input
# 輸入 n ( n ≤ 10 ) 個整數

# Output
# 輸出按此順序建立的二元樹，高度為多少

# Sample Input #1
# 3 1 2 4 5
# Sample Output #1
# 3


def main():
    nums = map(int, input().split())
    max_depth = 0
    # Represents tree with array. Capacity = 2 ** 10 because max n is 10
    t = [-1] * (2**10)

    for num in nums:
        i, d = 0, 0  # current node and current depth
        while t[i] != -1:  # node is not empty, continue left or right
            i = 2 * i + (1 if num < t[i] else 2)
            d += 1  # go down 1 level
        # At this point, i points to an empty node
        t[i] = num
        max_depth = max(max_depth, d)

    res = max_depth + 1  # because the root counts as level 1
    print(res)


if __name__ == "__main__":
    main()
