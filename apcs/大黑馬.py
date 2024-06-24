# 在某個校際球賽中，兩隊對決時每隊各派出奇數(2K+1)位選手進行 2K+1 場單打（不可重覆），贏得 K+1 場或以上的隊伍勝出。每位選手的實力以 BP 積分來表示，每場單打時積分較高的選手一定獲勝。然而因為賽程的安排，有時實力組合較強的一隊未必能勝出， 例如 A 隊有積分為 100, 80, 60 的三位選手，依序遭遇 B 隊積分為 90, 70, 50 的選手，將以 3：0 戰績獲勝， 但若依序遭遇 B 隊積分為 50, 90, 70 的選手，則反而將以 1：2 戰績落敗。
# 主辦單位將各隊選手的 BP 積分加總，依序決定各隊的種子順序，總積分最高的為第一種子。為了簡化問題，我們排除總積分相同的情況。而兩位 BP 積分相同的選手對決時， 則該場單打由來自總積分較高的隊伍獲勝。
# 然而，在實際賽程中，選手的表現偶有異常(突出或失誤)的表現，導致個別的實力(BP 積分)突然上升或下降，這些異常的表現也必須列入考慮。例如在下列的範例中，第三種子隊伍表現突出時，即可能擊敗其他兩隊。
# 某校的球隊是著名的黑馬，他們選手實力組合未必最強，但是卻經常意外擊敗實力組合堅強的隊伍。也就是說，他們雖然種子順序不高，卻經常爆出冷門，打敗種子順序超前 許多的隊伍。請找出今年參賽的隊伍中，可能成為今年冠軍的最大黑馬。也就是，在有機會擊敗所有對手的隊伍中，且不論機率多低，總積分最少的一隊(也就是種子順序數值最大的一隊)。
# Input
# 第一行輸入 K 和 N，以空白分開，代表每隊有 2K+1 位選手，參賽隊伍數為 N。
# 第二行開始有 N 行，每行有 1 + 3 * (2K + 1)個整數 S, P1, P2, …, P2K+1, U1, U2, …,U2K+1, L1, L2, …, L2K+1，中間以空白區隔，表示種子順序 S 的隊伍由積分 P1, P2, …, P2k+1 的 2K+1 位 選手組成，為了簡化資料輸入的問題，P1, P2, …, P2k+1 由大至小排列，也就是 P1 ≧ P2 ≧ … ≧ P2K+1，而這些選手表現突出時，實力相當於 U1, U2, …, U2K+1，但是表現失常時，實力則 相當於 L1, L2, …, L2K+1，且 Ui ≧ Pi ≧ Li。為了簡化問題，U1 ≧ U2 ≧ …  ≧ U2K+1 和 L1  ≧ L2 ≧ … ≧ L2K+1 也一定成立。
# Output
# 每筆測試資料輸出一行，包含兩個數字 S1, S2，中間以空白分開，代表若每位選手都無異常表現時，大黑馬是種子順序 S1 的隊伍，但若考慮每位選手各種可能的異常表現時， 大黑馬是種子順序 S2 的隊伍。
# Sample Input #1
# 1 3
# 1 100 80 60 100 80 60 100 80 60
# 2 90 70 50 100 80 60 90 70 50
# 3 80 60 40 100 80 60 70 50 30
# Sample Output #1
# 2 3


def can_beat_all_teams(team_index, teams, k, consider_anomalies=False):
    for opponent_index in range(len(teams)):
        if opponent_index == team_index:
            continue

        player_index = 0
        for opponent_player in range(2 * k + 1):
            performance_index = 1 if consider_anomalies else 0
            opp_performance_index = 2 if consider_anomalies else 0

            if player_index <= 2 * k and (
                teams[team_index]["performances"][player_index][performance_index]
                > teams[opponent_index]["performances"][opponent_player][
                    opp_performance_index
                ]
                or (
                    teams[team_index]["performances"][player_index][performance_index]
                    == teams[opponent_index]["performances"][opponent_player][
                        opp_performance_index
                    ]
                    and teams[team_index]["seed"] < teams[opponent_index]["seed"]
                )
            ):
                player_index += 1

        if player_index <= k:
            return False
    return True


def find_biggest_underdog(teams, k, consider_anomalies):
    biggest_underdog = 0
    for i in range(len(teams)):
        if can_beat_all_teams(i, teams, k, consider_anomalies):
            if teams[i]["seed"] > teams[biggest_underdog]["seed"]:
                biggest_underdog = i
    return teams[biggest_underdog]["seed"]


def main():
    k, n = map(int, input().split())
    teams = []

    for seed in range(1, n + 1):
        data = list(map(int, input().split()))
        team = {
            "seed": seed,
            "performances": [
                [data[1 + i], data[1 + (2 * k + 1) + i], data[1 + 2 * (2 * k + 1) + i]]
                for i in range(2 * k + 1)
            ],
        }
        teams.append(team)

    normal_underdog = find_biggest_underdog(teams, k, False)
    anomaly_underdog = find_biggest_underdog(teams, k, True)

    print(f"{normal_underdog} {anomaly_underdog}")


if __name__ == "__main__":
    main()
