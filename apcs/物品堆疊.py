# 某個自動化系統中有一個存取物品的子系統，該系統是將N個物品堆在一個垂直的貨架上，每個物品各佔一層。系統運作的方式如下：每次只會取用一個物品，取用時必須先將在其上方的物品貨架升高，取用後必須將該物品放回，然後將剛才升起的貨架降回原始位置，之後才會進行下一個物品的取用。
# 每一次升高某些物品所需要消耗的能量是以這些物品的總重來計算，在此我們忽略貨架的重量以及其他可能的消耗。現在有N個物品， 第i個物品的重量是w(i)而需要取用的次數為f(i)，我們需要決定如何擺放這些物品的順序來讓消耗的能量越小越好。舉例來說，有兩個物品w(1)=1、w(2)=2、f(1)=3、f(2)=4，也就是說物品1的重量是1需取用3次，物品2的重量是2需取用4次。我們有兩個可能的擺放順序(由上而下)：
#     (1,2)，也就是物品1放在上方，2在下方。那麼，取用1的時候不需要能量，而每次取用2的能量消耗是w(1)=1，因為2需取用f(2)=4次，所以消耗能量數為w(1)*f(2)=4。
#     (2,1)，也就是物品2放在1的上方。那麼，取用2的時候不需要能量，而每次取用1的能量消耗是w(2)=2，因為1需取用f(1)=3次，所以消耗能量數=w(2)*f(1)=6。
# 在所有可能的兩種擺放順序中，最少的能量是4，所以答案是4。再舉一例，若有三物品而w(1)=3、w(2)=4、w(3)=5、f(1)=1、f(2)=2、f(3)=3。假設由上而下以(3,2,1)的順序，此時能量計算方式如下：取用物品3不需要能量，取用物品2消耗w(3)*f(2)=10，取用物品1消耗(w(3)+w(2))*f(1)=9，總計能量為19。如果以(1,2,3)的順序，則消耗能量為3*2+(3+4)*3=27。事實上，我們一共有3!=6種可能的擺放順序，其中順序(3,2,1)可以得到最小消耗能量19。
# Input
# 輸入的第一行是物品件數N。
# 第二行有N個正整數，依序是各物品的重量w(1)、w(2)、...、w(N)，重量皆不超過1000且以一個空白間隔。
# 第三行有N個正整數，依序是各物品的取用次數f(1)、f(2)、...、f(N)，次數皆為1000以內的正整數，以一個空白間隔。
# Output
# 輸出最小能量消耗值，以換行結尾。
# 所求答案不會超過63個位元所能表示的正整數。
# Sample Input #1
# 2
# 20 10
# 1 1
# Sample Output #1
# 10
# Sample Input #2
# 3
# 3 4 5
# 1 2 3
# Sample Output #2
# 19

# import functools

# def main():
#     _ = int(input())
#     weights = list(map(int, input().split()))
#     freqs = list(map(int, input().split()))
#     items = list(zip(weights, freqs))

#     def cmp(a, b):
#         return a[0] * b[1] - b[0] * a[1]

#     items.sort(key=functools.cmp_to_key(cmp))

#     energy, weight = 0, 0
#     for w, f in items:
#         energy += weight * f
#         weight += w

#     print(energy)


# if __name__ == "__main__":
#     main()

# Solution 2: Optimized for memory as solution 1 failed 1 test case (total: 98% passed)
import functools


class Obj:
    def __init__(self, w=0, f=0):
        self.w = w
        self.f = f


def main():
    N = int(input())
    s = [Obj() for _ in range(100000)]  # Fixed size array

    # Read weights
    weights = list(map(int, input().split()))
    for i in range(N):
        s[i].w = weights[i]

    # Read frequencies
    freqs = list(map(int, input().split()))
    for i in range(N):
        s[i].f = freqs[i]

    def cmp(a, b):
        return a.w * b.f - b.w * a.f

    s_n = s[:N]  # Only sort the portion of the array we need
    s_n.sort(key=functools.cmp_to_key(cmp))

    energy, weight = 0, 0
    for i in range(N):
        energy += weight * s_n[i].f
        weight += s_n[i].w

    print(energy)


if __name__ == "__main__":
    main()
