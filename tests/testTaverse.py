from treenode import TreeNode, inorderTraverse, preorderTraverse, postorderTraverse, levelTraverse, buildTreeFromInorderPreorder, buildTreeFromInorderPostorder
import pytest


@pytest.fixture()
def root():
    yield TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5, left=TreeNode(6))))


def testInorderTraverse(root: TreeNode):
    assert list(inorderTraverse(root)) == [4, 2, 1, 3, 6, 5]


def testPreorderTraverse(root: TreeNode):
    assert list(preorderTraverse(root)) == [1, 2, 4, 3, 5, 6]


def testPostorderTraverse(root: TreeNode):
    assert list(postorderTraverse(root)) == [4, 2, 6, 5, 3, 1]


def testLevelTraverse(root: TreeNode):
    assert list(levelTraverse(root)) == [1, 2, 3, 4, 5, 6]


def testBuildTreeFromInorderPreorder(root: TreeNode):
    inorder = [4, 2, 1, 3, 6, 5]
    preorder = [1, 2, 4, 3, 5, 6]
    assert buildTreeFromInorderPreorder(inorder, preorder) == root


def testBuildTreeFromInorderPostorder(root: TreeNode):
    inorder = [4, 2, 1, 3, 6, 5]
    postorder = [4, 2, 6, 5, 3, 1]
    assert buildTreeFromInorderPostorder(inorder, postorder) == root
