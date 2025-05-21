class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) - always 26
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Adding new character on the right
            index = ord(s2[r]) - ord("a")
            if s1_count[index] == s2_count[index]:  # we're about to break a match
                matches -= 1
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:  # we just created a match
                matches += 1

            # Removing character on the left
            index = ord(s2[l]) - ord("a")
            if s1_count[index] == s2_count[index]:  # we're about to break a match
                matches -= 1
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:  # we just created a match
                matches += 1

            l += 1

        return matches == 26
