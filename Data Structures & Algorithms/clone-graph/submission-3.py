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

        def cloneNode(node):
            # if not node:
            #     return None
            if node in clones:
                return clones[node]

            clone = Node(node.val)
            clones[node] = clone

            for nei in node.neighbors:
                cloned_nei = cloneNode(nei)
                clone.neighbors.append(cloned_nei)
            
            return clone

        return cloneNode(node) if node else None
        