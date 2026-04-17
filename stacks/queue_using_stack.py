class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # def __repr__(self) -> str:
    #     return str(self.__dict__)

    def push(self, x: int) -> None:
        self.stack1.append(x)
        return
        
    def pop(self) -> int:
        if self.stack2:
            popped_num = self.stack2.pop()
        else:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
            popped_num = self.stack2.pop()
        return popped_num

    def peek(self) -> int:
        if self.stack2:
            peek = self.stack2[-1]
        else:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
            peek = self.stack2[-1]
        return peek

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()