# Josephus是一位猶太歷史學家，在他的書中曾記載一段故事：

# 他和40個士兵被羅馬人困在一個洞窟中，一群人為了不被俘虜決定集體自殺，然而Josephus與另外一個人其實並不贊成，於是Josephus建議41個人排成圓圈，由第1個人開始報數，每報數到3的人就必須自殺，然後由下一個重新報數，直到所有人都自殺身亡為止。
# Josephus與不想自殺的那個人分別排在第16個與第31個位置，於是順利存活

# Input
# 輸入包含一個正整數 n 代表洞窟內總人數，一個正整數 m 代表每次報數到 m 的人必須自殺

# Output
# 在不知道有沒有其他人也同樣不想自殺的狀況下，輸出 Josephus 應該站在那個位置才能保命

# Sample Input #1
# 41 3
# Sample Output #1
# 31

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def solve_joshephus_problem():
	n, m = map(int, input().split())

	# Build linked list
	dummy = Node(-1)
	cur = dummy
	for i in range(1, n + 1):
		node = Node(i)
		cur.next = node
		cur = cur.next

	# Connect the tail and head to form a circular linked list
	cur.next = dummy.next

	# Start counting
	alive = n
	while (alive > 1):
		# Stop before the person that will suicide this turn
		for _ in range(m - 1):
			cur = cur.next

		# Delete the person who suicided
		cur.next = cur.next.next
		alive -= 1

	# The spot of the one who survived in the end is the spot Joshepus needs
	print(cur.val)

if __name__ == "__main__":
	solve_joshephus_problem()
