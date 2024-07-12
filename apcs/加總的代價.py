# 是的，題目名稱就是你要做的任務：把一些數加起來。但是這對你來說一定是太簡單了，所以讓我們加一些東西在裡面。

# 做加法要付出的代價（cost） 定義為這2個數的總和，所以要加 1 和 10 所需付出的代價為 11 。假如你想要加 1, 2 和 3，那麼有以下幾種方法：
# 1 + 2 = 3, cost = 3
# 3 + 3 = 6, cost = 6
# Total = 9

# 1 + 3 = 4, cost = 4
# 2 + 4 = 6, cost = 6
# Total = 10

# 2 + 3 = 5, cost = 5
# 1 + 5 = 6, cost = 6
# Total = 11

# 我希望你已經瞭解你的任務，就是把 N 個數加起來使得付出的代價最少。

# Input
# 輸入含有多組測試資料。
# 每組測試資料開始有一個正整數 N（2 ≦ N ≦ 5000），接下來有 N 個正整數（均小於100000）。
# 當 N=0 時代表輸入結束。

# Output
# 針對每一組測試資料輸出一列，相加這N個數付出的代價最少是多少。
# 這個代價一定可以用 INT64 或是 long long 儲存

# Sample Input #1
# 3
# 1 2 3
# 4
# 1 2 3 4
# 0

# Sample Output #1
# 9
# 19

import heapq


def parse_input():
    test_cases = []
    while True:
        n = int(input())
        if n == 0:
            break
        test_cases.append(list(map(int, input().split())))
    return test_cases


def calculate_min_cost(nums):
    # We can be greedy here. Adding the smallest 2 numbers per iteration leads to the overall minimum cost
    # Approach: use min_heap and add the 2 smallest numbers
    heapq.heapify(nums)
    total_cost = 0

    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        cost = a + b
        total_cost += cost
        heapq.heappush(nums, cost)

    return total_cost


def main():
    test_cases = parse_input()
    for tc in test_cases:
        print(calculate_min_cost(tc))


if __name__ == "__main__":
    main()
