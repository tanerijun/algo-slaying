# 很多航空公司都會出售一種聯票，要求從起始站搭乘，上飛機時繳聯票，可以在中途任何一站下飛機。譬如，假設你要使用一張「城市1 →城市2→城市3」的聯票，你不能用來只從城市2飛到城市3（因為必須從起始站搭乘），也不能先從城市1飛到城市2，再用其他聯票飛到其他城市玩，回到城市2後再用原來的聯票飛到城市3（因為聯票已經上繳）。因此，你只能從聯票上的起始站開始你的旅程。
# 這裡有一個例子，假設有三種聯票，每種票的情況如下所示：
# 聯票1：城市1 →城市3 →城市4，票價225美元
# 聯票2：城市1 →城市2，票價200美元
# 聯票3：城市2 →城市3，票價50美元
# 你想從城市1飛到城市3，有兩種方法可以選擇。買聯票1，只飛第一段；或者買聯票2和3，透過城市2中轉。顯然第一種方法比較省錢，雖然浪費了一段（沒有使用城市3 →城市4）。
# 現在你的手邊有各種聯票的資訊，以及一個行程單，你的任務是買一些聯票，使得總花費最小（同一種聯票可以買多張）。在此保證輸入的行程單總是可行的。另外，行程單上的城市必須按順序到達，但中間可以經過一些中轉城市。

# Input
# 輸入資料的第一行為一個正整數 n (1 ≤ n ≤ 20)，即聯票的種類數。
# 以下 n 行每航為一個聯票的資訊，其中第一個整數為聯票的價格（票價為 €1 ~ €10,000），然後是聯票上城市的數目（為2到20）以及這些城市的編號（按順序列出）。
# 接下來為一個行程單的資訊，其中第一個正整數為行程單上的城市數目k（包括起始城市，2 ≤ k ≤ 10），以及這些城市的編號（按順序列出）。
# 聯票或行程單上的相鄰城市保證不同。聯票都從1開始編號。

# Output
# 輸出最小花費和對應的方案的其中一組解即可。

# Sample Input #1
# 3
# 100 2 2 4
# 100 3 1 4 3
# 200 3 1 2 3
# 3 1 2 4

# Sample Output #1
# Cost = 300, Tickets used: 3, 1

# Sample Input #2
# 3
# 100 2 2 4
# 100 3 1 4 3
# 200 3 1 2 3
# 3 1 4 3

# Sample Output #2
# Cost = 100, Tickets used: 2


from collections import defaultdict, namedtuple
import heapq

Ticket = namedtuple("Ticket", ["id", "cost", "next_cities"])
Node = namedtuple("Node", ["cost", "cur_pos", "visit_pos", "used_tickets"])


def main():
    n = int(input())
    tickets = defaultdict(list)
    for i in range(1, n + 1):
        cost, n_cities, *cities = list(map(int, input().split()))
        tickets[cities[0]].append(Ticket(i, cost, cities[1:]))

    len_itinerary, *itinerary = map(int, input().split())

    # initialize pq with tickets starting from first city
    pq = []
    for ticket in tickets[itinerary[0]]:
        p = 0
        for city in ticket.next_cities:
            if p + 1 < len_itinerary and city == itinerary[p + 1]:
                p += 1
            heapq.heappush(pq, Node(ticket.cost, city, p, [ticket.id]))

    while pq:
        cur = heapq.heappop(pq)
        if cur.visit_pos == len_itinerary - 1:  # reached last city in itinerary
            print(
                f"Cost = {cur.cost}, Tickets used: {', '.join(map(str, cur.used_tickets))}"
            )
            return

        # explore tickets from current city
        for ticket in tickets[cur.cur_pos]:
            used_tickets = cur.used_tickets + [ticket.id]
            p = cur.visit_pos
            for city in ticket.next_cities:
                if p + 1 < len_itinerary and city == itinerary[p + 1]:
                    p += 1
                heapq.heappush(pq, Node(cur.cost + ticket.cost, city, p, used_tickets))

    print("No valid path")  # shouldn't happen


if __name__ == "__main__":
    main()
