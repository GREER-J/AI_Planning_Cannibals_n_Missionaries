class Node:
    def __init__(self,  left_missionaries: int, left_cannibals: int, right_missionaries: int, right_cannibals: int) -> None:
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.right_missionaries = right_missionaries
        self.right_cannibals = right_cannibals
        self.state = f"[L({self.left_missionaries}, {self.left_cannibals}), R({self.right_missionaries}, {self.right_cannibals})]"
        if(self.left_cannibals > self.left_missionaries or self.right_cannibals > self.right_missionaries):
            self.valid = False
        else:
            self.valid = True

    def __repr__(self) -> str:
        return(self.state)
