# 給一個數列 S = { S1, S2, … , Sn }，你必須計算數列中連續項的最大乘積，如果最大乘積不是正數，應該輸出 0 表示無解
# Input
# 包含多組測試資料，每組測試資料開頭為一個正整數 1 ≤ N ≤ 18, 代表這個數列的項數，其中 -10 ≤ Si ≤ 10
# 接下來的 N 個數字即數列
# Output
# 每組測試輸出一列 "Case #M: The maximum product is P." 其中 M 代表測資的編號（從1開始計數），而 P 代表最大乘積。
# 每組測試資料後面請印出一行空白列。
# Sample Input #1
# 3
# 2 4 -3
# 5
# 2 5 -1 2 -1
# Sample Output #1
# Case #1: The maximum product is 8.
# Case #2: The maximum product is 20.

import sys


# Brute force (O(n^2))
def get_maximum_product(arr):
    if not arr:
        return 0

    max_product = float("-inf")
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            max_product = max(max_product, product)

    return max_product


def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    index = 0
    case_count = 1
    result = []
    while index < len(data):
        if index % 2 == 1:  # process only the array lines
            arr = list(map(int, data[index].split()))
            res = get_maximum_product(arr)
            result.append(f"Case #{case_count}: The maximum product is {res}.")
            case_count += 1
        index += 1

    for res in result:
        print(res)


if __name__ == "__main__":
    main()
