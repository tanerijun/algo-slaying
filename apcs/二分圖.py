# 如果一個無向圖 (undirected graph) G 的頂點集合 (vertex set) 可被分割為兩個互不相交的非空子集 A 和 B，使得 G中每一條邊 (edge) 的兩個頂點分別屬於這兩個子集，那麼我們稱G 為一個「二分圖」 (bipartite graph)，並稱 A 和 B 是一個有效分割。例如： 圖一(a)是一個二分圖，因為我們可以取 A = {2, 3, 5, 9} 和 B = {1, 4, 6, 7, 8, 10, 11} 使得每一條邊的兩個頂點分別屬於 A 和 B；圖一(b)也是一個二分圖，因為 A = {1, 4, 6, 8, 11, 13} 和 B = {2, 3, 5, 7, 9, 10, 12} 是一個有效分割；圖一(c)則不是一個二分圖，因為不存在任何有效分割。
# 一個圖 G 是不是二分圖可以判斷如下。我們試著將 G 中的每一個頂點著上白色或黑色。為了方便說明，我們假設 G 是一個連通圖 (connected graph)，也就是說 G 中任兩個頂點間都存在一條路徑:而且我們稱白和黑是兩個對立的顏色。開始時我們任選一頂點著上白色，其餘所有頂點都沒有顏色。然後重複以下規則直到每一個頂點都被著上顏色：
#  (R) 挑一個有顏色的頂點，將所有和它相鄰的頂點著上對立的顏色。
# 在過程中如果發現一個已經有顏色的頂點因為 (R) 這個規則必須被著上不同的顏色，那麼就出現了矛盾，G 不是二分圖，可以停止著色。否則，可以看出在著色結束後，白和黑兩群頂點所代表兩個子集 A 和 B 是一個有效分割。
# Input
# 測試資料第一行有兩個數字 n, m ，第一個數字 n 表示圖中的頂點數， 1 < n ≤ 105 ，第二個數字 m 表示圖中的邊數， 1 ≤ m ≤ 106，接下來會有 m 行，每行有兩個正整數 i, j，i ≠ j，1 ≤ i ≤ n，1 ≤ j ≤ n，表示頂點 i 和 j 之間有一條邊。(不會有重複邊)
# Output
# 請輸出一行，如果給定的無向圖 G 不是一個二分圖，請輸出 0；如果給定的無向圖 G 是一個二分圖，請輸出最小的整數 k 滿足 G 存在一個有效分割 A 和 B，其中 A 中的頂點數是 k。
# Sample Input #1
# 4 4
# 1 2
# 4 3
# 2 4
# 1 3
# Sample Output #1
# 2
# Sample Input #2
# 11 13
# 1 2
# 11 9
# 5 7
# 3 11
# 5 6
# 3 1
# 6 9
# 2 4
# 4 5
# 8 5
# 9 8
# 9 10
# 8 2
# Sample Output #2
# 4
# Sample Input #3
# 8 10
# 6 5
# 1 4
# 5 7
# 8 6
# 3 1
# 2 1
# 5 4
# 2 5
# 8 7
# 6 3
# Sample Output #3
# 0
# Sample Input #4
# 13 12
# 8 7
# 1 2
# 3 6
# 5 4
# 1 3
# 9 8
# 11 12
# 10 8
# 6 5
# 3 4
# 6 2
# 13 12
# Sample Output #4
# 5

from collections import defaultdict, deque


def create_graph():
    return defaultdict(list)


def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def bipartite_split(adj_list, visited, start):
    queue = deque([start])
    color_map = {start: "blue"}
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        opposite_color = "red" if color_map[vertex] == "blue" else "blue"
        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                color_map[neighbor] = opposite_color
                queue.append(neighbor)
                continue
            if color_map[vertex] == color_map[neighbor]:  # confict: not bipartite
                return None

    return color_map


def main():
    # Read input and create graph
    vertex_count, edge_count = map(int, input().split())
    graph = create_graph()
    for _ in range(edge_count):
        u, v = map(int, input().split())
        add_edge(graph, u, v)

    visited = set()
    k = 0
    # We have to do this because it's not guaranteed that all vertices are connected
    for vertex in range(1, vertex_count + 1):
        if vertex not in visited:
            color_map = bipartite_split(graph, visited, vertex)

            # Return early if not bipartite
            if color_map is None:
                print(0)
                return

            set_a, set_b = [], []
            for vertex, color in color_map.items():
                if color == "blue":
                    set_a.append(vertex)
                else:
                    set_b.append(vertex)

            # Accumulate the shorter length
            k += min(len(set_a), len(set_b))

    print(k)


if __name__ == "__main__":
    main()
