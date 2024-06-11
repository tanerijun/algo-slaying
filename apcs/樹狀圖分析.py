# 本題是關於有根樹(rooted  tree)。在一棵 n 個節點的有根樹中，每個節點都是以 1 ~ n 的不同數字來編號，描述一棵有根樹必須定義節點與節點之間的親子關係。一棵有根樹恰有一個節點沒有父節點(parent)，此節點被稱為根節點(root)，除了根節點以外的每一個節點都恰有一個父節點，而每個節點被稱為是它父節點的子節點(child)，有些節點沒有子節點，這些節點稱為葉節點(leaf)。在當有根樹只有一個節點時，這個節點既是根節點同時也是葉節點。
# 在圖形表示上，我們將父節點畫在子節點之上，中間畫一條邊(edge)連結。例如，圖一中表示的是一棵 9 個節點的有根樹，其中，節點 1 為節點 6 的父節點，而節點 6 為節點 1 的子節點；又 5、3 與 8 都是 2 的子節點。節點 4 沒有父節點，所以節點 4 是根節點；而 6、9、3 與 8 都是葉節點。
#  	 	 	 	4
#  	 	 	/	 	\
#  	 	1	 	 	 	7
#  	/	 	 	 	 	 	\
# 6	 	 	 	 	 	 	 	2
#  	 	 	 	 	 	 	/	|	\
#  	 	 	 	 	 	 	5	3	8
#  	 	 	 	 	 	 	|
#  	 	 	 	 	 	 	9

#  樹狀圖中的兩個節點 u 和 v 之間的距離 d(u,v) 定義為兩節點之間邊的數量。如圖一中，d(7, 5) = 2，而 d(1, 2) = 3。對於樹狀圖中的節點 v，我們以 h(v) 代表節點 v 的高度，其定義是節點 v 和節點 v 下面最遠的葉節點之間的距離，而葉節點的高度定義為 0。如圖一中，節點 6 的高度為 0，節點 2 的高度為 2，而節點 4 的高度為 4。此外，我們定義 H(T)為 T 中所有節點的高度總和，也就是說 H(T)  =  ∑v∈T  h(v)。給定一個樹狀圖 T，請找出 T 的根節點以及高度總和 H(T)。

# Input
# 第一行有一個正整數 n 代表樹狀圖的節點個數，節點的編號為 1 到 n。
# 接下來有 n 行，第 i 行的第一個數字 k 代表節點 i 有 k 個子節點，第 i 行接下來的 k 個數字就是這些子節點的編號。
# 每一行的相鄰數字間以空白隔開。
# Output
# 輸出兩行各含一個整數，第一行是根節點的編號，第二行是 H(T)。

# Sample Input #1
# 7
# 0
# 2 6 7
# 2 1 4
# 0
# 2 3 2
# 0
# 0
# Sample Output #1
# 5
# 4

# Sample Input #2
# 9
# 1 6
# 3 5 3 8
# 0
# 2 1 7
# 1 9
# 0
# 1 2
# 0
# 0
# Sample Output #2
# 4
# 11

from collections import defaultdict


def main():
    n = int(input())  # num of vertices
    tree = defaultdict(list)
    for i in range(1, n + 1):  # vertex value: 1 to n
        data = list(map(int, input().split()))
        childrens = data[1:]  # ignore first element (it tells the number of children)
        tree[i] = childrens

    heights = [-1] * n

    def get_height_dfs(node):
        if heights[node - 1] != -1:  # check cache
            return heights[node - 1]

        if len(tree[node]) == 0:  # leaf node
            heights[node - 1] = 0
            return 0

        res = 1 + max(map(get_height_dfs, tree[node]))
        heights[node - 1] = res
        return res

    for node in tree:
        get_height_dfs(node)

    total_height = 0
    max_height = 0
    root = 0
    for i, height in enumerate(heights):
        total_height += height
        if height > max_height:
            max_height = height
            root = i + 1  # vertex value: 1 to n

    print(root)
    print(total_height)


# Node with the highest height is the root

if __name__ == "__main__":
    main()
