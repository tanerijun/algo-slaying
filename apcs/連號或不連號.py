# 生物學家發現，與特定功能相關的一群基因在基因序列上的位置通常十分靠近，因此在不同的基因序列中如果都看見相同基因構成的連續片段 (順序不重要)，這些基因構成的集合就被認為是有意義的，稱為基因群 (gene cluster)。例如: 如果在一條基因序列上看到一個片段內容為 (a,b,c,d)，同時在另外一條基因序列上看到一個片段內容為 (d,b,a,c)，那麼 {a,b,c,d} 就構成一組基因群。
# 找出基因群並不是一件容易的工作，有一個計算生物學家想到一個聰明的方法來簡化這個問題。經過他的簡化後，基因群辨識的主要工作會被轉換成: 輸入一個由相異正整數組成的序列 S，然後判斷 S 的內容是否構成連續的一串整數。例如: S=(2,5,3,4) 的內容構成連續的一串整數 2,3,4,5；但是 S=(2,6,3,4) 的內容並不構成連續的一串整數 (缺了 5)。給定一個數字所構成的序列，請撰寫一個程式來判斷這個序列中的數字是否構成連續的一串整數。

# Input
# 測試資料是由一行的數字所構成 (數字間以一個以上的空白隔開)，第一個數字 n 表示所給定數字序列的長度，1<n≤100，接下來會有 n 個相異的正整數 mi，1≤i≤n 且 1≤mi≤1000，表示數字序列的內容。
# Output
# 輸出一行，如果此序列中的數字構成連續的一串整數，請輸出: a b yes；不行則輸出: a b no，其中 a 和 b 分別代表序列中所有數字的最小值與最大值。a 和 b 之間以及 b 和 yes/no 之間，請以剛好一個空白隔開。(yes/no 請用小寫)
# Sample Input #1
# 第一子題 輸入範例1
# 2  6  5
# 第一子題 輸入範例 2
# 2 5 7
# Sample Output #1
# 第一子題 輸出範例1
# 5  6  yes
# 第一子題  輸出範例2
# 5  7  no
# Sample Input #2
# 第二子題 輸入範例1
# 3 9 8 7
# 第二子題 輸入範例2
# 3 10 9 7
# Sample Output #2
# 第二子題 輸出範例1
# 7 9 yes
# 第二子題 輸出範例2
# 7 10 no
# Sample Input #3
# 第三子題 輸入範例1
# 5 2 3 4 5 6
# 第三子題 輸入範例2
# 5 2 3 4 5 7
# Sample Output #3
# 第三子題 輸出範例1
# 2 6 yes
# 第三子題 輸出範例2
# 2 7 no

import sys


# Solution 1:
# Time complexity: O(nlog(n))
# Space complexity: O(1)
def is_consecutive(nums):
    for i in range(len(nums)):
        if nums[i] != nums[0] + i:
            return False
    return True


def main():
    input = sys.stdin.read
    valid_input = list(map(lambda x: x.split(), input().split("\n")))
    for line in valid_input:
        data = list(map(int, line))
        n, nums = data[0], data[1:]
        nums.sort()
        print(f"{nums[0]} {nums[n - 1]} {'yes' if is_consecutive(nums) else 'no'}")


if __name__ == "__main__":
    main()
