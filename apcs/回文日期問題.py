# 回文數(或迴文數)是指一個像16461這樣對稱的數，即將這個數的數字按相反的順序重新排列後，所得到的數和原來的數一樣。這裡，「回文」是指正讀反讀都相同的單詞或句子。
# 日期的表示中包含年、月、日三部分，假設年以西元曆法表示固定為四位數字，月數與日期數部分若為小於10 (介於1到9之整數)則可以採用刪除或不刪除前導0的方式表示為1到9或01到09。例如，2017年1月2日可以表示為 201712, 2017012, 2017102, 20170102四種數字。從給定一個數字來看，20111102代表2011年11月2日，只代表一個日期。但數字2017102 可以代表2017年10月2日或代表2017年1月2日。數字2011102 可以代表2011年10月2日或2011年1月2日 。
# 設計一個程式，輸入四位數字代表西元年(介於1000到9999 之間)，輸出該年度內所有可能產生回文數的日期與個數，不同日期所轉成的回文數雖相同但需要分別計算。例如2017102 可以代表2017年10月2日或代表2017年1月2日算兩次。此問題中，需要考慮閏年的影響，閏年定義為西元年份可以被4整除但不能被100整除則為閏年。若西元年份可以被100 整除(例如 1900)則必須同時被 400 整除才是閏年 (如2000)。
# Input
# 輸入資料中第一列為一整數n，代表接下來有n組測試資料。
# 每組測試為一個介於1000與9999之間的數字。
# Output
# 輸出該年度回文日期的個數與所有回文日期(包含重複的回文日期，重複兩次須印出兩個)，將回文日期視為整數後由小到大輸出，各資料間以一個空格分開。
# Sample Input #1
# 5
# 1111
# 1201
# 2017
# 1340
# 1010
# Sample Output #1
# 4 111111 1111111 1111111 11111111
# 2 1201021 12011021
# 2 2017102 2017102
# 0
# 3 1010101 1010101 10100101


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def main():
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    times = int(input())
    for _ in range(times):
        year = int(input())
        month, day = 1, 1
        palindromes = []

        while True:
            if month < 10:
                if day < 10:
                    date = year * 100 + month * 10 + day
                    if is_palindrome(date):
                        palindromes.append(date)

                date = year * 1000 + month * 100 + day
                if is_palindrome(date):
                    palindromes.append(date)

            if day < 10:
                date = year * 1000 + month * 10 + day
                if is_palindrome(date):
                    palindromes.append(date)

            date = year * 10000 + month * 100 + day
            if is_palindrome(date):
                palindromes.append(date)

            if month == 12 and day == 31:
                break
            elif day < (month_days[month] + (1 if month == 2 and is_leap(year) else 0)):
                day += 1
            else:
                day = 1
                month += 1

        palindromes.sort()
        print(len(palindromes), *palindromes)


if __name__ == "__main__":
    main()
