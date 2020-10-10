from treenode import TreeNode, toList, fromList


def testToList():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
    assert toList(root) == [1, 2, 3, 4, '#', '#', 5]
    assert toList(None) == []


def testFromList():
    lst = [1, 2, 3, 4, '#', '#', 5]
    expect = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
    assert str(fromList(lst)) == str(expect)
    assert fromList([]) == None