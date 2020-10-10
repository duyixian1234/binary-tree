class TreeNode:
    left: 'TreeNode'
    right: 'TreeNode'
    val: int

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left = f', left={self.left}' if self.left else ''
        right = f', right={self.right}' if self.right else ''
        return f'TreeNode(val={self.val}{left}{right})'

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


def inorderTraverse(root: TreeNode):
    if not root:
        return
    yield from inorderTraverse(root.left)
    yield root.val
    yield from inorderTraverse(root.right)


def preorderTraverse(root: TreeNode):
    if not root:
        return
    yield root.val
    yield from preorderTraverse(root.left)
    yield from preorderTraverse(root.right)


def postorderTraverse(root: TreeNode):
    if not root:
        return
    yield from postorderTraverse(root.left)
    yield from postorderTraverse(root.right)
    yield root.val


def levelTraverse(root: TreeNode):
    level = [root] if root else []
    while level:
        nextLevel = []
        for node in level:
            yield node.val
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        level = nextLevel


def buildTreeFromInorderPreorder(inorder: list, preorder: list):
    if not inorder:
        return None
    node = TreeNode(preorder[0])
    index = inorder.index(node.val)
    node.left = buildTreeFromInorderPreorder(inorder[:index], preorder[1:index + 1])
    node.right = buildTreeFromInorderPreorder(inorder[index + 1:], preorder[index + 1:])
    return node


def buildTreeFromInorderPostorder(inorder: list, postorder: list):
    if not inorder:
        return None
    node = TreeNode(postorder[-1])
    index = inorder.index(node.val)
    node.left = buildTreeFromInorderPostorder(inorder[:index], postorder[:index])
    node.right = buildTreeFromInorderPostorder(inorder[index + 1:], postorder[index:-1])
    return node


def toList(node: TreeNode):
    ret = []
    if not node:
        return ret
    stack = [node]
    ret.append(node.val)
    while stack:
        node = stack.pop(0)
        if node.left:
            ret.append(node.left.val)
            stack.append(node.left)
        elif stack:
            ret.append('#')

        if node.right:
            ret.append(node.right.val)
            stack.append(node.right)
        elif stack:
            ret.append('#')

    while ret[-1] == '#':
        ret.pop(len(ret) - 1)

    return ret


def fromList(lst: list):
    if not lst:
        return None
    val = lst.pop(0)
    root = TreeNode(val)
    stack = [root]
    while stack:
        parent = stack.pop(0)
        if not lst:
            break
        val = lst.pop(0)
        if val != '#':
            node = TreeNode(val)
            stack.append(node)
            parent.left = node
        if not lst:
            break
        val = lst.pop(0)
        if val != '#':
            node = TreeNode(val)
            stack.append(node)
            parent.right = node
    return root
