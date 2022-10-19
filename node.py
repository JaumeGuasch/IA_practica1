class Node:
    def __init__(self, _state, _parent=None, _action=None, _cost=0):
        self.state = _state
        self.parent = _parent
        self.action = _action
        self.cost = _cost

    # quan jo estic en un punt puc veure l'acció que m'ha portat allí
    # No puc veure els meus successors
    def total_path(self):
        if not self.parent:
            return []
        return self.parent.total_path() + [self.action]  # action es la última acció que va del meu pare a mi

    def __str__(self):
        # TODO implement, default behaviour:
        return f"Node[{self.state}, {self.action}, {self.cost}]"


# sudo apt install python3-tkinter

def test_robot():
    # For the problem of the robot cleaning two cells
    from collections import namedtuple
    State = namedtuple("State", "cell clean0 clean1")

    root = Node(State(0, False, False))
    step1 = Node(
        State(0, True, False),
        root, "SWEEP"
    )
    step2 = Node(
        State(1, True, False),
        step1, "MOVE"
    )
    step3_1 = Node(
        State(0, True, False),
        step2, "MOVE"
    )
    step3_2 = Node(
        State(1, True, True),
        step2, "SWEEP"
    )

    print(root)
    print(step1)
    print(step3_1.total_path())
    print(step3_2.total_path())


if __name__ == "__main__":
    test_robot()
