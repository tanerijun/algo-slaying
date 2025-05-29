class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V)
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]  # i-th node -> parent
        rank = [1] * (N + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return edges[0]  # won't happen

    def findRedundantConnection2(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        parents = [i for i in range(N + 1)]  # i-th node -> parent, ignore 0

        def find_par(x):
            if parents[x] != x:
                parents[x] = find_par(parents[x])  # path compression
            return parents[x]

        def union(x, y):
            root_x = find_par(x)
            root_y = find_par(y)

            if root_x == root_y:
                return False

            parents[root_x] = root_y # make 1 root point to the other (union)
            return True

        for x, y in edges:
            if not union(x, y)
                return [x, y]

        return edges[0]  # won't happen
