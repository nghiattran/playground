class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    top = None
    items = 0

    def __init__(self):
        self.values = []

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.items += 1

    def pop(self):
        if self.top is not None:
            data = self.top.data
            self.top = self.top.next
            self.items -= 1
            return data
        return None

    def peek(self):
        return self.top.data

class SetOfStack(Stack):
    threshold = 3
    top = None

    def peek_stack(self):
        return self.top.data

    def peek(self):
        return self.top.data.peek()

    def push(self, value):
        if self.top is None or self.peek_stack().items >= self.threshold:
            super(SetOfStack, self).push(Stack())
        self.peek_stack().push(value)

    def pop(self):
        if self.top is None:
            return None

        if self.peek_stack().items > 0:
            return self.peek_stack().pop()
        else:
            return super(SetOfStack, self).pop().pop()


def hanoi(n, source, helper, target):
    # print("hanoi( ", n, source, helper, target, " called")
    if n > 0:
        hanoi(n - 1, source, target, helper)

        disk = source[0].pop()
        print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
        target[0].append(disk)
        hanoi(n - 1, helper, source, target)


source = ([2, 1], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]), source, helper, target)

print(source, helper, target)