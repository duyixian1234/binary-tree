from treenode import TreeNode


def testTreeNode():
    root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    expect = 'TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))'
    assert str(root) == expect
    assert root == TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
