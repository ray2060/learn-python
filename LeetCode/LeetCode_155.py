class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return min(self.items)
