# 給你n個正整數,你需要去找他們所有之中最大的一對GCD值 (greatest common divisor)

# Input
# 第一行為測資有幾組資料 N (1<N<100)
# 接下來的N行是第N組資料
# 每組資料都有M個數字 (1<M<100) 讓你去找其中的最大的一對GCD值

# Output
# 對於每組資料請輸出最大的一對GCD值

# Sample Input #1

# 3
# 10 20 30 40
# 7  5 12
# 125 15 25

# Sample Output #1

# 20
# 1
# 25

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def main():
    N = int(input())
    for _ in range(N):
        nums = list(map(int, input().split()))
        res = 0
        # Check all permutations
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = max(res, gcd(nums[i], nums[j]))

        print(res)

main()
