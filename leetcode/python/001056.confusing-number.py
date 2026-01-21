class Solution:
    # Time complexity: O(L) -> L is the number of maximum digits n can have (floor(log_10(n)) + 1)
    # Space complexity: O(L)
    def confusingNumber(self, n: int) -> bool:
        rotate_map = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }

        rotated = ""
        str_n = str(n)
        for i in range(len(str_n) - 1, -1, -1):
            ch = str_n[i]
            if ch not in rotate_map:
                return False
            rotated += rotate_map[ch]

        return rotated != str_n
