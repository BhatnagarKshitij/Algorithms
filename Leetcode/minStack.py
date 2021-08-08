class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.minstack) == 0 or val <= self.minstack[-1]:
            self.minstack.append(val) 
        self.stack.append(val)
        

    def pop(self) -> None:
        pop = self.stack.pop()
        if self.minstack[-1] == pop:
            self.minstack.pop()
        
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
