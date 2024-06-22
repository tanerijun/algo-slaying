# 在電腦科學中，二分搜尋（binary search），也稱折半搜尋（half-interval search）、對數搜尋（logarithmic search），是一種在有序陣列中尋找某一特定元素的搜尋演算法。
# 搜尋過程從陣列的中間元素開始，如果中間元素正好是要尋找的元素，則搜尋過程結束；如果某一特定元素大於或者小於中間元素，則在陣列大於或小於中間元素的那一半中尋找，而且跟開始一樣從中間元素開始比較。如果在某一步驟陣列為空，則代表找不到。這種搜尋演算法每一次比較都使搜尋範圍縮小一半。

# Input
# 第一列包含一個整數 n (0 < n ≤ 10000)
# 第二列包含 n 個 相異且已排序 的整數
# 第三列有一個整數 x，代表要搜尋的數字

# Output
# 請找出整數 x 在陣列中的編號，並輸出以二分搜尋法搜尋所需次數
# 如果陣列中不包含整數 x，則輸出 "not found" 及搜尋所需次數

# Sample Input #1
# 6
# 1 3 4 6 7 8
# 7
# Sample Output #1
# 4 2

# Sample Input #2
# 6
# 1 3 4 6 7 8
# 9
# Sample Output #2
# not found 3


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    iteration_count = 0
    target_index = -1
    l, r = 0, len(nums) - 1
    while l <= r:
        iteration_count += 1
        mid = (r + l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            target_index = mid
            break

    print("not found" if target_index == -1 else target_index, iteration_count)


if __name__ == "__main__":
    main()
