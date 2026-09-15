"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(n):
            if n is None:
                return None
            if n in clones:
                return clones[n]

            clone = Node(n.val)
            clones[n] = clone

            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
        