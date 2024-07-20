# 為因應資訊化與數位化的發展趨勢，某市長想要在城市的一些服務點上提供無線網路服務，因此他委託電信公司架設無線基地台。某電信公司負責其中 N 個服務點，這 N個服務點位在一條筆直的大道上，它們的位置(座標)係以與該大道一端的距離 P[i]來表示，其中 i=0~N-1。由於設備訂製與維護的因素，每個基地台的服務範圍必須都一樣，當基地台架設後，與此基地台距離不超過 R (稱為基地台的半徑)的服務點都可以使用無線網路服務，也就是說每一個基地台可以服務的範圍是 D=2R(稱為基地台的直徑)。現在電信公司想要計算，如果要架設 K 個基地台，那麼基地台的最小直徑是多少才能使每個服務點都可以得到服務。
# 基地台架設的地點不一定要在服務點上，最佳的架設地點也不唯一，但本題只需要求最小直徑即可。以下是一個 N=5 的例子，五個服務點的座標分別是 1、2、5、7、8。


# 0    1    2    3    4    5    6    7    8    9
#      ▲    ▲              ▲         ▲    ▲


# 假設 K=1，最小的直徑是 7，基地台架設在座標 4.5 的位置，所有點與基地台的距離都在半徑 3.5 以內。假設 K=2，最小的直徑是 3，一個基地台服務座標 1 與 2 的點，另一個基地台服務另外三點。在 K=3 時，直徑只要 1 就足夠了。

# Input
# 輸入有兩行。
# 第一行是兩個正整數 N 與 K，以一個空白間格。
# 第二行 N 個非負整數P[0],P[1],....,P[N-1]表示 N 個服務點的位置，這些位置彼此之間以一個空白間格。
# 請注意，這 N 個位置並不保證相異也未經過排序。本題中，K<N 且所有座標是整數，因此，所求最小直徑必然是不小於 1 的整數。

# Output
# 輸出最小直徑，不要有任何多餘的字或空白並以換行結尾。

# Sample Input #1
# 5 2
# 5 1 2 8 7

# Sample Output #1
# 3

# Sample Input #2
# 5 1
# 7 5 1 2 8

# Sample Output #2
# 7


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()

    def can_cover(diameter):
        count = 1
        curr_end = P[0] + diameter  # position where coverage ends
        for pos in P[1:]:
            if pos > curr_end:  # every pos before curr_end are covered
                count += 1
                curr_end = pos + diameter
            if count > K:
                return False
        return True

    def find_min_diameter():
        # Set the lower bound to 1 (minimum possible diameter)
        # Set the upper bound to the maximum distance between any two points
        left, right = 1, P[-1] - P[0]
        while left < right:
            mid = (left + right) // 2
            if can_cover(mid):
                right = mid  # try lowering the diameter even more
            else:
                left = mid + 1

        return left

    res = find_min_diameter()
    print(res)


if __name__ == "__main__":
    main()
