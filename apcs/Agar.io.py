# 《Agar.io》是 一款大型多人線上遊戲。在遊戲中玩家控制一個在培養皿地圖的細胞，目的是為了獲得儘可能多的質量而儘可能不被更大的細胞吞噬。
# 在遊戲中，玩家開始時會得到一個質量固定為10的小球。基本上就是大球吃小球的遊戲，由於小球速度永遠比大球來的快，所以大球要利用空白鍵分裂才比較容易吃掉小球，但分裂的風險很高，有可能分裂前無法吃掉你的敵人就變成能吞掉你。而W鍵主要是用來餵鋸齒球，使鋸齒球分裂出去攻擊敵人。如果對某方向鋸齒球餵，則鋸齒球會往該方向分出一顆鋸齒球。當球越來越大時，它質量縮小的速度也會越來越快，所以必須要繼續進食才能維持及增加質量。
# 現在有N個玩家，想請問你算出在一陣大亂鬥之後，最大的那顆細胞包含了哪些細胞的殘骸。注意，本遊戲中被吃掉之後就不能復活了。

# Input
# 每組測試資料第一行有兩個正整數N, M (0 ≦ M < N ≦ 10000)，代表遊戲一開始時有N個細胞，遊戲之中有M次互相吞噬的行為。
# 接下來M行每行各有兩個正整數A, B (0 < A, B ≦10000)，描述此次是A與B互吃，測試資料保證 A 與 B 當時一定還沒有被其他細胞吞噬，但不一定誰大誰小，若兩者大小相同，則前者吞噬後者。
# Output
# 每組測試資料輸出兩行，第一行只有一個正整數X代表最大的細胞編號，第二行則是列出包含在X中所有細胞的編號 (包括自己)，由小而大排序。保證最大的細胞只有一個。

# Sample Input #1
# 6 4
# 6 1
# 3 4
# 6 2
# 3 6

# Sample Output #1
# 6
# 1 2 3 4 6


def main():
    N, M = map(int, input().split())
    state = [set() for _ in range(N + 1)]
    biggest = 1

    for i in range(1, N + 1):
        state[i].add(i)

    for _ in range(M):
        a, b = map(int, input().split())
        # Ensure the larger set absorbs the smaller set
        if len(state[a]) < len(state[b]):
            a, b = b, a

        state[a].update(state[b])  # a eats b
        # b is dead, so if a is eaten going forward, it's b that's eaten
        state[b] = state[a]

        if len(state[a]) >= len(state[biggest]):
            biggest = a

    print(biggest)
    print(" ".join(map(str, sorted(state[biggest]))))


if __name__ == "__main__":
    main()
