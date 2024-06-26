# 寫一支程式找出兩個不重複且由 0 ~ 9 組成的五位數，使得第一個數字除以第二個數字剛好等於 N(2 ≦ N ≦ 79)，換而言之：
# abcde / fghij = N
# 其中 a ~ j 每個英文字母代表 0 ~ 9 之間不同的數字，第一位數可以為0
# Input
# 輸入包含許多筆待測資料，每列代表一筆待測資料，每筆待測資料包含一個正整數Ｎ，Ｎ為０時代表輸入結束。
# Output
# 針對每筆測試資料由小到大輸出每一對符合條件的數。如果找不到符合條件的數對，則輸出 "There are no solutions for N."
# 每筆測試資料間必須空一列。
# Sample Input #1
# 61
# 62
# 0
# Sample Output #1
# There are no solutions for 61.
# 79546 / 01283 = 62
# 94736 / 01528 = 62

from itertools import permutations


# TLE
def find_solutions(N):
    solutions = []
    digits = "0123456789"

    for perm in permutations(digits, 10):
        abcde = int("".join(perm[:5]))
        fghij = int("".join(perm[5:]))

        if fghij != 0 and abcde / fghij == N:
            solutions.append((abcde, fghij))

    return sorted(solutions)


# TLE
def find_solutions2(N):
    solutions = []

    for abcde in range(10000, 100000):
        if len(set(str(abcde))) != 5:  # all numbers should be unique
            continue

        fghij = abcde // N
        fghij_str = f"{fghij:05d}"  # str ver needed to preserve zero, ex: 01234

        if len(fghij_str) != 5:  # all numbers should be unique
            continue

        if abcde / N == fghij and len(set(fghij_str)) == 5:
            # Check if all digits are unique in abcdefghij
            if len(set(str(abcde) + fghij_str)) == 10:
                solutions.append((abcde, fghij))

    return sorted(solutions)


# TLE
def find_solutions3(N):
    solutions = []
    digits = "0123456789"

    for perm in permutations(digits):
        # Extract 'abcde' from the first 5 digits of the permutation
        abcde_str = "".join(perm[:5])
        abcde = int(abcde_str)

        fghij = abcde * N
        # Break if fghij is more than 5 digits
        if fghij > 98765:
            break

        fghij_str = f"{fghij:05d}"  # ensure 5 digits with leading zeros

        # Check if fghij is a 5-digit number
        if len(fghij_str) == 5:
            # Check if sorted fghij_str matches the last 5 digits of the permutation
            if sorted(fghij_str) == list(perm[5:]):
                solutions.append((fghij, abcde))

    return sorted(solutions)


def main():
    while True:
        N = int(input())
        if N == 0:
            break

        solutions = find_solutions3(N)

        if not solutions:
            print(f"There are no solutions for {N}.")
        else:
            for abcde, fghij in solutions:
                print(f"{abcde:05d} / {fghij:05d} = {N}")

        print()  # Empty line between test cases


if __name__ == "__main__":
    main()
