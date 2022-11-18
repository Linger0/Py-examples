import uuid
from graphviz import Digraph

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree():
    def __init__(self, root=None):
        self.root = root
        self.dot = Digraph(comment='Tree', format='png')
    def printTree(self, savePath = 'Tree'):
        def printChildren(parent: TreeNode, parTag: str):
            if parent.left:
                lTag = str(uuid.uuid1())
                self.dot.node(lTag, str(parent.left.rmark))
                self.dot.edge(parTag, lTag)
                printChildren(parent.left, lTag)
            if parent.right:
                rTag = str(uuid.uuid1())
                self.dot.node(rTag, str(parent.right.rmark))
                self.dot.edge(parTag, rTag)
                printChildren(parent.right, rTag)
        if isinstance(self.root, TreeNode):
            rootTag = str(uuid.uuid1())
            self.dot.node(rootTag, str(self.root.rmark))
            printChildren(self.root, rootTag)
        self.dot.render(savePath)

def listBuildTree(vals: list, i=0):
    if i < len(vals) and vals[i]:
        v = vals[i]
        node = TreeNode(v)
        node.left = listBuildTree(vals, 2 * i + 1)
        node.right = listBuildTree(vals, 2 * i + 2)
        return node
    return None

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def DFS(node: TreeNode):
            if node.left:
                lcMark, vl = DFS(node.left)
                if lcMark:
                    lmark = {x + 1: y for x, y in lcMark.items()}
                else:
                    lmark = {1: 1}
            else:
                vl = 0
                lmark = dict()
            if node.right:
                rcMark, vr = DFS(node.right)
                if rcMark:
                    rmark = {x + 1: y for x, y in rcMark.items()}
                else:
                    rmark = {1: 1}
            else:
                vr = 0
                rmark = dict()

            ret = vl + vr
            for i in range(1, distance):
                for j in range(1, distance - i + 1):
                    ret += lmark.get(i, 0) * rmark.get(j, 0)

            merge = lmark.copy()
            for k, v in rmark.items():
                merge[k] = merge.get(k, 0) + v
            return (merge, ret)

        if not root:
            return 0
        return DFS(root)[1]


if __name__ == "__main__":
    tree = Tree()
    tree.root = listBuildTree([1,2,3,None,4])
    print(Solution.countPairs(None, tree.root, 3))
    # tree.printTree(savePath='TreeRight')