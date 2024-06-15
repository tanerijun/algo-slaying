# 打卡公司為了促進城市觀光，發展一個可推薦前往觀光(打卡)的App。該公司選定了 N 個觀光（打卡）點，若遊客在任一觀光點打卡，該App就會預測遊客可能會有興趣的其他觀光點並推薦給該遊客。
# 為了能夠準確預測該推薦的觀光點，打卡公司設計了觀光景點相關性地圖（如下圖），圖上有 N 個點，分別以 V1, V2, V3, …, VN 代表觀光點，並精心挑選了 N−1 組觀光點以線段相連並依據經驗給定 Ri,j 值，以代表 Vi 與 Vj 的相關性。特別的是，該圖之任意兩點 Vm 與 Vn 一定有單一路徑 p ，相互串連，而Vm 與 Vn 的相關性就為該路徑上所有已知相關性的最小值 (即路徑上最小Ri,j值)。以下圖為例 V1 與 V2的相關性為 min {4, 3, 6} = 3。
# 請寫一個程式計算與任一觀光點 Vk 相關性至少為 q 的景點數量。
# Input
# 輸入的第一行有三個以空白符號隔開的正整數 N, Vk, q。接著 N-1 行中，每一行有三個空白符號隔開的正整數分別代表 i, j, Ri,j。保證1 ≤ i ≤ N、1 ≤ j ≤ N、q≤109、Ri,j ≤ 109。
# Output
# 請輸出與觀光點 Vk 相關性不低於 q 的景點數量。
# Sample Input #1
# 3 2 4
# 1 2 3
# 1 3 2
# Sample Output #1
# 0
# Sample Input #2
# 6 4 6
# 4 2 10
# 3 6 3
# 5 3 8
# 2 3 6
# 1 6 4
# Sample Output #2
# 3

from collections import defaultdict


def main():
    vertex_count, source, target = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(vertex_count - 1):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    visited = set()
    stack = []  # monotonic decreasing stack
    valid_correlation = 0

    def dfs(node, current_min):
        nonlocal valid_correlation

        visited.add(node)

        should_pop = False
        if len(stack) == 0 or current_min < stack[-1]:
            stack.append(current_min)
            # Since this node is the minimum so far, when we're done,
            # we should pop and correlation will be the previous minimum
            # Ex: if our stack is [10, 6, 3], and we're done with node that give val 3,
            # we should pop it from the stack
            should_pop = True

        correlation = stack[-1]
        if correlation >= target:
            valid_correlation += 1

        for n, w in graph[node].items():
            if n not in visited and n != source:
                dfs(n, w)

        if should_pop:
            stack.pop()

    for n, w in graph[source].items():
        if n not in visited:
            dfs(n, w)

    print(valid_correlation)


if __name__ == "__main__":
    main()
