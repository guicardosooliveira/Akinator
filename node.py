class Node:
    def __init__(self, type, value):
        self.__left_node = None
        self.__right_node = None
        self.__type = type
        self.__value = value

    @property
    def left_node(self):
        return self.__left_node

    @left_node.setter
    def left_node(self, left_node):
        self.__left_node = left_node

    @property
    def right_node(self):
        return self.__right_node

    @right_node.setter
    def right_node(self, right_node):
        self.__right_node = right_node

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value