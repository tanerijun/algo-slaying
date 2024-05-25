# Content
# 給定凸多邊形的頂點座標，請使用結構(struct)儲存點座標，並計算多邊形面積

# Input
# 輸入一個數字n(n<100)，代表圖形是一個n邊形
# 接下來有n列，每列有兩個小數，代表一個點座標，且這些座標已按照順時針排序

# Output
# 請輸出多邊形面積到小數點以下兩位

# Sample Input #1
# 4
# 0.0 0.0
# 0.0 1.0
# 1.0 1.0
# 1.0 0.0

# Sample Output #1
# 1.00

def calc_polygon_area():
	n = int(input())
	vertices = []
	for _ in range(n):
		x, y = map(float, input().split())
		vertices.append((x, y))

	# Shoelace Formula - Find area of polygon
	# https://en.wikipedia.org/wiki/Shoelace_formula
	area = 0.0
	for i in range(len(vertices)):
		j = (i + 1) % len(vertices)
		area += vertices[i][0] * vertices[j][1]
		area -= vertices[j][0] * vertices[i][1]
	area = abs(area) / 2.0

	print(f"{area:.2f}")

if __name__ == "__main__":
	calc_polygon_area()
