# 輸入第一列給定三正整數 n 、 m 、 k （1 ≦ n 、 m 、 k ≦ 50），代表有 n 個伺服器（編號 0 ～ n - 1）、 m 座城市（編號 0 ～ m - 1）以及 k 個伺服器放置方案。

# 接著有 n 列輸入，每列給定 m 個非負整數，代表這 n 個伺服器到 m 個城市的預計流量。再接著有 k 列輸入，每列給定 n 個非負整數，代表在此方案下每個伺服器要分配到哪個城市。

# 假設有伺服器的城市 u 有流量到城市 v （若有多個伺服器有起點、終點一樣的流量路徑，則先將這些路徑合併再做其他計算），則：
# 當 u ＝ v 時，則每單位流量需要花 1 元；
# 當 u ≠ v 時， ≦ 1000 之部分每單位 3 元 、 > 1000 之部分則變為每單位 2 元。

# 試問給定的 k 個方案中哪個方案之總成本最小，其值為何？

# Sample Input #1
# 2 3 3
# 30 23 23
# 5 25 3
# 0 0
# 0 1
# 0 2

# Sample Output #1
# 217

# Sample Input #2
# 3 4 5
# 500 400 800 200
# 500 400 100 600
# 450 420 800 790
# 0 0 0
# 0 1 2
# 0 2 2
# 2 1 2
# 1 1 1

# Sample Output #2
# 13470

def main():
    n, m, k = map(int, input().split())

    Q = []
    for _ in range(n):
        Q.append(list(map(int, input().split())))

    proposals = []
    for _ in range(k):
        proposals.append(list(map(int, input().split())))

    min_cost = float('inf')
    for proposal in proposals:
        total_cost = 0

        for v in range(m):
            city_traffic = [0] * m # store traffic from other cities to this city
            for server, city in enumerate(proposal):
                city_traffic[city] += Q[server][v]
            for u, traffic in enumerate(city_traffic):
                if traffic > 0:
                    if u == v:
                        total_cost += traffic
                    elif traffic <= 1000:
                        total_cost += traffic * 3
                    else:
                        total_cost += 1000 * 3 + (traffic - 1000) * 2

        min_cost = min(min_cost, total_cost)

    print(min_cost)

main()
