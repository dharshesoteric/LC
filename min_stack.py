class MinStack:

    def __init__(self):
        
        self.Stack = []
        self.min_stack = [] #Maintaining a secondary stack to prefix the local minimum for each index of the stack

    def push(self, val: int) -> None:
        
        self.Stack.append(val)
        
        if not self.min_stack:
            self.min_stack.append(val) #First val does not need any conditional check and is always the minimum
        else:
            if val < self.min_stack[-1]:
                self.min_stack.append(val) #Updating the local minimum if only the current val param is lesser than the current min stack val
            else:
                self.min_stack.append(self.min_stack[-1]) #If the val param is not lesser than the running min, we update the same to the current iter
                        
    def pop(self) -> None:

        if not self.Stack:
            return
        else:
            self.Stack.pop()
        
        if not self.min_stack:
            return 
        else:
            self.min_stack.pop()


    def top(self) -> int:

        if not self.Stack:
            return
        else:
            return self.Stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return
        else:
            return self.min_stack[-1]