# 有一組探險隊要去一個樹狀結構的石窟內探險，該石窟內有 個石室，第 個石室有一個編號 ，若 為偶數則會有 條分支(左分支和右分支)，若 為奇數則有 條分支(左分支、中分支和右分支)。
# 探險隊想要紀錄這個石窟的結構，每次只要第一次走到一個新的石室，就會將該石室的編號記錄在紙上，並由左到右依序走訪該石室的分支們，若走到一條死路則會在紙上紀錄一個數字
# ，若該石室已經走完所有分支則退回到上一個石室，走訪完整個石窟後在紙上得到上一個數字序列。
# 探險隊回到基地後忘記計算了這個石窟內所有相鄰的石室編號相差取絕對值的總和，請幫助探險隊從紙上的序列推算出該數值。

# Input
# 輸入一個整數個數不超過
# 的整數序列，石室的編號不超過 ，並保證造出來的樹深度不超過 。

# 子題配分
# (20%): 石室數量最多不超過 個，編號均為偶數
# (20%): 石室數量最多不超過 個
# (60%): 石室最大深度不超過40層，而且編號和石室編號不超過 ，答案可能會超過。

# Output
# 輸出一個整數代表這個石窟內所有相鄰的石室編號相差取絕對值的總和，答案大小有可能會超過。

# Sample Input #1
# 2 6 0 8 14 0 0 0 10 0 4 0 0

# Sample Output #1
# 26

# Sample Input #2
# 5 2 10 0 0 0 8 0 0 17 0 0 0

# Sample Output #2
# 26


def main():
    ids = list(map(int, input().split()))
    root = ids[0]
    res = 0
    idx = 1

    def dfs(node):
        nonlocal res, idx

        if idx == len(ids) or node == 0:
            return

        child_count = 2 if node % 2 == 0 else 3
        for _ in range(child_count):
            new_node = ids[idx]
            idx += 1
            if new_node != 0:
                res += abs(node - new_node)
            dfs(new_node)

    dfs(root)
    print(res)


main()
