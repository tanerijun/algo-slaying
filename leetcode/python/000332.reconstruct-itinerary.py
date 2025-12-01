from collections import defaultdict


class Solution:
    # Time complexity: O(E^2)
    # For each of the E edges, we might try and backtrack
    # Each backtracking operation involves pop(i) and insert(i, v) which are O(E) operations in PY
    # So: E edges × O(E) per operation = O(E²)
    # Space complexity: O(E)
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        # Sorting tickets ensures destinations are added in lexicographical order
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            # +1 on tickets because we include the starting point "JFK"
            if len(res) == len(tickets) + 1:
                return True
            # There's no connection to other places from this node (dead end)
            # This is only allowed if it's the final destination (which will trigger the 1st condition)
            if src not in graph:
                return False

            temp = graph[src].copy()  # because we're mutating graph[src]
            for i, v in enumerate(temp):
                graph[src].pop(i)  # temporary remove the ticket to mark it as "used"
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                graph[src].insert(i, v)

            return False

        dfs("JFK")
        return res

    # Hierholzer's Algorithm -> Eulerian Path
    # Time complexity: O(Elog(e)) -> E = number of tickets
    # Space complexity: O(E)
    def findItinerary1(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        # Sort tickets lexicographically, then REVERSE the order
        # Why reverse? Because we'll use pop() which takes from the END
        # After building graph for tickets [["JFK","SFO"],["JFK","ATL"]]:
        # graph["JFK"] = ["SFO", "ATL"]
        #                  ^      ^
        #               first   last (popped first!)
        # When we pop(), we get "ATL" first (lexicographically smallest)
        for src, dst in sorted(tickets)[::-1]:
            graph[src].append(dst)

        res = []  # will store our itinerary in REVERSE order

        def dfs(src):
            # Keep exploring while current airport has outgoing flights
            while graph[src]:
                # lexicographically SMALLEST unvisited destination
                dst = graph[src].pop()
                # Recursively visit that destination
                # We go as deep as possible before adding to result
                dfs(dst)

            # We append AFTER visiting all destinations (postorder)
            # This means we add airports in REVERSE order of the actual path
            # The deepest airport (final destination) gets added first
            # The starting airport "JFK" gets added last
            res.append(src)

        dfs("JFK")

        # Since we built the path backwards, reverse it to get correct order
        return res[::-1]

    # Tracing input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # 1. Build graph:
    # Sorted: [["ATL","JFK"], ["ATL","SFO"], ["JFK","ATL"], ["JFK","SFO"], ["SFO","ATL"]]
    # Reversed: [["SFO","ATL"], ["JFK","SFO"], ["JFK","ATL"], ["ATL","SFO"], ["ATL","JFK"]]
    # Graph after building:
    # JFK: ["SFO", "ATL"]  ← "ATL" is at the end, will be popped first
    # ATL: ["SFO", "JFK"]  ← "JFK" is at the end, will be popped first
    # SFO: ["ATL"]
    #
    # 2. DFS:
    # Call dfs("JFK"):
    #   graph["JFK"] = ["SFO", "ATL"]
    #   Pop "ATL" → graph["JFK"] = ["SFO"]
    #
    #   Call dfs("ATL"):
    #     graph["ATL"] = ["SFO", "JFK"]
    #     Pop "JFK" → graph["ATL"] = ["SFO"]
    #
    #     Call dfs("JFK"):
    #       graph["JFK"] = ["SFO"]
    #       Pop "SFO" → graph["JFK"] = []
    #
    #       Call dfs("SFO"):
    #         graph["SFO"] = ["ATL"]
    #         Pop "ATL" → graph["SFO"] = []
    #
    #         Call dfs("ATL"):
    #           graph["ATL"] = ["SFO"]
    #           Pop "SFO" → graph["ATL"] = []
    #
    #           Call dfs("SFO"):
    #             graph["SFO"] = []  ← No more flights!
    #             res.append("SFO")  → res = ["SFO"]
    #
    #           res.append("ATL")  → res = ["SFO", "ATL"]
    #
    #         res.append("SFO")  → res = ["SFO", "ATL", "SFO"]
    #
    #       res.append("JFK")  → res = ["SFO", "ATL", "SFO", "JFK"]
    #
    #     res.append("ATL")  → res = ["SFO", "ATL", "SFO", "JFK", "ATL"]
    #
    #   res.append("JFK")  → res = ["SFO", "ATL", "SFO", "JFK", "ATL", "JFK"]
