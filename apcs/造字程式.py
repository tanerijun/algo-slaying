# # j606. 2. 造字程式

# from doctest import OutputChecker


# 有一個長度K的的初始字串S，每個字元都是小寫的英文字母。
# 接下來有Q次的修改，每次的修改會把舊的字串重新排列成一個新的字串。
# 更具體來講，每次修改時會給一個1~K的排列P=[P1, P2, ..., Pk]，要將舊字串的第 的字元複製到新字串的第 個字元。
# 例子：
#     - 若舊字串是 "abac"，且 P=[4,1,3,2]，可以得到新字串 "bcaa"。
#     - 若舊字串是 "bcaa"，且 P=[1,2,3,4]，可以得到新字串 "bcaa"。
#     - 若舊字串是 "bcaa"，且 P=[2,3,4,1]，可以得到新字串 "abca"。

# 在Q的修改中，每次修改出來的新字串會被當成下一次修改中的舊字串，而第一次修改時使用的舊字串就是初始字串。

# 題目另外會給一個數字R，請依照下面定義的順序輸出R行，每行Q個字元
#     - 輸出操作 1 ~ Q的新字串的第1個字元
#     - 輸出操作 1 ~ Q的新字串的第2個字元
#     - ...
#     - 輸出操作 1 ~ Q的新字串的第R個字元

# Input
# 第一行有三個整數 K, Q, R
# 第二行是長度K的初始字串
# 接下來有Q行，每行有是一個1~K的排列

# Output
# 請依照題目敘述輸出RxQ個字元


# Sample Input #1
# 5 4 1
# abcde
# 2 1 3 5 4
# 5 1 2 4 3
# 4 1 2 3 5
# 3 1 4 5 2

# Sample Output #1
# bacd

# Sample Input #2
# 4 3 4
# abac
# 4 1 3 2
# 1 2 3 4
# 2 3 4 1

# Sample Output #2
# bba
# ccb
# aac
# aaa


# def solve_string_transformation(K, Q, R, initial_string, permutations):
#     # Initialize the result matrix
#     result = [[""] * Q for _ in range(R)]

#     # Initialize the current string
#     current_string = initial_string

#     # Process each permutation
#     for q in range(Q):
#         # Create a new string based on the current permutation
#         new_string = [""] * K
#         for i, p in enumerate(permutations[q]):
#             new_string[p - 1] = current_string[i]

#         # Update the result matrix
#         for r in range(min(R, K)):
#             result[r][q] = new_string[r]

#         # Update the current string for the next iteration
#         current_string = "".join(new_string)

#     # Return the result as a list of strings
#     return ["".join(row) for row in result]


# # Input processing
# K, Q, R = map(int, input().split())
# initial_string = input().strip()
# permutations = [list(map(int, input().split())) for _ in range(Q)]

# # Solve the problem
# output = solve_string_transformation(K, Q, R, initial_string, permutations)

# # Print the output
# for row in output:
#     print(row)


def main():
    K, Q, R = map(int, input().split())
    init_str = input().strip()
    P = [list(map(int, input().split())) for _ in range(Q)]

    results = [[""] * Q for _ in range(R)]
    current_str = init_str

    for q in range(Q):  # process each permutation
        new_str = [""] * K
        for i, p in enumerate(P[q]):
            new_str[p - 1] = current_str[i]

        for r in range(min(R, K)):
            results[r][q] = new_str[r]

        current_str = "".join(new_str)

    for res in results:
        print("".join(res))


if __name__ == "__main__":
    main()
