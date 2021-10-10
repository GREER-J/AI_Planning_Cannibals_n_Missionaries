from node import Node


class Action:
    def __init__(self, fn_name: str, fn_action) -> None:
        self.fn_name = fn_name
        self.fn_callable = fn_action


def apply_action(state: Node, action: Action):
    left_missionaries = state.left_missionaries
    left_cannibals = state.left_cannibals
    right_missionaries = state.right_missionaries
    right_cannibals = state.right_cannibals
    posterior = action.fn_callable(left_missionaries, left_cannibals,
                                   right_missionaries, right_cannibals)
    return(posterior)


def try_action(root, action: Action):
    try:
        left_missionaries, left_cannibals, right_missionaries, right_cannibals = apply_action(
            root.node, action)
    except ValueError:
        return()
    return(left_missionaries, left_cannibals, right_missionaries, right_cannibals)
