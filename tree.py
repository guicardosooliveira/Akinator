from node import Node


class Tree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def insert_question_and_answers(self, new_answer, yes_node, no_node, value_to_be_changed=None):
        node_to_insert = Node("question", new_answer)
        left_node = Node("answer", yes_node)
        right_node = Node("answer", no_node)
        node_to_insert.left_node = left_node
        node_to_insert.right_node = right_node

        if self.__root is None:
            self.__root = node_to_insert