# 有一家新開張速食店，客人到店內消費採先到先服務(First in first out)的順序，每一個顧客都很有耐心，只要開始排隊了就一定會排到吃到餐點為止，而且客人不會插隊。老闆為了瞭解一天之內，來店消費顧客其排隊隊伍最長為多長(正在被服務者不算入等待隊伍長度內)，特別委請你設計一程式來幫他計算。
# 假定客人進來排隊的時間以及每個人被服務的時間都是預先知道的，同時一個時間只能服務一個客人。現在給你一群顧客進來消費的時間資料，請計算此店的服務排隊隊伍最長為多少。

# Input
# 第一行為一個正整數 n(n<=100) ，代表客人數量。
# 接下來共有 n 行，每一行有兩個整數q及s，分別代表客人的來店排隊的時間點以及需要被服務的時間。
# 其中，0<q≤1000、0<s≤1000且輸入以 q 排序（意即依照來店時間點的先後順序輸入）。
# Output
# 輸出一個整數，代表隊伍最長的長度(正在被服務者不算入等待隊伍長度內)。如範例1，第一個客人來店時不需排隊，之後兩個客人到達時，因為第一個客人尚未服務完畢，因此該筆測資最長的隊伍長度為 2 。

# Sample Input #1
# 3
# 1 10
# 2 5
# 3 1
# Sample Output #1
# 2
# Sample Input #2
# 3
# 1 2
# 2 3
# 5 1
# Sample Output #2
# 1

from collections import deque

def calc_longest_queue():
	n = int(input())
	customers = []
	for _ in range(n):
		q, s = map(int, input().split())
		customers.append((q, s))

	queue = deque()
	max_queue_length = 0

	for arrival_time, service_time in customers:
		# Remove customers that're done
		while queue and queue[0][1] < arrival_time:
			queue.popleft()

		# Calculate finish time
		# There are 2 possible scenarios
		# 1. Queue empty: no need to wait, start processing 1 tick
		# 2. Queue isn't empty: have to wait until the last person in queue before we can start processing
		finish_time = arrival_time + service_time - 1 if len(queue) == 0 else queue[-1][1] + service_time

		queue.append((arrival_time, finish_time))

		max_queue_length = max(max_queue_length, len(queue) - 1) # exclude one that's being served

	print(max_queue_length)

if __name__ == "__main__":
	calc_longest_queue()
