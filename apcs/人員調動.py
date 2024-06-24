# 某學校人事部門為了整體學校運作效能並預防人員在同一個單位待太久可能衍伸弊端的狀況發生，會於年度結束之前調查校內各單位人員是否有異動意願，並據以作下個年度人員調動依據，為了維持各單位人力平衡，規定每一個人限填寫一項異動要求，而異動要被允許只有在你想去的單位也剛好有人想到你的單位，如此兩人互調，異動方可完成，請幫該校人事室寫一程式，根據今年本校人員異動申請資料，計算出有多少對的人員可以異動？

# Input
# 第一列為一個整數N(0 < N ≦ 100)，代表測試資料有幾組。
# 接下來的每一組測試資料的第1列有一個整數 M(0 < M ≦ 1000)，代表提出申請的員工數量，
# 接下的M列，每一列有二個以空白隔開的整數 a, b (0 < a, b ≤ 1000)，分別代表申請者原單位代碼及想去的單位代碼，之後每一組測試資料安排方式依此類推。

# Output
# 對於每一組測試資料，請輸出有多少對的人員可以異動，若沒有任何符合異動條件的組別則輸出0。

# Sample Input #1
# 2
# 7
# 1 2
# 35 66
# 100 500
# 2 1
# 2 3
# 500 100
# 3 2
# 3
# 100 200
# 200 400
# 400 1

# Sample Output #1
# 3
# 0


def main():
    dataset_count = int(input())
    datasets = []
    for _ in range(dataset_count):
        dataset = []
        dataset_length = int(input())
        for _ in range(dataset_length):
            a, b = map(int, input().split())
            dataset.append((a, b))
        datasets.append(dataset)

    res = []
    for dataset in datasets:
        count = 0
        desire_map = {}

        for a, b in dataset:
            if (b, a) in desire_map and desire_map[(b, a)] > 0:
                count += 1
                desire_map[(b, a)] -= 1
            else:
                desire_map[(a, b)] = desire_map.get((a, b), 0) + 1

        res.append(count)

    for result in res:
        print(result)


if __name__ == "__main__":
    main()
