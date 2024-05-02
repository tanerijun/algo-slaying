# ROT13（迴轉13位，rotate by 13 places，有時中間加了個連字符稱作ROT-13）是一種簡易的替換式密碼。它是一種在英文網路論壇用作隱藏八卦（spoiler）、妙句、謎題解答以及某些髒話的工具，目的是逃過版主或管理員的匆匆一瞥。
# 使用ROT13加密，只需要將字母取代成13位之後的對應字母，有需要時則重新繞回26英文字母開頭即可

# Input
# 輸入一段文字（文字長度必<=5000）

# Output
# 請將這段文字轉成密文後輸出

# Sample Input #1
# It may be famous for its meandering medinas and the scenic Atlas Mountains, but Morocco might soon make its name as a solar superpower.
# Sample Output #1
# Vg znl or snzbhf sbe vgf zrnaqrevat zrqvanf naq gur fpravp Ngynf Zbhagnvaf, ohg Zbebppb zvtug fbba znxr vgf anzr nf n fbyne fhcrecbjre.


def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():  # ignore non-alphabet
            offset = 13
            base = "a" if char.islower() else "A"
            new_char = chr(((ord(char) - ord(base) + offset) % 26) + ord(base))
        else:
            new_char = char
        result += new_char
    return result


if __name__ == "__main__":
    text = input("")
    print(rot13(text))
