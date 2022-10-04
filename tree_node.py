#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

#A leaf is a node with no children.

#Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#Output: true
#Explanation: The root-to-leaf path with the target sum is shown.



class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pass

# Creating test TreeNode 1
test_1 = TreeNode(5)
test_1.left = TreeNode(4)
test_1.right = TreeNode(8)
test_1.left.left = TreeNode(11)
test_1.left.left.left = TreeNode(7)
test_1.left.left.right = TreeNode(2)
test_1.right.left = TreeNode(13)
test_1.right.right = TreeNode(4)
test_1.right.right.right = TreeNode(1)

# Creating test TreeNode 2
test_2 = TreeNode(1)
test_2.left = TreeNode(2)
test_2.right = TreeNode(3)

# creating test 3
test_3 = None

# Calling Tests
s = Solution()

print(s.hasPathSum(test_1, 22),
s.hasPathSum(test_2, 5),
s.hasPathSum(test_3, 0))
