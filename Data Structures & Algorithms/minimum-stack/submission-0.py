class MinStack:

    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, val: int) -> None:
        self.items.append(val)

        if not self.min_items:
            self.min_items.append(val)
        else:
            current_min = self.min_items[-1]
            self.min_items.append(min(val, current_min))

    def pop(self) -> None:
        self.items.pop()
        self.min_items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_items[-1]