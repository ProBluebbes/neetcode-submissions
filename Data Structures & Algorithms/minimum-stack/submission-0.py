class MinStack:

    def __init__(self):
        self._min = []
        self._list = []


    def push(self, val: int) -> None:
        self._list.append(val)
        if (len(self._min) > 0):
            self._min.append(min(self._min[-1], val))
        else:
            self._min.append(val)

    def pop(self) -> None:
        self._list.pop()
        self._min.pop()

    def top(self) -> int:
        return self._list[-1]

    def getMin(self) -> int:
        return self._min[-1]