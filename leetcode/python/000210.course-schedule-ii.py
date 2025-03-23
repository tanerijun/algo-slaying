class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prerequisites_map = {c: [] for c in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        visited, visiting = set(), set()
        output = []

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for prerequisite in prerequisites_map[course]:
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output
