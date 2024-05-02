# 跑長編碼(Run-Length Coding)是一種常見的資料壓縮技術，特別適用於字串樣式重複頻率高的情況。其編碼格式為(重複樣式,重複次數)，例如一個二元字串 0000001111111001111 可編碼為 (0,6) (1,7) (0,2) (1,4)，因為樣式 0 重複了 6 次，而之後的樣式 1 則重複了 7 次。

# 寫一個程式來壓縮一個長位元串，並輸出壓縮比率(壓縮後位元個數除以原位元個數，四捨五入到整數百分比)。重複位元的長度用 3 個位元來表示(最大連續長度為 7)，放在重複位元的後面，形成一個 4 位元的碼字(code word)。

# Input
# 輸入資料中第一列為一整數n，代表接下來有n組測試資料。

# 第二列開始共有n列，每列輸入一長串連續的位元(長度小於 500)

# Output
# 輸出跑長編碼後的4位元碼字，可能是 ( 0, 連續 0 的長度) 或 ( 1, 連續 1 的長度)，兩個碼字之間用一個空格分開，最後是四捨五入的壓縮率。如果輸入不是一個2進制位元串，直接輸出-1。

# Sample Input #1
# 4
# 00010000000111111101111111
# 11111100000000000000111111111111110000
# 0011  1111100000101010
# HINET0800000123
# Sample Output #1
# 0011 1001 0111 1111 0001 1111 92%
# 1110 0111 0111 1111 1111 0100 63%
# -1
# -1


def rle(text):
    res = []

    i = 0
    while i < len(text):
        ch = text[i]
        if ch not in ["0", "1"]:  # immediately return -1 on non-binary encounter
            return ["-1"]

        j = i
        while j < len(text) and text[j] == ch and j - i < 7: # extend window when text is still the same, but max 7 spaces
            j += 1

        n_occurrences = j - i
        res.append(ch + bin(n_occurrences)[2:].zfill(3)) # format: [0|1][count_in_binary]
        i = j

    return res


def compressor():
    # Process input
    input_line_count = int(input())
    texts = []
    for _ in range(input_line_count):
        texts.append(input())

    for text in texts:
        compressed = rle(text)
        if compressed[0] == "-1":
            print("-1")
            continue

        compression_ratio = round((len(compressed) * 4 / len(text) * 100))  # in percent
        compression_ratio_str = str(compression_ratio) + "%"
        output = " ".join(compressed)
        print(output, compression_ratio_str)


if __name__ == "__main__":
    compressor()
