from Binary_Search.src.main import Tree, Node


def test_insert():
    # Arrange
    node = Node(
        root=None,
        key=1,
        left_branch=None,
        right_branch=None
    )

    tree = Tree()

    # Act
    tree.insert(node)

    # Assert
    assert tree.branches[0].key == node.key


def test_insert_generates_root_node():
    # Arrange
    node = Node(
        root=None,
        key=1,
        left_branch=None,
        right_branch=None
    )
    tree = Tree()

    # Act
    tree.insert(node)

    # Assert
    assert tree.branches[0].root == node.key


