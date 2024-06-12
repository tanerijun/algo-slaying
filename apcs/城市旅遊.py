# 已知所有城市之間的道路，請問是否能從A城市旅行到B城市？
# Input
# 包含多筆測資。
# 每筆測資有兩個正整數 N ( N <= 800) , M(M <= 10000 )，代表總共有 N 個城市 M 條道路。
# 下來有 M 行， 每行有 2 個正整數 x, y (1 <= x,y <= N)，代表有一條道路可以從x城市移動到y城市，所有道路都是單行道，所以y城市無法透過該條道路到達x城市。
# 最後一行有兩個正整數 A, B ( 1 <= A,B <= N ) ，代表要詢問的兩個城市
# Output
# 如果可以從A城市移動到B城市，則輸出Yes，不行請輸出No
# Sample Input #1
# 4 5
# 1 2
# 3 4
# 3 2
# 1 3
# 2 4
# 1 4
# Sample Output #1
# Yes

from collections import defaultdict


def main():
    N, M = map(int, input().split())  # N cities, M roads
    graph = defaultdict(list)

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)  # directed edge

    source, target = map(int, input().split())

    visited = set()

    def dfs(node):
        if node == target:
            return True

        visited.add(node)
        for city in graph[node]:
            if city not in visited:
                if dfs(city):
                    return True

        return False

    res = dfs(source)
    print("Yes" if res else "No")


if __name__ == "__main__":
    main()
