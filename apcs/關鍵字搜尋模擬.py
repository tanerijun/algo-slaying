# 搜尋引擎其實主要在做兩件事情，分別是利用軟體爬行網站內容與依搜尋到的關鍵字建立網站索引，使用網頁相關性去排序這些搜尋結果網頁，再提供搜尋引擎演算法認為最相關的結果列表給想要透過搜尋取得答案的人。
# 假設每一個文件有文件編號(每一文件不重複，且已由低到高的順序排列)，和至少一個不同的關鍵字。當使用者輸入查詢的一個或多個關鍵字時，需要於系統所記錄的所有文件中找出搜尋的關鍵字與文件關鍵字最相關的文件，提供給使用者。
# 然而關鍵字並不一定完全符合，可能有不同長度(大於等於1)的部份且連續的子字串相同，此相同的部分可以代表此文件的相關性，可以提供部分的參考。例如查詢關鍵字BBB 與文件關鍵字ABC，其中有長度為1的子字串B相符，代表可以提供1/3的參考價值。例如查詢關鍵字BC 與文件關鍵字ABC，其中有長度為2的子字串BC相符，代表可以提供2/2=1的參考價值。由以上的觀察，關鍵字比對的判斷分數計算如下：
# (1)若查詢關鍵字STRING1 與文件之關鍵字STRING2完全相同(長度、內文)則得分為1。
# (2)若查詢關鍵字STRING1 與文件之關鍵字STRING2 的部分相同，則其得分為最長相同的連續子字串長度除以查詢關鍵字STRING1的字串長度之比率。
# (3)計算時以浮點數(float)型態表示(以原計算結果表示不做進位或捨位處理)。
# 須注意部分字串的比對評分方式，若有多個查詢關鍵字，將每一個查詢關鍵字依以上規則與文件之關鍵字比對後，取出最高的相關數值代表該查詢與文件的相關得分。例如查詢關鍵字BBB和BC與文件關鍵字ABC，其中前者獲得1/3的參考價值，後者獲得1的參考價值，故其最後代表價值為max{1/3, 1}=1。另外，例如查詢關鍵字AAA和BB與文件關鍵字AB，其中AB與AAA比對最長相同子字串為A，故相關性為1/3。AB與BB比對最長相同子字串為B故相關性為1/2，取兩者最大值代表，故計為max{1/3, 1/2}=1/2。
# 文件的相關性總分的計算則以所有查詢關鍵字與文件之所有關鍵字之判斷分數之總和做計算，算出總和後方才做進位或捨位處理到小數點下兩位，四捨五入。
# 設計一個程式，讀入所要查詢的一或多個關鍵字與文件關鍵字資訊，將符合關鍵字查詢的文件編號由相關性由高到低輸出(若相關性相同則以文件編號小的優先顯示)，若無則顯示找不到。
# 說明範例如下：
# 假設文件資料如下：
# 1 AAAA BBBB C DDDD EEEE
# 2 AA BB CC DD
# 3 A B C D
# 4 AB ABC AC AD
# 5 ACEF AAAA
# 使用者搜尋的關鍵字若為AAA與BB，對於每一個文件的每組關鍵字(此例為兩個關鍵字AAA與BB)得分情形如下:
#     1 -> AAAA(1) + BBBB(1) + C(0) + DDDD(0) + EEEE(0) = 2
#     2 -> AA(2/3) + BB(1) + CC(0) + DD(0) = 1.67
#     3 -> A(1/3) + B(1/2) + C(0) + D(0) = 0.83
#     4 -> AB(1/2) + ABC(1/2) + AC(1/3) + AD(1/3) = 1.67
#     5 -> ACEF(1/3) + AAAA(1) = 1.33

# Input
# 讀入第一列代表所要查詢的一或多個關鍵字(關鍵字間以一個空白分隔)。第二列為整數，代表文件的個數。其後每一列代表文件的資料，第一個整數代表文件編號，其後接續為該文件的關鍵字，關鍵字均為英文字串，每一文件至少有一個關鍵字，最多可以設定10個關鍵字，各資料間以一個空白分隔。格式如下：
# 文件編號 關鍵字1 關鍵字2 關鍵字3 關鍵字4 關鍵字5

# Output
# 將文件編號依相關性總分由高到低顯示，每一文件編號之間相隔一個空白(若相關性相同則以文件編號小的優先顯示)，若所有文件均找不到總分大於0的文件則輸出FALSE。

# Sample Input #1
# AAA BB
# 5
# 1 AAAA BBBB C DDDD EEEE
# 2 AA BB CC DD
# 3 A B C D
# 4 AB ABC AC AD
# 5 ACEF AAAA

# Sample Output #1
# 1 2 4 5 3


def calc_relevance(query, keyword):
    if query == keyword:  # exact match
        return 1.0

    dp = [[0] * (len(keyword) + 1) for _ in range(len(query) + 1)]
    max_len = 0

    for i in range(1, len(query) + 1):
        for j in range(1, len(keyword) + 1):
            if query[i - 1] == keyword[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])

    return max_len / len(query)


def calc_document_score(keywords, queries):
    total = 0

    for keyword in keywords:
        scores = []
        for query in queries:
            relevance = calc_relevance(query, keyword)
            scores.append(relevance)
        total += max(scores)

    total = round(total, 2)
    return total


def all_doc_scores_zero(arr):
    return all(x[1] == 0 for x in arr)


def main():
    queries = input().split()
    N = int(input())

    results = []
    for _ in range(N):
        doc = input().split()
        doc_id = int(doc[0])
        doc_keywords = doc[1:]

        doc_score = calc_document_score(doc_keywords, queries)
        results.append((doc_id, doc_score))

    if all_doc_scores_zero(results):
        print("FALSE")
    else:
        results.sort(
            key=lambda x: (-x[1])
        )  # sort in descending order, prioritize score then ID
        output = " ".join(str(doc_id) for doc_id, _ in results)
        print(output)


if __name__ == "__main__":
    main()
