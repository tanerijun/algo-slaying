# Koch Snowflake's Equilateral Triangle Count

# Koch 曲線是瑞典數學家 Helge von Koch 於 1904 年提出來的。它是一種碎形，其形態似雪花，又稱 Koch 雪花曲線。一開始給定一個等邊三角形，如下方左圖 N = 1 所示，它含有三個等長的線段。接下來 N = 2 的 Koch 曲線可以由以下步驟生成：
# 將接觸外面的每個線段平分成三等份的較小線段。
# 以中間那一個較小線段為底，向外畫出一個等邊三角形。
# 此時我們看出 N = 2 時共有 4 個等邊三角形（1 個大的、3 個小的）， watch https://www.youtube.com/watch?v=OtooZTDRoS0。
# 繼續以上的步驟，N = 3 時共有大大小小的16個等邊三角形。N = 4 時可依此類推。現在要請你寫一個程式，輸入 N ，求出從 1 開始直到 N，所對應的等邊三角形的總數量。

# Input
# 測試資料只有一行，只有一個數字 N，其值為 1 至 120 的整數。

# Output
# 輸出資料為一個正整數，表示從 1 開始直到 N ，所對應的等邊三角形的總數量。
# 下面輸入範例一的輸入 N = 2，其等邊三角形的總數量為 1 + 4 = 5。
# 而輸入範例二的輸入 N = 3，等邊三角形的總數量為 1 + 4 + 16 = 21。

# Sample Input #1
# 2
# Sample Output #1
# 5
# Sample Input #2
# 3
# Sample Output #2
# 21

# Observation:
# Base Case (N = 1): Initially there is only one triangle.
# Recursive Step: At levels (N > 1), we observe the following:
# Each equilateral triangle at level N is divided into smaller equilateral triangles.
# For each equilateral triangle at level N, we create 4 equilateral triangles at level N+1.
# Additionally, there's one equilateral triangle at level N+1 that is formed from the middle segment of each side at level N.
# Conc, for each level, the number of triangles is 4 times the number of triangles at the previous level plus one additional triangle formed in the center.


def koch_triangles(N):
    if N == 1:
        return 1
    else:
        return 1 + 4 * koch_triangles(N - 1)


if __name__ == "__main__":
    N = int(input())
    print(koch_triangles(N))
