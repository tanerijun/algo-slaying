class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def compress(self, chars: list[str]) -> int:
        write = 1
        cur_count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cur_count += 1
            else:
                if cur_count != 1:
                    digits = str(cur_count)
                    for digit in digits:
                        chars[write] = digit
                        write += 1
                chars[write] = chars[i]
                cur_count = 1
                write += 1

        if cur_count > 1:
            digits = str(cur_count)
            for digit in digits:
                chars[write] = digit
                write += 1

        del chars[write:]
        return len(chars)

    # Time complexity: O(n)
    # Space complexity: O(1)
    def compress1(self, chars: list[str]) -> int:
        write = 0
        group_start = 0

        for read in range(len(chars)):
            if read + 1 == len(chars) or chars[read] != chars[read + 1]:
                chars[write] = chars[group_start]
                write += 1
                count = read - group_start + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                group_start = read + 1

        return write
