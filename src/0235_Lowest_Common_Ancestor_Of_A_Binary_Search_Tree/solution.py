class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Runtime: 90.61%
        Memory: 79.93%
        """
        pval, qval = p.val, q.val

        node = root
        while True:
            if (
                min(pval, qval) < node.val
                and node.val < max(pval, qval)
                or node.val == pval
                or node.val == qval
            ):
                return node

            if pval < node.val:
                node = node.left
            else:
                node = node.right

    def lowestCommonAncestorNaive(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Runtime: 90.61%
        Memory: 47.55%
        """
        pval, qval, rval = p.val, q.val, root.val
        if root is p or root is q or min(pval, qval) < rval and rval < max(pval, qval):
            return root

        if pval < rval:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
