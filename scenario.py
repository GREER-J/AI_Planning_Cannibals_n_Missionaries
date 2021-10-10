class State:
    """ Class describing a state of the world
    """

    def __init__(self, left_missionaries: int, left_cannibals: int, right_missionaries: int, right_cannibals: int) -> None:
        self.left_cannibals = left_cannibals
        self.left_missionaries = left_missionaries
        self.right_cannibals = right_cannibals
        self.right_missionaries = right_missionaries

        # Check fail condition
        if(left_cannibals > left_missionaries or right_cannibals > right_missionaries):
            self.valid = False
        else:
            self.valid = True

        self.state = "(L:({}c{}m), R({}c{}m))".format(
            self.left_cannibals, self.left_missionaries, self.right_cannibals, self.right_missionaries)

    def __repr__(self) -> str:
        return(self.state)


class Action:
    def __init__(self, action_name: str, fn_action) -> None:
        self.name = action_name
        self.fn = fn_action


def fn_move_1m1c(left_missionaries: int, left_cannibals: int, right_missionaries: int, right_cannibals: int):
    if(left_missionaries >= 1 and left_cannibals >= 1):
        left_missionaries -= 1
        left_cannibals -= 1
        right_missionaries += 1
        right_cannibals += 1
    else:
        raise ValueError("You can't complete the action")
    return(left_missionaries, left_cannibals, right_missionaries, right_cannibals)


def fn_move_2c(left_missionaries: int, left_cannibals: int, right_missionaries: int, right_cannibals: int):
    if(left_cannibals >= 2):
        left_cannibals -= 2
        right_cannibals += 2
    else:
        raise ValueError("You can't complete the action")
    return(left_missionaries, left_cannibals, right_missionaries, right_cannibals)


def fn_move_2m(left_missionaries: int, left_cannibals: int, right_missionaries: int, right_cannibals: int):
    if(left_missionaries >= 2):
        left_missionaries -= 2
        right_missionaries += 2
    else:
        raise ValueError("You can't complete the action")
    return(left_missionaries, left_cannibals, right_missionaries, right_cannibals)


def apply_action(state: State, action: Action):
    left_missionaries = state.left_missionaries
    left_cannibals = state.left_cannibals
    right_missionaries = state.right_missionaries
    right_cannibals = state.right_cannibals
    posterior = action.fn(left_missionaries, left_cannibals,
                          right_missionaries, right_cannibals)
    return(posterior)


def create_actions():
    mv_1m1c = Action("1m1c", fn_move_1m1c)
    mv_2m = Action("2m", fn_move_2m)
    mv_2c = Action("2c", fn_move_2c)

    actions = [mv_2m, mv_1m1c, mv_2c]
    return(actions)
