from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class Tree:
    """
    A Binary Search Tree (BST) is a tree data structure where each node has at most two children, and the left subtree
    of a node contains only nodes with keys less than the current_node's key/root, and the right subtree of a node
    contains only nodes with keys greater than the node's key/root.
    """

    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, node: Node) -> None:
        """
        Inserts a new node with the given key into the Tree
        """
        # IF no existing node then generate root
        if self.root is None:
            self.root = Node(node.key)
        else:
            self._insert_recursive(self.root, node)

    def _insert_recursive(self, root: Node, node: Node):
        """
        Runs through a search of all the existing nodes
        Checks if they have a current value attached to their left or right branches and assigns
        the passed through node to the correct position

        - IF `node.key` values are less than the `root.key` then add to left branch
        - ELSE IF `node.key` values are greater than `root.key` then add to right branch
        """
        if node.key < root.key:
            if root.left is None:
                root.left = node
            else:
                self._insert_recursive(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self._insert_recursive(root.right, node)

    def search(self, node: Node) -> Node:
        """
        - Searches for a node with the given key in the Tree, and returns its value
        - Raises exception if the node is not found
        :returns: node.key
        """
        return self._search_recursive(self.root, node)

    def _search_recursive(self, root: Node, node: Node) -> Node:
        """
        Searches for different values from the nodes in the tree and then returns it back once
        Identifying the specific key input
        """
        if root is None:
            raise ValueError(
                f"expected node value: {node.key} doesn't exist within tree and therefore can't be searched."
            )
        else:
            if root.key == node.key:
                return node
            elif node.key < root.key:
                return self._search_recursive(root.left, node)
            elif node.key > root.key:
                return self._search_recursive(root.right, node)

    def delete(self, key):
        """
        - Deletes the node with the given key from the Tree.
        - Raises exception if the node is not found.
        """
        pass

    def is_empty(self):
        """
        - Returns True if the Tree is empty,
        - Returns False if the Tree is populated.

        :returns: Boolean
        """
        pass
