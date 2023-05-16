import pytest

from Binary_Search.src.main import Tree, Node


def test_insert():
    # Arrange
    root_key = 10
    node_key = 12
    tree = Tree()

    # Act
    tree.insert(Node(root_key))
    tree.insert(Node(node_key))

    # Assert
    assert tree.root.right is not None          # Check that the roots right branch is populated
    assert tree.root.right.key == node_key      # Check the key in the right branch is consistent with the key provided


def test_insert_generates_root_node():
    # Arrange
    node = Node(1)
    tree = Tree()

    # Act
    tree.insert(node)

    # Assert
    assert tree.root.key == node.key


def test_search_finds_node():
    # Arrange
    tree = Tree()
    tree.insert(Node(0))
    tree.insert(Node(20))
    tree.insert(Node(10))

    # Act
    searched_node = tree.search(Node(10))

    # Assert
    assert searched_node is not None
    assert searched_node.key == 10


def test_search_does_not_find_node():
    # Arrange
    tree = Tree()
    tree.insert(Node(0))
    tree.insert(Node(20))
    tree.insert(Node(10))

    # Act and Assert
    with pytest.raises(ValueError):
        # Act
        searched_node = tree.search(Node(5))
        # Assert
        assert searched_node is None

