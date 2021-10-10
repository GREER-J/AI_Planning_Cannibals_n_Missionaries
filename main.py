from scenario import apply_action, create_actions, State, Action
from tree import TreeNode


def main():
    # Create actions
    actions = create_actions()

    init = State(left_missionaries=3, left_cannibals=3,
                 right_missionaries=0, right_cannibals=0)

    root = TreeNode(init)
    for action in actions:
        root.add_roots(action)
    root.print_tree()


main()
