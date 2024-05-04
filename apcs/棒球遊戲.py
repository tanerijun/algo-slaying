# 謙謙最近迷上棒球，他想自己寫一個簡化的遊戲計分程式。這會讀入隊中每位球員的打擊結果，然後計算出球隊得分。
# 這是個簡化版的模擬，假設擊球員打擊結果只有以下情況：
# (1) 安打：以1B,2B,3B和HR 分別代表一壘打、二壘打、三壘打和全（四）壘打。
# (2) 出局：以 FO,GO和 SO表示。

# 這個簡化版的規則如下：
# (1) 球場上有四個壘包，稱為本壘、一壘、二壘、和三壘。
# (2) 站在本壘握著球棒打球的稱為「擊球員」，站在另外三個壘包的稱為「跑壘員」。
# (3) 當擊球員的打擊結果為「安打」時，場上球員（擊球員與跑壘員）可以移動；結果為 「出局」時，跑壘員不動，擊球員離場換下一位擊球員。
# (4) 球隊總共有九位球員，依序排列 。比賽開始由第1位開始打擊，當第 i 位球員打擊完畢後，由第 (i+1)位球員擔任擊球員。當第九位球員完畢後，則輪回第一位球員。
# (5) 當打出 K 壘打時，場上球員（擊球員和跑壘員）會前進 K 個壘包。從本壘前進一個壘包會移動到一壘，接著是二壘、三壘，最後回到本壘。
# (6) 每位球員回到本壘時可得 1分
# (7) 每達到三個出局數時，一、二和三壘就會清空（ 跑壘員都得離開） ，重新開始。

# Input
# 每組測試資料固定有十行。
# 第一到九行，依照球員順序，每一行代表位球員的打擊資訊。每一行開始有一個正整數 a (1≤a≤5)，代表球員總共打了 a 次。接下來有 a 個字串（均為兩個字元），依序代表每次打擊的結果。 資料之間均以一個空白字元隔開。球員的打擊資訊不會有錯誤也不會缺漏。
# 第十行有一個正整數 b (1≤b≤27) ，表示我們想要計算當總出局數累計到 b 時， 該球隊的得分。輸入的打擊資訊中至少包含b個出局。

# Output
# 計算在總計第b個出局數發生時的總得分，並將此得分輸出於一行。

# Sample Input #1
# 5 1B 1B FO GO 1B
# 5 1B 2B FO FO SO
# 4 SO HR SO 1B
# 4 FO FO FO HR
# 4 1B 1B 1B 1B
# 4 GO GO 3B GO
# 4 1B GO GO SO
# 4 SO GO 2B 2B
# 4 3B GO GO FO
# 3
# Sample Output #1
# 0

# Sample Input #2
# 5 1B 1B FO GO 1B
# 5 1B 2B FO FO SO
# 4 SO HR SO 1B
# 4 FO FO FO HR
# 4 1B 1B 1B 1B
# 4 GO GO 3B GO
# 4 1B GO GO SO
# 4 SO GO 2B 2B
# 4 3B GO GO FO
# 6
# Sample Output #2
# 5


def new_base():
    return [0 for _ in range(3)]  # represents base 1, 2, and 3. 0 = empty, 1 = filled


def parse_inputs(inputs):
    actions = []
    for input in inputs:
        action = input.split(" ")[1:]  # ignore first char (num of move a player made)
        actions.append(action)

    ordered_actions = []
    for j in range(len(actions[0])):  # first entry will be longest for sure
        for i in range(len(actions)):
            if j > len(actions[i]) - 1:
                break
            ordered_actions.append(actions[i][j])

    return ordered_actions


def parse_actions(actions):
    values = []
    for action in actions:
        if action not in ["1B", "2B", "3B", "HR"]:
            values.append(0)
        elif action == "HR":
            values.append(4)
        else:
            values.append(int(action[0]))  # first char represents base number
    return values


def baseball_game():
    inputs = []
    for _ in range(9):
        inputs.append(input())

    max_out_count = int(input())

    base = new_base()
    score, out_count = 0, 0
    actions = parse_inputs(inputs)
    values = parse_actions(actions)

    for value in values:
        if value > 0:
            # Advance the other players
            for i in range(len(base) - 1, -1, -1):
                if base[i] > 0:  # advance player if the spot is not empty
                    new_spot = i + value
                    if new_spot >= len(base):  # reached the base
                        score += 1
                    else:
                        base[new_spot] += 1
                    base[i] -= 1

            # Advance the batter
            if value > len(base):
                score += 1
            else:
                base[value - 1] += 1
        else:
            out_count += 1
            if out_count == max_out_count:
                break
            if out_count % 3 == 0:  # empty field every 3 outs
                base = new_base()

    print(score)


if __name__ == "__main__":
    baseball_game()
