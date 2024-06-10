# 小宇有一個大家族。有一天，他發現記錄整個家族成員和成員間血緣關係的家族族譜。小宇對於最遠的血緣關係 (我們稱之為"血緣距離") 有多遠感到很好奇。
# 下圖為家族的關係圖。 0 是 7 的孩子， 1、2 和 3 是 0 的孩子， 4 和 5 是 1 的孩子， 6 是 3 的孩子。我們可以輕易的發現最遠的親戚關係為 4(或 5) 和 6 ，他們的"血緣距離"是 4 (4→1→0→3→6)。
# 給予任一家族的關係圖，請找出最遠的"血緣距離"。你可以假設只有一個人是整個家族成員的祖先，而且沒有兩個成員有同樣的小孩。

# Input
# 輸入包含多筆測資。每筆側資中，第一行為一個正整數 N 代表成員的個數，每人以 0~N-1 之間唯一的編號代表。
# 接著的 N-1 行，每行有兩個以一個空白隔開的整數 a 與 b (0 ≤ a, b ≤ N-1)，代表 b 是 a 的孩子。
# 其中  10%的測資滿足， 2 ≤ N ≤ 100 ，整個家族的祖先最多 2 個小孩，其他成員最多一個小孩。
# 其中  40%的測資滿足， 2 ≤ N ≤ 100。
# 其中  70%的測資滿足， 2 ≤ N ≤ 2000。
# 其中100%的測資滿足， 2 ≤ N ≤ 100000。
# Output
# 每筆測資輸出一行，輸出最遠"血緣距離"的答案。
# 本題為嚴格比對，請務必按照說明進行輸出。

# Sample Input #1
# 8
# 0 1
# 0 2
# 0 3
# 7 0
# 1 4
# 1 5
# 3 6
# Sample Output #1
# 4

# Sample Input #2
# 4
# 0 1
# 0 2
# 2 3
# Sample Output #2
# 3

# Solution proof: https://iq.opengenus.org/diameter-of-tree-using-dfs/

from collections import defaultdict, deque


# Create undirected edges
def add_edge(graph, u, v):
    graph[u].add(v)
    graph[v].add(u)


# Model graph using adjacency list
def create_graph():
    return defaultdict(set)


# Implementation using BFS
def find_farthest_node(graph, start_node):
    visited = set()
    farthest_node = start_node
    max_distance = 0
    # queue of tuple containing current_node and current_distance
    queue = deque([(start_node, 0)])
    while queue:
        current_node, current_distance = queue.popleft()
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_distance > max_distance:
            max_distance = current_distance
            farthest_node = current_node

        for neighbor in graph[current_node]:
            if not neighbor in visited:
                queue.append((neighbor, current_distance + 1))  # type: ignore

    return farthest_node, max_distance


# Implementation using DFS
def find_farthest_node_dfs(graph, start_node):
    visited = set()
    farthest_node = start_node
    max_distance = 0

    def dfs(current_node, current_distance):
        nonlocal farthest_node, max_distance
        visited.add(current_node)

        if current_distance > max_distance:
            max_distance = current_distance
            farthest_node = current_node

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                dfs(neighbor, current_distance + 1)

    dfs(start_node, 0)
    return farthest_node, max_distance


def main():
    N = int(input())
    graph = create_graph()
    for _ in range(N - 1):
        a, b = map(int, input().split())
        add_edge(graph, a, b)

    # Find the farthest node (on the boundary) using DFS/BFS
    start_node = 0  # arbitary, any node will work
    farthest_node, _ = find_farthest_node_dfs(graph, start_node)

    # Find the farthest node from the boundary to get the diameter
    _, diameter = find_farthest_node_dfs(graph, farthest_node)

    # Output
    print(diameter)


if __name__ == "__main__":
    main()
