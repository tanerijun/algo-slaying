# 李伯伯年紀很大了，常常記不清楚自己的小孩什麼時候會回來老家看看他。而且每個小孩都事業有成，非常忙碌，像大兒子每15天回老家一趟、大女兒住比較近，可以每3天回來一趟。李伯伯希望有人可以幫幫他，算出什麼時候他的小孩們會一起回來看他。

# Input
# 第一行是李伯伯總共有N個小孩。

# 第二行則有N個數字代表小孩個別回家的時間，每個數字以空格隔開。

# 第三行是最近一次全部小孩一起回家的日期，格式為YYYY/MM/DD。

# Output
# 共一行。輸出下次一起回家的日期，日期格式為YYYY/MM/DD。

# Sample Input #1
# 4
# 4 5 12 21
# 2015/10/10
# Sample Output #1
# 2016/12/03

from functools import reduce
import math
import datetime

def lcm(a, b):
	return (a * b) // math.gcd(a, b)

def date_after_days(before_date, n):
	date_format = "%Y/%m/%d"
	before = datetime.datetime.strptime(before_date, date_format)
	after = before + datetime.timedelta(days=n)
	return after.strftime(date_format)

if __name__ == "__main__":
	n = int(input())
	intervals = map(int, input().split())
	last_visit_date = input()

	visit_together_interval = reduce(lcm, intervals)
	print(date_after_days(last_visit_date, visit_together_interval))
