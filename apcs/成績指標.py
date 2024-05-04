# 成績指標

# 一次考試中，於所有及格學生中獲取最低分數者最為幸運，反之，於所有不及格同學中，獲取最高分數者，可以說是最為不幸，而此二種分數，可以視為成績指標。
# 請你設計一支程式，讀入全班成績(人數不固定)，請對所有分數進行排序，並分別找出不及格中最高分數，以及及格中最低分數。
# 當找不到最低及格分數，表示對於本次考試而言，這是一個不幸之班級，此時請你印出：「worst case」；反之，當找不到最高不及格分數時，請你印出「best case」。
# 註：假設及格分數為60，每筆測資皆為0~100間整數，且筆數未定。

# Input
# 第一行輸入學生人數，第二行為各學生分數(0~100間)，分數與分數之間以一個空白間格。每一筆測資的學生人數為1~20的整數。

# Output
# 每筆測資輸出三行。
# 第一行由小而大印出所有成績，兩數字之間以一個空白間格，最後一個數字後無空白；
# 第二行印出最高不及格分數，如果全數及格時，於此行印出best case；
# 第三行印出最低及格分數，當全數不及格時，於此行印出worst case。

# Sample Input #1
# 10
# 0 11 22 33 55 66 77 99 88 44
# Sample Output #1
# 0 11 22 33 44 55 66 77 88 99
# 55
# 66
# 範例一測資說明：不及格分數最高為 55，及格分數最低為 66。

# Sample Input #2
# 1
# 13
# Sample Output #2
# 13
# 13
# worst case
# 範例二測資說明：由於找不到最低及格分數，因此第三行須印出「worst case」。

# Sample Input #3
# 2
# 73 65
# Sample Output #3
# 65 73
# best case
# 65
# 範例三測資說明：由於找不到最高不及格分數，因此第二行須印出「best case」。

def find_highest_fail_index(scores):
    left = 0
    right = len(scores) - 1

    while left <= right:
        mid = (left + right) // 2
        if scores[mid] < 60:
            left = mid + 1
        else:
            right = mid - 1

    return right


def performance_indicator():
    n_students = int(input())
    scores = list(map(int, input().split()))
    sorted_scores = sorted(scores)

    highest_fail_index = find_highest_fail_index(sorted_scores)
    highest_fail = sorted_scores[highest_fail_index] if highest_fail_index >= 0 else "best case"
    lowest_pass = sorted_scores[highest_fail_index + 1] if highest_fail_index + 1 < len(scores) else "worst case"

    print(" ".join(map(str, sorted_scores)))
    print(highest_fail)
    print(lowest_pass)


if __name__ == "__main__":
    performance_indicator()
