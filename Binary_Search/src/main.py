from dataclasses import dataclass
from typing import Union


@dataclass
class Node:
    root: Union[int, None]
    key: int
    left_branch: Union[list, None]
    right_branch: Union[list, None]


class Tree:
    """
    A Binary Search Tree (BST) is a tree data structure where each node has at most two children, and the left subtree
    of a node contains only nodes with keys less than the node's key, and the right subtree of a node contains only
    nodes with keys greater than the node's key.
    """

    def __init__(self):
        self.branches: [Node] = []

    @staticmethod
    def generate_root_node(node: Node) -> int:
        node.root = node.key
        return node.root

    def insert(self, node: Node) -> None:
        """
        Inserts a new node with the given key into the Tree
        """
        # IF no existing node then generate root
        if len(self.branches) == 0:
            node.root = self.generate_root_node(node)
        # IF node key values are less than the root node then add to left branch
        # ELSE IF node key values are greater than root node then add to right branch
        self.branches.append(node)

    def search(self, key):
        """
        - Searches for a node with the given key in the Tree, and returns its value
        - Raises exception if the node is not found
        :returns: Key
        """
        pass

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
