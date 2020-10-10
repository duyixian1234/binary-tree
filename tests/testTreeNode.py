from treenode import TreeNode, swapChildren


def testTreeNode():
    root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    expect = 'TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))'
    assert str(root) == expect
    assert root == TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))


def testSwapChildren():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
    expect = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5)), right=TreeNode(val=2, right=TreeNode(val=4)))
    swapChildren(root)
    assert root == expect
    swapChildren(root)
    assert root == TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
