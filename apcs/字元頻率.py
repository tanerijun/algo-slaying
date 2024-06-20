# 給你一列文字，請你找出各字元出現的次數，且保證不包含ASCII 32之前的字元或128之後的字元

# Input
# 每筆測試資料一列。每列最大長度為1000
# Output
# 對每一列輸入，請輸出各字元的ASCII值及其出現的次數。請根據出現的次數由小到大輸出。如果有2個以上的字元有相同的次數，則ASCII值較大的先輸出。 測試資料間請空一列，參考Sample Output

# Sample Input #1
# AAABBC
# 122333
# Sample Output #1
# 67 1
# 66 2
# 65 3

# 49 1
# 50 2
# 51 3

import sys


def generate_frequency_map(s):
    freq_map = {}
    for ch in s:
        freq_map[ord(ch)] = freq_map.get(ord(ch), 0) + 1
    return freq_map


def sort_by_frequency_and_ascii(m):
    # Sort by frequency in ascending order,
    # then sort by ASCII value in descending order
    return sorted(m.items(), key=lambda entry: (entry[1], -entry[0]))


def main():
    input = sys.stdin.read
    data = input().strip().split("\n")

    maps = []
    for tc in data:
        maps.append(generate_frequency_map(tc))

    results = list(map(sort_by_frequency_and_ascii, maps))
    for i, res in enumerate(results):
        for k, v in res:
            print(k, v)
        if i < len(results) - 1:  # don't print a newline after last result
            print()


if __name__ == "__main__":
    main()
