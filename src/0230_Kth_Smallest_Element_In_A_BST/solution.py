class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Eh... doesn't feel faster than naive on average.
        Runtime: 97.74%
        Memory: 56.74%
        """
        stack = []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallestRecursiveOofN(self, root: TreeNode, k: int) -> int:
        """
        Slow AF.
        """

        def order(node: TreeNode):
            if node is None:
                return []
            return order(node.left) + [node.val] + order(node.right)

        nodes = order(root)
        return nodes[k - 1]

    def count_nodes(self, node: TreeNode) -> int:
        if node is None:
            return 0

        rtn = 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
        return rtn

    def kthSmallestNaive(self, root: TreeNode, k: int) -> int:
        """
        Runtime: 81.95%
        Memory: 95.51%
        """
        curr_node_idx = 1 + self.count_nodes(root.left)

        if curr_node_idx == k:
            return root.val
        elif curr_node_idx < k:
            return self.kthSmallestNaive(root.right, k - curr_node_idx)
        else:
            return self.kthSmallestNaive(root.left, k)
