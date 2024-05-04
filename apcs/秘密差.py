# 將一個十進位正整數的奇數位數的和稱為A，偶數位數的和稱為B，則A與B的絕對差值|A－B|稱為這個正整數的秘密差。

# 例如：263541的奇數位數的和A = 6+5+1 = 12，偶數位數的和B = 2+3+4 = 9，所以263541的秘密差是|12－9|= 3。

# 給定一個十進位正整數X，請找出X的秘密差。

# Input
# 輸入為一行含有一個十進位表示法的正整數X，之後是一個換行字元。

# Output
# 請輸出X的秘密差Y(以十進位表示法輸出)，以換行字元結尾。

# Sample Input #1
# 263541
# Sample Output #1
# 3

# Sample Input #2
# 131
# Sample Output #2
# 1


def secret_difference():
    num_str = input()
    A = 0  # even
    B = 0  # odd

    for n in num_str[1::2]:
        A += int(n)

    for n in num_str[::2]:
        B += int(n)

    res = abs(A - B)

    # Output
    print(res)


if __name__ == "__main__":
    secret_difference()
