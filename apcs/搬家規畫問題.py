# 有個大家族找搬家公司協助分批搬遷，家族要求每個成員列出要般的物品重量與需求度，請搬家公司根據車子的載重量，讓車子搬運的物品的種需求度最高，
# 以便盡快讓家族安居，請你為搬家公司寫一個程式，根據輸入的物品重量、物品的需求度、與車子的載重量，計畫出一次最多可搬運的總需求度。
# 舉例來說，以下例子中，第一列共有7個物品的重量，第二列為每個物品的需求度。
# 若載重量為5時，最多可搬運的總需求度為10，其中一種可能的搬運組合為物品3、物品4、與物品7。
# 若載重量為7時，最多可搬運的總需求度為13。其中一種可能的搬運組合為物品3、物品4、物品6、與物品7。
# 物品重量  1   1   1   1   2   2   3
# 需求程度	1	1	2	3	1	3	5

# Input
# 測試資料 共有三列。第一列有 A （1 ≤ A ≤ 1000）個以一空格開的整數 B （1 ≤ B ≤ 1000）代表 物品重量 。第二列同樣有 同樣有 A個以一空格開的整數 B代 表每個物品的需求度 。第三列有一個整數 C （1 ≤ C ≤ 1000000），代表 載重量 。

# Output
# 輸出 1個整數，代表 最多可搬運的總需要度 。

# Sample Input #1
# 1 1 1 1 2 2 3
# 1 1 2 3 1 3 5
# 7

# Sample Output #1
# 13

# Sample Input #2
# 815 906 127 914 633 98 279 547 958 965
# 158 971 958 486 801 142 422 916 793 960
# 5000

# Sample Output #2
# 5963


def main():
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    capacity = int(input())

    # store max_val for each weight up to capacity (0 to capacity)
    cache = [0] * (capacity + 1)

    for i in range(len(weights)):
        for j in range(capacity, weights[i] - 1, -1):
            cache[j] = max(cache[j], cache[j - weights[i]] + values[i])

    print(cache[-1])


if __name__ == "__main__":
    main()
