# 給定一維座標上一些線段，求這些線段所覆蓋的長度，注意，重疊的部分只能算一 次。例如給定三個線段：(5, 6)、(1, 2)、(4, 8)、和(7, 9)，如下圖，線段覆蓋長度為 6。
# Input
# 第一列是一個正整數 N，表示此測試案例有 N 個線段。
# 接著的 N 列每一列是一個線段的開始端點座標和結束端點座標整數值，開始端點 座標值小於等於結束端點座標值，兩者之間以一個空格區隔。
# Output
# 輸出其總覆蓋的長度 。
# Sample Input #1
# 5
# 160 180
# 150 200
# 280 300
# 300 330
# 190 210
# Sample Output #1
# 110
# Sample Input #2
# 1
# 120 120
# Sample Output #2
# 0


# Memory Error
def main0():
    N = int(input())
    data = []
    s = set()
    for _ in range(N):
        a, b = map(int, input().split())
        data.append((a, b))
    for start, end in data:
        for i in range(start, end):
            s.add(i)

    print(len(s))


def main():
    N = int(input())
    data = []
    for _ in range(N):
        a, b = map(int, input().split())
        data.append((a, b))
    data.sort()

    res = 0
    right = 0
    for start, end in data:
        if end > right:
            if start > right:  # not connected
                res += end - start
            else:
                res += end - right
            right = end

    print(res)


if __name__ == "__main__":
    main()
