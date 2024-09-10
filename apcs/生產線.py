# 有n台機器排成一直線, 每一個機器都有一個數值t[i], 代表該台機器要產出一單位的資料需要t[i]單位的時間
# 接下來有m個工作要完成, 每一個工作都需要位置在l[i],r[i]的機器各生產出w[i]單位資料
# 現在你可以調換n台機器的順序, 目標是使得這m個工作做完的總時間要最小

# Input
# 先輸入兩個正整數n和m代表有n台機器和m個工作
# 接下來有m行, 每行有三個正整數l[i],r[i]和w[i]代表第i個工作需要編號從l[i]到r[i]的機器完成, 並且需要各產生出w[i]單位的資料
# 最後一行包含n個正整數t[1],t[2],...t[n]

# Output
# 輸出最小的總花費時間

# Sample Input #1
# 5 1
# 2 4 1
# 1 2 3 4 5

# Sample Output #1
# 6

# Sample Input #2
# 10 3
# 2 5 6
# 3 6 4
# 7 8 1
# 1 2 3 4 5 6 7 8 9 10

# Sample Output #2
# 117


# def main():
#     n, m = map(int, input().split())
#     jobs = [list(map(int, input().split())) for _ in range(m)]
#     machines = list(map(int, input().split()))

#     position_counts = [0] * n
#     for l, r, w in jobs:
#         for i in range(l - 1, r):
#             position_counts[i] += w

#     sorted_positions = sorted(range(n), key=lambda i: -position_counts[i])
#     sorted_machines = sorted(range(n), key=lambda i: machines[i])

#     optimal_arrangement = [0] * n
#     for i in range(n):  # assign fastest machine to most used pos
#         optimal_arrangement[sorted_positions[i]] = machines[sorted_machines[i]]

#     total_time = 0

#     for l, r, w in jobs:
#         job_time = sum(optimal_arrangement[i] * w for i in range(l - 1, r))
#         total_time += job_time

#     print(total_time)


# if __name__ == "__main__":
#     main()


# def main():
#     n, m = map(int, input().split())
#     jobs = [list(map(int, input().split())) for _ in range(m)]
#     machines = list(map(int, input().split()))

#     position_counts = [0] * n
#     for l, r, w in jobs:
#         for i in range(l - 1, r):
#             position_counts[i] += w

#     sorted_positions = sorted(range(n), key=lambda i: -position_counts[i])
#     sorted_machines = sorted(machines)

#     # optimal arrangement: the fastest machine in the most demanded position
#     optimal_arrangement = [0] * n
#     for i in range(n):
#         optimal_arrangement[sorted_positions[i]] = sorted_machines[i]

#     # compute prefix sums for the arranged machines
#     prefix_sum = [0] * (n + 1)
#     for i in range(n):
#         prefix_sum[i + 1] = prefix_sum[i] + optimal_arrangement[i]

#     total_time = 0
#     for l, r, w in jobs:
#         range_sum = prefix_sum[r] - prefix_sum[l - 1]
#         total_time += range_sum * w

#     print(total_time)


# if __name__ == "__main__":
#     main()


def main():
    n, m = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(m)]
    machines = list(map(int, input().split()))

    # difference array to record the cumulative weight updates
    diff = [0] * (n + 1)
    for l, r, w in jobs:
        diff[l - 1] += w
        if r < n:
            diff[r] -= w

    position_counts = [0] * n
    current_weight = 0
    for i in range(n):
        current_weight += diff[i]
        position_counts[i] = current_weight

    sorted_positions = sorted(range(n), key=lambda i: -position_counts[i])
    sorted_machines = sorted(machines)

    # optimal arrangement: assign fastest machines to most demanded positions
    optimal_arrangement = [0] * n
    for i in range(n):
        optimal_arrangement[sorted_positions[i]] = sorted_machines[i]

    # compute prefix sums for the arranged machines
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + optimal_arrangement[i]

    total_time = 0
    for l, r, w in jobs:
        range_sum = prefix_sum[r] - prefix_sum[l - 1]
        total_time += range_sum * w

    print(total_time)


if __name__ == "__main__":
    main()
