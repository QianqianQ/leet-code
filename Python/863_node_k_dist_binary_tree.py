from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        parent = {}

        def mark_parents(node, par=None):
            if node:
                if par:
                    parent[node] = par
                mark_parents(node.left, node)
                mark_parents(node.right, node)

        mark_parents(root)

        # BFS
        visited = set()
        q = deque([target])
        visited.add(target)
        dist = 0

        while q:
            if dist == k:
                return [node.val for node in q]
            for _ in range(len(q)):
                node = q.popleft()
                for n in (node.left, node.right, parent.get(node)):
                    if n and n not in visited:
                        visited.add(n)
                        q.append(n)
            dist += 1

        return []


if __name__ == '__main__':
    # Example usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    target = root.left  # Node with value 2
    k = 1

    solution = Solution()
    result = solution.distanceK(root, target, k)
    print(result)  # Output: [1, 4, 5]
