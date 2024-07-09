def main():
    N, M = map(int, input().split())

    # Initialize the dependency graph as a 2D list (matrix)
    # dependency_graph[i][j] = 1 if component i must be tested before component j, else 0
    graph = [[0] * N for _ in range(N)]

    # Each element is a tuple (num_dependencies, component_letter)
    component_order = [(0, chr(i + ord("A"))) for i in range(N)]

    # Store the requirement number where we first determine the complete order
    complete_order_requirement = 0

    for current_requirement in range(1, M + 1):
        before, after = input().split()

        # Update dependency graph
        before_idx = ord(before) - ord("A")
        after_idx = ord(after) - ord("A")
        graph[before_idx][after_idx] = 1

        # Propagate the dependencies (Floyd-Warshall algorithm)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    # If i->k and k->j, then i->j
                    graph[i][j] |= graph[i][k] and graph[k][j]

        # Check for conflicts (cycles)
        if any(graph[i][i] for i in range(N)):
            print(f"Order conflict after getting pair {current_requirement}")
            return

        if not complete_order_requirement:
            dependency_counts = set()
            for i in range(N):
                num_dependencies = sum(graph[i])
                component_order[i] = (num_dependencies, chr(i + ord("A")))
                dependency_counts.add(num_dependencies)
            if len(dependency_counts) == N:
                complete_order_requirement = current_requirement

    if not complete_order_requirement:  # if we never determined a complete order
        print("No answer")
    else:
        component_order.sort(reverse=True)  # sort based on number of dependencies
        order_sequence = "".join(component for _, component in component_order)
        print(
            f"Determine the testing sequence after getting pair {complete_order_requirement} : {order_sequence}"
        )


if __name__ == "__main__":
    main()
