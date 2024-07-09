# 在一個公司中有各個部門，對一個新開發的產品，產品會先被分成多個組成元件分配給各部門研發分析。各部門在研發自己負責的元件後，必須指定該元件和其他元件的測試先後需求。例如甲部門研發元件A，可指定乙部門研發的元件B必須先測試無誤，才能進行元件A的功能測試。研發長對這個測試先後順序的要求很嚴謹，各部門指定的元件先後測試需求必須能決定一個產品所有元件的測試先後順序，這個研發長的秘書必須彙整各部門回報的元件先後測試需求進行檢查。
# 各部門會陸續提出元件之先後測試需求，且可能給定重複之元件先後測試需求。每次接到一筆先後測試需求，秘書就必須檢查目前所蒐集的先後測試需求是否已經可以確定所有元件間的測試先後順序。若收到第 i 筆先後測試需求就可確定所有元件間的測試先後順序，就列出數值i 及所有元件間的測試先後順序。若讀到第 i 筆先後測試需求後發現有順序矛盾的情況，例如A要在B之前、B要在C之前、C又要在A之前，則必須列出數值 i 並顯示先後順序有矛盾的訊息。若收到各部門所有回報的元件先後測試需求後，仍無法決定產品所有元件的測試先後順序，則必須顯示資訊不完整的訊息。請你寫一個程式幫忙這位研發長的秘書順利完成此工作。

# Input
# 第一行為兩個正整數N及M，以空白區隔。其中N表示元件的個數，M 表示所輸入元件先後測試需求的筆數。其中2 ≦ N≦26，1≦M≦100。
# 第二行開始M行，每一行輸入兩個不同的英文大寫字母，中間以空白區隔，表示兩個不同元件。先出現的元件表示要在後出現元件前先測試。

# Output
# 依三種情況分別顯示
# 1.所有元件已可決定測試順序:
# Determine the testing sequence after getting pair i : 接下來依已決定之所有元件測試先後順序 輸出這些元件
# 2.部分元件順序產生矛盾:
# Order conflict after getting pair i
# 3.已讀完所有配對但無法決定讀入元件的配對
# No answer
# 若在所有元件已可決定測試順序後，繼續讀入其後的前後測試需求會發生部分元件順序產生矛盾的情況，則請輸出第二種情況。
# /* 若任意輸入資料皆回傳 No answer 則不予計分 */

# Sample Input #1
# 4 6
# A B
# B C
# C D
# A D
# A C
# B D

# Sample Output #1
# Determine the testing sequence after getting pair 3 : ABCD

# Sample Input #2
# 4 6
# A B
# B C
# C A
# A D
# C D
# B D

# Sample Output #2
# Order conflict after getting pair 3

# Sample Input #3
# 4 5
# A B
# A C
# B D
# C D
# A C

# Sample Output #3
# No answer


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
