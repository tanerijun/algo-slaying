# 去買飲料的時候，最怕遇到前面的客人一次購買很多杯飲料，如此一來，即使排隊人數很少，一樣要等很久。
# 有一天，你經過了一家飲料店，發現有N個人排隊要買飲料。不過，這家飲料店人手充足，一共有M個店員可以服務這些排隊的人潮。
# 為了公平起見，雖然店員很多，但是排隊只排成一列，避免在排很多列的情況下，每列前進的速度會不一樣。
# 另外，為了服務品質起見，這家店的店員必須遵守兩個規則：必須按照客人排隊順序服務客人，不能先服務排在後面的顧客，否則前面的客人可能會森77（而這是飲料店最不想看到的狀況）；另外，如果某個店員服務了某個客人，則該客人點的所有飲料都要由該店員製作，製作完成之後才能服務下一位客人。
# 你做了一下市場調查，詢問每位排隊的客人要買幾杯飲料。假如所有的店員製作飲料的速度都是每分鐘1杯，在遵守這些規則的前提下，請問服務完這些客人至少需要多久？

# Input
# 輸入第一行有兩個正整數N,M，分別代表排隊等待的客人數量，以及店員數量。
# 接下來會有N個以空白隔開的正整數，依序為每位排隊顧客要購買的飲料數量。
# 對於所有測資，N≦106,M≦104，每個客人要購買的飲料數不超過1000。
# 子任務(測資)	額外限制	分數
# 1(0~1)	 M=1	     7
# 2(0~3)	 M≦2	    16
# 3(4~6)	 N，M≦20	 9
# 4(4~9)	 N≦104	     7
# 5(4~13)	 N≦105	     8
# 6(0~17)	無限制	    53

# Output
# 輸出一行包含一個整數，代表服務完這些客人至少需要幾分鐘。

# Sample Input #1
# 5 2
# 1 5 2 1 1

# Sample Output #1
# 5

# Hint
# 假設初始時間為0，五個客人的飲料分別在時間點0, 0, 1, 3, 4開始製作（其中一位店員負責第二位客人，另外一位負責其他四位）；製作完成的時間分別是1, 5, 3, 4, 5。


# def main():
#     N, M = map(int, input().split())
#     orders = list(map(int, input().split()))
#     total_time = 0
#     staff_time = [0] * M  # track when each staff is availabe

#     for order in orders:
#         # get the soonest available staff
#         staff_idx = staff_time.index(min(staff_time))

#         # the staff will be in charge of the order
#         staff_time[staff_idx] += order

#         total_time = max(total_time, staff_time[staff_idx])

#     print(total_time)


# if __name__ == "__main__":
#     main()

### Priority Queue solution

import heapq


def main():
    N, M = map(int, input().split())
    orders = list(map(int, input().split()))
    total_time = 0

    # Initialize priority queue with (time_available, staff_index)
    staff_queue = [(0, i) for i in range(M)]
    heapq.heapify(staff_queue)

    for order in orders:
        # Get the soonest available staff
        time_available, staff_idx = heapq.heappop(staff_queue)

        finish_time = time_available + order

        total_time = max(total_time, finish_time)

        # Put staff back in pq with new available time
        heapq.heappush(staff_queue, (finish_time, staff_idx))

    print(total_time)


if __name__ == "__main__":
    main()
