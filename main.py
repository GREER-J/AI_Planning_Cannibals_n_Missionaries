from setup import create_actions
from node import Node
from tree import State_Tree

# init world
actions = create_actions()
init = Node(left_missionaries=3, left_cannibals=3,
            right_missionaries=0, right_cannibals=0)
root = State_Tree(init)

# Create tree
root.try_actions(actions)
root.print_tree()
