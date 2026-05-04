class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minimum.append(val)
        else:
            self.stack.append(val)
            self.minimum.append(min(self.minimum[-1],val))

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minimum.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
