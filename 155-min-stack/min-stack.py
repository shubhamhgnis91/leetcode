class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = self.getMin()

        if minVal is None or minVal > val:
            minVal = val
        
        self.stack.append([val, minVal])
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack) > 0 else None

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) > 0 else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()