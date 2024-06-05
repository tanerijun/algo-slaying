# 有 K 個球從一完整二元樹（fully binary tree, FBT）的樹根（root）一個一個往下掉。當這個球遇到非終端節點時，可能往左子樹跑，也可能往右子樹跑，如此直到這顆球到達終端節點（也就是樹葉）為止。至於在非終端節點時球該往左或往右的決定乃是由 2 個值 true, false 來控制的。如果這非終端節點的現在的值為 false，則球來的時候會往左子樹走，但是這個值會變為 true。如果這非終端節點的現在的值為 true，則球來的時候會往右子樹走，但是這個值會變為 false。請注意：一開始時所有非終端節點的值均為 false。另外，在完整二元樹中所有的節點被依序編號，從上（深度 = 1）到下，由左到右。請參考下圖。
# 舉例來說，上面的圖為深度為4的完整二元樹。第一顆球往下掉會經過節點 1、2、4 最後落在節點 8 中。第二顆球往下掉則會經過節點 1、3、6 最後落在節點 12 中。第三顆球往下掉會經過節點 1、2、5 最後落在節點 10 中。
# 給你完整二元樹的深度 D 以及落下的第 I 個球，請你寫一個程式算出第 I 個球落在終端節點的編號。

# Input
# 輸入的第一列有一個整數，代表以下有幾組測試資料。
# 每組測試資料一列有 2 個整數 D, I（2 <= D <= 11, 1 <= I <= 1024）。你可以假設 I 不會超過終端節點的數目。

# Output
# 對每組測試資料輸出一列，第 I 個球落在終端節點的編號

# Sample Input #1
# 5
# 4 2
# 3 4
# 10 1
# 2 2
# 8 128
# Sample Output #1
# 12
# 7
# 512
# 3
# 255


# Constructing whole tree and simulate ball drops (too slow for 1 of the test case)
class Solution1:
    class Node:
        def __init__(self, id, value=False, left=None, right=None):
            self.id = id
            self.value = value
            self.left = left
            self.right = right

    def construct_tree(self, depth):
        if depth <= 0:
            return None

        # First level
        root = self.Node(1)
        queue = [root]
        id = 2

        for _ in range(1, depth):
            next_level = []
            for node in queue:
                # Create left and right children
                node.left = self.Node(id)
                id += 1
                node.right = self.Node(id)
                id += 1
                next_level.extend([node.left, node.right])
            queue = next_level

        return root

    def insert_ball(self, node):
        if not node.left and not node.right:
            # We have reached the leaf
            return node.id

        if not node.left.value:
            node.left.value = True
            return self.insert_ball(node.left)
        else:
            node.left.value = False
            return self.insert_ball(node.right)

    def main(self):
        N = int(input())
        data = []
        for _ in range(N):
            D, I = map(int, input().split())
            data.append((D, I))

        res = []
        for D, I in data:
            root = self.construct_tree(D)
            for _ in range(I - 1):
                self.insert_ball(root)
            final_ball_location = self.insert_ball(root)
            res.append(final_ball_location)

        for r in res:
            print(r)


# Solution 2: Using index arithmetic
def find_leaf(D, I):
    pos = 1  # initial position (root)
    for _ in range(D - 1):
        if I % 2 == 1:  # if I is odd, go left
            pos = pos * 2  # update position to left child
            I = (I + 1) // 2
        else:  # if I is even, go right
            pos = pos * 2 + 1  # update position to right child
            I //= 2
    return pos


def main():
    N = int(input())
    results = []
    for _ in range(N):
        D, I = map(int, input().split())
        results.append(find_leaf(D, I))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
