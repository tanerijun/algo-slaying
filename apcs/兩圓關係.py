# 給定平面上n個圓形的圓心和半徑資料，請使用結構(struct)儲存圓的資料，並輸出指定兩個圓之間的關係（外離、外切、相交兩圓、內切、內離）

# Input
# 輸入一個整數n(n<=50)代表總共有n個圓，接下來有n列資料，每列有兩個整數代表圓心座標，及一個小數代表圓半徑
# 輸入一個整數m(m<=200)代表要詢問m組兩圓關係，接下來有m列資料，每列有兩個數字，代表兩個圓的編號

# Output
# 請輸出m組兩圓關係

# Sample Input #1
# 3
# 1 1 1.0
# 1 3 1.0
# 4 4 1.0
# 2
# 1 2
# 1 3

# Sample Output #1
# 外切
# 外離

import math
import sys
import io

# Set default encoding to UTF-8 because test env is in ASCII
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def circle_relationship():
	n = int(input())
	circles = []
	for _ in range(n):
		x, y, r = input().split()
		circles.append((int(x), int(y), float(r)))

	m = int(input())
	for _ in range(m):
		input1, input2 = map(int, input().split())
		circle1, circle2 = circles[input1 - 1], circles[input2 - 1] # input uses one-based-indexing
		x1, y1, r1 = circle1
		x2, y2, r2 = circle2

		# Find distance: Euclidean Distance Formula -> Distance between 2 points in 2D plane
		# https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions
		distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

		# Find relationship: https://web.ntnu.edu.tw/~496403159/teachpage/2cir.htm
		if distance == r1 + r2:
			print("外切")
		elif distance > r1 + r2:
			print("外離")
		elif distance == abs(r1 - r2):
			print("內切")
		elif distance < abs(r1 - r2):
			print("內離")
		else:
			print("相交兩圓")

if __name__ == "__main__":
	circle_relationship()
