# 一個益智遊戲：有一塊面積為 N^2 的正方形（區分為 N^2 個單元）農地，玩家須在農地上找出最有效益的農作物採收區域，採收區域限制為連續區域（正方形或長方形），但不一定要從周圍開始採收，也可以通通不採收。
# 但要注意—不是每一單元的採收都有效益（加分），採收到農作物尚未完全成熟的單元會造成虧損（扣分）！每個單元以一個整數來表示正或負的分數。正數代表有效益的採收單元及其得分，負數代表虧損的採收單元及其扣分。
# 範例一：以下為一  單元的農地，以及其每一單元加、扣分：
#     0   -2  -8  1
#     11  2   -6  0
#     -1  -3  -9  12
#     1   9   0   3
# 以上例而言，最有效益的採收區域如下：
#     11  2
#     -1  -3
#     1   9
# 也就是說，最佳採收區域的得分為 19 分，出現在左下角的六個採收單元(11+2-1-3+1+9 = 19)，其他的連續採收區域（正方形或長方形）的得分都比 19 小。
# 你的任務是：寫一程式計算出最佳採收區域的得分(最高得分)。

# Input
# 輸入的第一列有一正整數 N(1≦N≦100)，代表農地每一邊的長度。第二列開始有 N^2 個整數（值為-127~127、以空白鍵或換行鍵隔開），代表以列為主(row major)由左至右每個單元的分數。

# Output
# 最佳採收區域的得分（最高得分）

# Sample Input #1
# 4
# 0 -2 -8 1 11 2 -6 0 -1 -3 -9 12 1 9 0 -3

# Sample Output #1
# 19

# Sample Input #2
# 2
# 0 -1 0 -3

# Sample Output #2
# 0

# Kadane's algorithm: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
def max_subarray_sum(arr):
    max_so_far = float("-inf")
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# Find rectangle (submatrix) with the largest sum
def max_sum_rectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float("-inf")

    for left in range(cols):  # iterate through all possible left boundaries
        temp = [0] * rows  # store sum of elems in each row between curr l&r bound
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            current_sum = max_subarray_sum(temp)  # find top and bottom boundaries
            max_sum = max(max_sum, current_sum)

    return max(max_sum, 0)  # Return 0 (not harvesting) if all values are negative


def main():
    N = int(input())
    field = []
    tiles = list(map(int, input().split()))
    for i in range(0, len(tiles), N):
        field.append(tiles[i : i + N])

    result = max_sum_rectangle(field)
    print(result)


if __name__ == "__main__":
    main()
