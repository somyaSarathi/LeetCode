class MyQueue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()
        

    def push(self, x: int) -> None:
        # if queue(reverse stack) not empty
        if self.s2:
            while self.s2:
                self.s1.append( self.s2.pop( len(self.s2) - 1 ) )

        self.s1.append(x)

        while self.s1:
            self.s2.append( self.s1.pop( len(self.s1) - 1 ) )
        

    def pop(self) -> int:
        return self.s2.pop( len(self.s2) - 1 )
        

    def peek(self) -> int:
        return self.s2[-1]
        

    def empty(self) -> bool:
        return not(bool(self.s2))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()