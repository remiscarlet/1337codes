from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Runtime: 98.28%
    Memory: 97.83%
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        stack: List["TreeNode"] = [root]
        parents_map: Dict["TreeNode", Optional["TreeNode"]] = {root: None}

        node: Optional["TreeNode"] = None
        while p not in parents_map or q not in parents_map:
            node = stack.pop()

            if node.left:
                parents_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parents_map[node.right] = node
                stack.append(node.right)

        p_ancestry = set()
        node = p
        while node is not None:
            p_ancestry.add(node)
            node = parents_map[node]

        node = q
        while node is not None:
            if node in p_ancestry:
                return node
            node = parents_map[node]

        raise RuntimeError("???")

    def lowestCommonAncestorNaive(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cache = {}  # type: ignore

        def is_child(root: "TreeNode", t: "TreeNode") -> bool:
            if root is None:
                return False
            cache_key = (root.val, t.val)
            if cache_key in cache:
                return cache[cache_key]

            rtn = root.val == t.val or is_child(root.left, t) or is_child(root.right, t)

            cache[cache_key] = rtn
            return rtn

        def helper(root, p, q):
            if root is p or root is q:
                return root

            p_on_left = is_child(root.left, p)
            q_on_left = is_child(root.left, q)

            if p_on_left != q_on_left:
                # One is on left, one is on right. Root is ancestor.
                return root
            elif not p_on_left and not q_on_left:
                return helper(root.right, p, q)
            else:
                return helper(root.left, p, q)

        return helper(root, p, q)
