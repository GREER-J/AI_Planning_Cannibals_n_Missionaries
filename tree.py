from action import Action, try_action
from node import Node


class State_Tree:
    """ A class to manage all the states of the world and how they relate to each other
    """

    def __init__(self, node: Node) -> None:
        self.node = node
        self.children = {}
        self.parent = None

    def add_child(self, child, path: Action):
        child.set_parent(self)
        self.children[child] = path

    def get_children(self):
        return(self.children)

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return(self.parent)

    def get_level(self):
        level = 0
        p = self.parent
        while(p):
            level += 1
            p = p.parent
        return(level)

    def try_actions(self, actions):
        for action in actions:
            val = try_action(self, action)
            if(val):
                left_missionaries = val[0]
                left_cannibals = val[1]
                right_missionaries = val[2]
                right_cannibals = val[3]
                node_obj = Node(left_missionaries=left_missionaries, left_cannibals=left_cannibals,
                                right_missionaries=right_missionaries, right_cannibals=right_cannibals)
                state_tree_obj = State_Tree(node_obj)
                self.add_child(state_tree_obj, action)
        for child in self.children:
            child.try_actions(actions)

    def print_tree(self):
        spaces = ' ' * 20 * self.get_level()
        first = '|-'
        second = '->'
        print(
            f"{spaces} {first + self.parent.children[self].fn_name + second if(self.parent) else ''} {self.node} {'' if(self.node.valid) else '*'}")
        for child in self.children:
            child.print_tree()
