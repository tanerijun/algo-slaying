# 飛天桑妮是一隻運動神經很好的鼯鼠，她很喜歡在樹木間移動，尤其最愛從高處一躍 而下，享受滑翔的快感。她所居住的森林裡有 N 棵樹木，已知每棵樹 ti (1 ≦ i ≦ N) 的位 置 (xi, yi) 和高度 hi。桑妮的家 t1 位於 (0, 0)，而桑妮的奶奶家 tN 位於 (10000, 10000) 的位置。這個週末她要去奶奶家，因而尋求你的協助。 從家裡前往奶奶家的旅程可定義為由 K (2 ≦ K ≦ N) 棵相異樹木構成的序列 π= [π(1) = 1, π(2), …, π(K) = N]。 由於桑妮想要快點到奶奶家，所以旅程後段的樹木不能比前段的樹木離桑妮家還近，也就 是 d(t1, tπ(i+1)) ³ ≧d(t1, tπ(i))，其中 d(ti, tj) 表示兩棵樹 ti 和 tj 的直線距離。當桑妮從一棵較 高的樹 tπ(i) 跳到下一棵樹 tπ(i+1) 時，如果是由高到低，她就能使出滑翔絕技，享受樂趣。 高度差越大，樂趣就越大，因此我們可以把樂趣值定為 max{0, hπ(i) - hπ(i+1)}。她希望這段 旅程中可以享受到最大的樂趣，因此想請你幫忙寫一個程式，計算所有可能的旅程中，最 大的樂趣值為多少。
# 以上圖為例，森林中有五棵樹，其位置和高度如圖所示。如果桑妮的旅程是 [1, 2, 3, 4, 5]，則這段旅程的最大樂趣為 t3 到 t4 得到的樂趣值 300 – 100 = 200；如果旅程是 [1, 3, 5]，則最大樂趣為 t3 到 t5 得到的樂趣值 300 – 150 = 150。旅程 [1, 3, 2, 5] 是不合理的， 因為 t2 比 t3 離桑妮家還要近。旅程 [1, 5] 是合理的（記得飛天桑妮的運動神經很好嗎）， 但最大樂趣值是 0。

# Input
# 第一列有一個正整數 N (N ≦100,000)，代表森林中的樹木數。接下來的 N 列，每一 列有3個正整數 xi、 yi (1 ≦ xi, yi ≦ 10,000) 和 hi (1≦ hi ≦ 100,000)，彼此間以一個空白隔開， 代表第 i 棵樹 ti 在位置(xi, yi)，且該樹高度為 hi。
# Output
# 請輸出所有合理旅程中，最大的樂趣值。
# Sample Input #1
# 5
# 3000 1000 50
# 8000 7000 100
# 0 0 100
# 3000 5000 300
# 10000 10000 150
# Sample Output #1
# 200
# Sample Input #2
# 7
# 0 0 42
# 5726 1480 29359
# 6965 4467 5706
# 8148 3284 16828
# 6335 6503 19170
# 9962 492 2996
# 10000 10000 18468
# Sample Output #2
# 26363


def main():
    N = int(input())
    trees = []  # contains tuple (x, y, h)
    for _ in range(N):
        tree = tuple(map(int, input().split()))
        trees.append(tree)

    # Sort by distance
    # In case where distance is equal, sort by height in reverse
    trees.sort(key=lambda t: (t[0] ** 2 + t[1] ** 2, -t[2]))

    highest_tree_height = trees[0][2]
    max_enjoyment = 0
    for tree in trees:
        h = tree[2]
        enjoyment = highest_tree_height - h
        max_enjoyment = max(max_enjoyment, enjoyment)
        highest_tree_height = max(highest_tree_height, h)

    print(max_enjoyment)


if __name__ == "__main__":
    main()
