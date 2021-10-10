from action import Action


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


def create_actions():
    mv_1m1c = Action("1m1c", fn_move_1m1c)
    mv_2m = Action("2m", fn_move_2m)
    mv_2c = Action("2c", fn_move_2c)

    actions = [mv_2m, mv_1m1c, mv_2c]
    return(actions)
