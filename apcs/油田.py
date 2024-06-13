# 一家地質調查公司專門探勘地底的石油儲量，這家公司每次都會處理一大片矩形的土地，為了方便起見，他們將土地切割為許多小區塊，並使用儀器對每個小區塊進行探勘。
# 每個含有石油的小區塊我們稱之為一個油囊，如果有兩個油囊相鄰，他就隸屬於同一塊油田。油田可能非常龐大，包含相當多的油囊。
# 你的任務就是確認這塊土地中有多少個不同的油田
# Input
# 輸入包含多筆資料，每筆資料的第一行有 2 個整數 m, n (1 <= m, n <= 100)，其中 m 代表這塊土地的列數，n 代表行數，如果輸入 m = 0則表示輸入結束
# 接下來的 m 列為這塊地探勘的結果， @代表這個小區塊含有石油， *則代表不含石油
# Output
# 輸出這塊土地上油田的數量
# Sample Input #1
# 1 1
# *
# 3 5
# *@*@*
# **@**
# *@*@*
# 1 8
# @@****@*
# 5 5
# ****@
# *@@*@
# *@**@
# @@@*@
# @@**@
# 0 0
# Sample Output #1
# 0
# 1
# 2
# 2


from collections import deque

# N, NE, E, SE, S, SW, W, NW, N
directions = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]  # (x, y)


def count_oil_deposits(field):
    count = 0
    field_height = len(field)
    field_width = len(field[0])
    visited = [[False for _ in range(field_width)] for _ in range(field_height)]

    def isValidCoordinate(x, y):
        return (x >= 0 and x < field_width) and (y >= 0 and y < field_height)

    # Mark coordinate as visited
    # If coordinate is a deposit, try expanding to neighbors
    def bfs(y, x):
        queue = deque([(y, x)])
        while queue:
            y, x = queue.popleft()
            visited[y][x] = True
            if field[y][x] == "@":  # found a deposit, start expanding
                for x_offset, y_offset in directions:
                    if (
                        isValidCoordinate(x + x_offset, y + y_offset)
                        and not visited[y + y_offset][x + x_offset]
                    ):
                        queue.append((y + y_offset, x + x_offset))

    for i in range(field_height):
        for j in range(field_width):
            if not visited[i][j]:
                if field[i][j] == "@":  # found deposit, increase count
                    count += 1
                bfs(i, j)

    return count


def main():
    fields = []

    while True:
        m, n = map(int, input().split())
        if m == 0 or n == 0:
            break

        field = []
        for _ in range(m):
            field.append(list(input()))

        fields.append(field)

    res = []
    for field in fields:
        res.append(count_oil_deposits(field))

    for r in res:
        print(r)


if __name__ == "__main__":
    main()
