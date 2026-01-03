class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1
        return count
