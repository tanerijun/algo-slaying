# 一個具偶同位特性的布林矩陣中，每一列及每一欄加總結果必為偶數。例如下面的4x4矩陣，即具有偶同位特性：

# 1	    0	  1	    0	 sum=2
# 0	    0	  0	    0	 sum=0
# 1	    1	  1	    1	 sum=4
# 0	    1	  0	    1	 sum=2
# sum=2	sum=2 sum=2 sum=2

# 寫一個程式判斷輸入的矩陣是否具備偶同位性質，如果不具偶同位性質，請判斷是否能夠修改矩陣中的一個位元就讓矩陣具備偶同位性質，如果無法達成，則將矩陣歸類為corrupt

# Input
# 包含多筆測資，每筆測資第一列有一個整數 n (n < 100)，代表矩陣的大小。接下來有 n 列，每列包含 n 個整數(在此整數只有0和1)。
# 如果 n 為0時，代表測資結束。

# Output
# 針對每個矩陣，輸出一列結果。
# 如果矩陣具備偶同位性質，請輸出 OK
# 如果能夠修改矩陣中的一個位元就讓矩陣具備偶同位性質，請輸出Change bit (i,j)，其中 i 為該位元所在的列 j 為該位元所在的欄位其餘請輸出 Corrupt

# Sample Input #1
# 4
# 1 0 1 0
# 0 0 0 0
# 1 1 1 1
# 0 1 0 1
# 4
# 1 0 1 0
# 0 0 1 0
# 1 1 1 1
# 0 1 0 1
# 4
# 1 0 1 0
# 0 1 1 0
# 1 1 1 1
# 0 1 0 1
# 0
# Sample Output #1
# OK
# Change bit (2,3)
# Corrupt


def parse_lines(lines):
    matrix = []
    for line in lines:
        matrix.append(list(map(int, line.split(" "))))
    return matrix


def error_fixer():
    outputs = []

    while True:
        # End program
        line_count = int(input())
        if line_count == 0:
            break

        lines = []
        for _ in range(line_count):
            lines.append(input())

        matrix = parse_lines(lines)

        odd_row_idxs = []
        odd_col_idxs = []

        for i in range(line_count):
            sum = 0
            for j in range(line_count):
                sum += matrix[i][j]
            if sum % 2 != 0:
                odd_row_idxs.append(i)

        for i in range(line_count):
            sum = 0
            for j in range(line_count):
                sum += matrix[j][i]
            if sum % 2 != 0:
                odd_col_idxs.append(i)

        if len(odd_row_idxs) == 0 and len(odd_col_idxs) == 0:
            outputs.append("OK")
        elif len(odd_row_idxs) == 1 and len(odd_col_idxs) == 1:
            outputs.append(f"Change bit ({odd_row_idxs[0] + 1},{odd_col_idxs[0] + 1})") # plus 1 due to zero indexing
        else:
            outputs.append("Corrupt")

    for output in outputs:
        print(output)


if __name__ == "__main__":
    error_fixer()
