from node import Node
from type_enum import TypeEnum


class Tree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def insert_question_and_answers(self, new_question: str, yes_node: str, no_node: str, old_node: Node = None):
        node_to_insert = Node(TypeEnum.QUESTION, new_question)
        left_node = Node(TypeEnum.ANSWER, yes_node)
        right_node = Node(TypeEnum.ANSWER, no_node)
        node_to_insert.left_node = left_node
        node_to_insert.right_node = right_node

        if self.__root is not None:
            old_node.value = new_question
            old_node.type = TypeEnum.QUESTION
            old_node.left_node = left_node
            old_node.right_node = right_node

        else:
            self.__root = node_to_insert

    def get_parent_by_child(self, child_value):
        pointer = self.__root
        while pointer.left_node.value != child_value or pointer.right_node.value != child_value:
            pointer = pointer.left_node
