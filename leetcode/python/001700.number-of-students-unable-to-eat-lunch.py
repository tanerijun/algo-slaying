from collections import Counter, deque


class Solution:
    # Time complexity: O(n^2) - worst case is when sandwiches alternate types, but students are clustered in groups (ex: Sandwiches: [1, 0, 1, 0] (Alternating), Students: [0, 0, 1, 1] (Clustered))
    # Space complexity: O(n)
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        q = deque(students)
        i = 0
        t = 0

        while i < len(sandwiches):
            if t >= len(q):
                return len(q)

            if q[0] == sandwiches[i]:
                q.popleft()
                i += 1
                t = 0
            else:
                q.append(q.popleft())
                t += 1

        return 0

    # Time complexity: O(n)
    # Space complexity: O(1)
    def countStudents1(self, students: list[int], sandwiches: list[int]) -> int:
        want0, want1 = 0, 0
        for s in students:
            if s == 0:
                want0 += 1
            else:
                want1 += 1

        for s in sandwiches:
            if s == 0:
                if want0 == 0:
                    return want1
                else:
                    want0 -= 1
            else:
                if want1 == 0:
                    return want0
                else:
                    want1 -= 1

        return 0

    # Time complexity: O(n)
    # Space complexity: O(1)
    def countStudents2(self, students: list[int], sandwiches: list[int]) -> int:
        count = Counter(students)
        for i in range(len(sandwiches)):
            if count[sandwiches[i]] == 0:
                return len(sandwiches) - i
            count[sandwiches[i]] -= 1
        return 0
