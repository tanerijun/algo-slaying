def grandpa_trees_planning():
    n_col, n_row = list(map(int, input().split(" ")))
    plot = [[0 for _ in range(n_col)] for _ in range(n_row)]

    t = int(input())
    for _ in range(t):
        # Get initial coordinate and final coordinate
        y0, x0, y1, x1 = list(
            map(lambda x: int(x) - 1, input().split(" "))
        )  # -1 due to zero index array

        # Set directions
        dx, dy = 0, 0
        if x1 > x0:
            dx = 1
        elif x1 < x0:
            dx = -1
        if y1 > y0:
            dy = 1
        elif y1 < y0:
            dy = -1

        # Fill plot
        while x0 != x1 or y0 != y1:
            plot[x0][y0] = 1
            x0 += dx
            y0 += dy

        # The loop above stop when the cursor is at the final plot, but the plot is not filled yet
        plot[x0][y0] = 1

    # Visit all node in the plot, and get sum
    sum = 0
    for i in range(len(plot)):
        for j in range(len(plot[0])):
            sum += plot[i][j]

    # Output
    print(sum)


if __name__ == "__main__":
    grandpa_trees_planning()
