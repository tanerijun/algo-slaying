class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0  # track word
        p2 = 0  # track abbr

        while p1 < len(word) and p2 < len(abbr):
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            elif not abbr[p2].isdigit() or abbr[p2] == "0":
                return False
            else:
                count = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    count = count * 10 + int(abbr[p2])
                    p2 += 1
                p1 += count

        return p1 == len(word) and p2 == len(abbr)
