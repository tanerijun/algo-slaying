# 冒險者萊恩在新手村訓練即將屆滿一年，他詢問師父，什麼時候才能離開新手村，到 外面的世界冒險。師父聽聞，拿出一張世界地圖，用手指了地圖的一個位置。
# 「萊恩，我們在這裡，這是新手村。你想到哪裡去呢？」
# 萊恩很興奮地說，「聽說迷霧森林很刺激，我想去那裡看看。」
# 師父又用手指了地圖上另一個位置，「這裡就是迷霧森林。」接著，師父在地圖上雙 手揮舞，地圖上開始浮現許多數字。
# 「哇，好酷喔！師父，這些數字是什麼意思！」
# 「沒有數字的區域代表無法橫跨的沙漠，數字代表可行經區域裡的怪物等級；如果冒 險者的等級低於怪物等級，是沒辦法活著通過那個區域的。」
# 「啊！？」萊恩很仔細地看著地圖，慢慢地用手指帶出一條路線。「我如果從新手村 往北走，再往東走，這樣說起來，我得把我的等級提升到 5 級，才能到得了迷霧森林了。」 目前等級只有 4 級的萊恩低下頭。
# 「別急，萊恩，看看這裡。」師父抓著萊恩的手指，你可以先往東走，再往北走，然 後往西抵達迷霧森林。這條路線，4 級的你就能辦到了。」
# 「喔耶！謝謝師父！」
# 真實冒險世界的地圖很大，需要你的幫忙。請你寫一個程式，給定地圖尺寸、新手村 和迷霧森林的位置，以及地圖上區域的怪物等級，計算出萊恩最少需要幾等級，才能從新 手村出發，安全抵達迷霧森林。

# Input
# 第一行有兩個正整數 R 和 C (1 ≦ R, C ≦ 1000)，代表地圖有幾列與幾行。
# 第二行有四個整數 Rs, Cs, Rd, Cd (0 ≦ Rs, Rd < R，0 ≦ Cs, Cd < C)，其中 (Rs, Cs) 代 表新手村的位置，(Rd, Cd) 代表迷霧森林的位置。新手村和迷霧森林很安全，裡 面必定沒有怪物。新手村和迷霧森林不會在同一個位置。
# 第三行有一個整數 N (0 ≦ N ≦ R×C)，代表地圖中有幾個可以行經的區域。
# 接下去有 N 行，第 i 行有三個整數值 Ri, Ci, Li (0 ≦ Ri < R，0 ≦ Ci < C，1 ≦ Li ≦ 109 )，分別代表區域座標和該區域怪物等級。
# 輸入中，任兩個整數間以一個空白隔開。

# Output
# 輸出萊恩最少需要為幾等級，才能從新手村出發，平安抵達迷霧森林。（測試資料保 證存在至少一條從新手村到迷霧森林的路。）

# Sample Input #1

# 6 5
# 1 1 4 3
# 18
# 0 0 2
# 0 1 3
# 1 0 1
# 1 2 1
# 1 3 4
# 1 4 2
# 2 0 3
# 2 1 2
# 2 4 4
# 3 1 3
# 3 2 5
# 3 3 2
# 3 4 3
# 4 1 3
# 4 2 5
# 4 4 2
# 5 2 2
# 5 3 2

# Sample Output #1
# 4

# Passed 65% of the test cases, the rest: MemoryError
# The same solution in C++ passed all the test cases

import heapq


def find_minimum_level(R, C, start, end, map_grid):
    rs, cs = start

    distances = {(rs, cs): 0}
    pq = [(0, rs, cs)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    while pq:
        max_level, r, c = heapq.heappop(pq)

        if (r, c) == end:
            return max_level

        if max_level > distances.get((r, c), float("inf")):
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and map_grid[nr][nc] != -1:
                new_max_level = max(max_level, map_grid[nr][nc])

                if new_max_level < distances.get((nr, nc), float("inf")):
                    distances[(nr, nc)] = new_max_level
                    heapq.heappush(pq, (new_max_level, nr, nc))

    return -1  # No path found (shouldn't happen)


def main():
    R, C = map(int, input().split())
    Rs, Cs, Rd, Cd = map(int, input().split())
    N = int(input())

    map_grid = [[-1] * C for _ in range(R)]

    # Set start and end points to 0 (no monsters)
    map_grid[Rs][Cs] = 0
    map_grid[Rd][Cd] = 0

    # Fill in passable areas with monster levels
    for _ in range(N):
        Ri, Ci, Li = map(int, input().split())
        map_grid[Ri][Ci] = Li

    result = find_minimum_level(R, C, (Rs, Cs), (Rd, Cd), map_grid)
    print(result)


if __name__ == "__main__":
    main()
