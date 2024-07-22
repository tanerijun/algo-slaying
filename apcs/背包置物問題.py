# 小明每天上學會背著一個後背包上學，為了避免背包太重，他的後背包裡最多只會放3本參考書。每天老師會指定上課需要用的一本參考書，而且學校的抽屜沒有空間讓小明把參考書放在學校，所以小明上課當天需要用的那本參考書必須在背包內，帶到學校去。小明很不喜歡整理背包，所以如果背包還沒滿，他就直接把當天需要的參考書放進背包去。如果背包滿了，他就會從背包裡拿出一本參考書，再放進當天需要用的參考書。
# 為了減少小明要從背包拿出參考書再放入參考書的動作，請根據老師所給接下來每天要用到的參考書，幫小明判斷每天要從背包選哪一本參考書拿出來，能使他需要拿出參考書再放進去的動作達到最少次。
# 舉例說明: 參考書的編號從1到5，每天上課需要用的參考書編號序列如下:
# 5, 1, 2, 3, 1, 4, 1, 5, 3, 4, 1, 4, 3, 2, 1, 2, 5, 1, 2, 1
# 最佳的放置順序如下:
# Day 1    Day 2    Day 3    Day 4    Day 5    Day 6    Day 7    Day8     Day 9    Day 10
# 放5      放1        放2      取2      不動       取3      不動      不動      取5      不動
# 放3                放4                         放3
# Day 11   Day 12   Day 13   Day 14   Day 15   Day 16   Day 17   Day 18   Day 19   Day 20
# 不動      不動      不動      取3      不動      不動      取4      不動     不動     不動
# 放2                         放5
# 這樣需要拿出參考書再放進去的動作只有5次。

# Input
# 1) 第一行為一個正整數n (1≦n≦20)，代表共有n本參考書，編號從1到n。
# 2) 第二行有m個從1到n的正整數(1≦m≦30)，以空白區分，表示每天上課需要用的參考書編號序列。
# 3) 第三行為一個正整數k (1≦k≦10)，代表小明背包最多只會放k本參考書。

# Output
# 1) 輸出一個數字，代表需要拿出參考書再放進去的最少次數。

# Sample Input #1
# 5
# 5 1 2 3 1 4 1 5 3 4 1 4 3 2 1 2 5 1 2 1
# 3

# Sample Output #1
# 5

# Sample Input #2
# 4
# 1 2 3 1 3 2
# 2

# Sample Output #2
# 2


def check_last_use(book_list, search_array):
    last_use = -1
    res = None
    for book in book_list:
        try:
            day_until_use = search_array.index(book)
            if day_until_use > last_use:
                last_use = day_until_use
                res = book
        except ValueError:
            # Book not in search_array, consider it as infinitely far
            return book
    return res


def main():
    N = int(input())
    books = list(map(int, input().split()))
    capacity = int(input())

    backpack = set()
    swap_count = 0

    for i, book in enumerate(books):
        if book in backpack:
            continue
        if len(backpack) < capacity:
            backpack.add(book)
        else:
            to_remove = check_last_use(backpack, books[i + 1 :])
            backpack.remove(to_remove)
            backpack.add(book)
            swap_count += 1

    print(swap_count)


if __name__ == "__main__":
    main()
