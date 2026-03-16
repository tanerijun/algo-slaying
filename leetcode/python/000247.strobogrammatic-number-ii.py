class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
             we will sort your return value in output
    """

    # Time complexity: O(n * 5 ^ (n / 2)) - 5 pairs, N/2 layers, each result has length n
    # Space complexity: O(5 ^ (n / 2)) results stored
    def find_strobogrammatic(self, n: int) -> list[str]:
        def helper(curr_len, total_len):
            if curr_len == 0:
                return [""]
            if curr_len == 1:
                return ["0", "1", "8"]

            inner = helper(curr_len - 2, total_len)
            result = []

            for mid in inner:
                for left, right in [("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]:
                    result.append(left + mid + right)

                # Only add "0...0" if it's NOT the outermost layer
                if curr_len != total_len:
                    result.append("0" + mid + "0")

            return result

        return helper(n, n)
