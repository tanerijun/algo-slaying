# 給定兩個容量分別為x公升和y公升的無刻度容器，若只能將容器完全裝滿、完全倒光或將水倒到另外的容器中，要設法量出z公升的水最少需要多少次? (裝滿、倒光、倒到另一個容器各算一次)，若無法倒出z公升的水則輸出-1。假設處理過程中水量不損耗，水無限供應。
# 假設以序對 (x, y) 代表目前容量。若x=3, y=5, z=4，則其可能的動作如下：
# (1)先把三公升容器的水加滿 (3, 0)
# (2)將三公升容器中的水倒入五公升的容器內，這時五公升容器內有3公升水 (0, 3)
# (3)再次把三公升的水加滿變成 (3, 3)
# (4)再將三公升容器中的水倒入五公升倒滿五公升的容器內，五公升容器裝滿5公升水，而這時三公升容器內的水應該還剩下1公升 (1, 5)，
# (5) 請把五公升容器內的水全倒掉 (1, 0)
# (6)再將三公升容器內的所剩1公升水倒入五公升容器內 (0, 1)
# (7) 再一次將三公升的容器裝滿 (3, 1)
# (8)再倒入現有1公升水的五公升容器內，就這樣出現4公升的水 (0,4)。
# 共需要8次，其步驟可以表示如下：(3, 0) – (0, 3) – (3, 3) –(1, 5) –(1, 0) –(0, 1) –(3, 1) –(0, 4)。
# 範例 x=9, y=7, z=6，則可能的方法為 (9, 0) – (2, 7) – (2, 0) – (0, 2) – (9, 2) –(4, 7) –(4, 0) –(0, 4) –(9, 4) –(6, 7) 需10次。
# 範例x=6, y=4, z=3，則可能的方法為 (6, 0)– ( 2, 4) – ( 2, 0) – (0, 2) – (6, 2) –(4, 4) –(4, 0) – (0, 4)– (6, 4) – (6, 0) 無法量出。

# Input
# 輸入資料中每一列為一整數n，代表接下來有n組測試資料。
# 第二列開始每列有三個正整數，正整數間以一個空白隔開，依序為 x, y, z 。

# Output
# 輸出量出z公升所需要的最少動作次數，輸入資料錯誤或無法量出請輸出 -1 。

# Sample Input #1
# 3
# 3 5 4
# 9 7 6
# 6 4 3

# Sample Output #1
# 6
# 10
# -1

from collections import deque


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solve_water_jug(x, y, z):
    # Return early when it's impossible to measure z liters.
    # z > max(x, y): impossible as we can't fill that much water in either jug.
    # gcd(x, y) represents the smallest amount of water we can measure.
    # Any amount of water we can measure will be a multiple of this gcd.
    if z > max(x, y) or z % gcd(x, y) != 0:
        return -1

    queue = deque([(0, 0, 0)])  # (x_jug, y_jug, steps)
    visited = set([(0, 0)])

    while queue:
        x_jug, y_jug, steps = queue.popleft()

        if x_jug == z or y_jug == z:
            return steps

        # Try all possible actions
        next_states = [
            (x, y_jug),  # Fill x
            (x_jug, y),  # Fill y
            (0, y_jug),  # Empty x
            (x_jug, 0),  # Empty y
            (min(x_jug + y_jug, x), max(0, y_jug - (x - x_jug))),  # Pour y to x
            (max(0, x_jug - (y - y_jug)), min(x_jug + y_jug, y)),  # Pour x to y
        ]

        for new_x, new_y in next_states:
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))

    return -1


def main():
    n = int(input())
    results = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        steps = solve_water_jug(x, y, z)
        results.append(steps)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
