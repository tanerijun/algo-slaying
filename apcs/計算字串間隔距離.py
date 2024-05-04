# 給定一個由大小寫英文字母所組成的字串以及一個英文字母，請輸出字母在字串中出現的間隔距離。

# Input
# 第一行為一個由大小寫字母所組成的長字串，字串長度為n(2≤n≤100)。
# 第二行為一個英文字母，代表要計算間隔距離的字母，且該字母在長字串中必至少不分大小寫地出現兩次(含)以上。

# Output
# 不分大小寫，列出該字母在此長字串中出現的間隔距離（距離間以一個空白字元分開）。

# Sample Input #1
# ABCDAAEFeDaBDCBCBcBCbCBBd
# A
# Sample Output #1
# 4 1 5


def string_distance_calculator():
    string = input().lower()
    char = input().lower()

    outputs = []

    i = 0
    while i < len(string):
        if string[i] == char:
            # Extend window
            j = i + 1
            while j < len(string) and string[j] != char:
                j += 1

            if j < len(string):
                outputs.append(str(j - i))

            i = j
        else:
            i += 1

    print(" ".join(outputs))


if __name__ == "__main__":
    string_distance_calculator()
