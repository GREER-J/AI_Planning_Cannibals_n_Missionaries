from scenario import apply_action
from scenario import State


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.data = val.state
        self.children = {}
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix} |__if self.parent else  -> {self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child, path):
        child.parent = self
        self.children[child] = path

    def add_roots(self, action):
        try:
            lm, lc, rm, rc = apply_action(self.val, action)
            n = State(lm, lc, rm, rc)
            s = TreeNode(n)
            self.add_child(s, action)
        except ValueError:
            pass
        if self.children:
            for child in self.children:
                child.add_roots(action)
