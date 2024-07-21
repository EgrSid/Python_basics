class Stack:
    def __init__(self):
        self.head = None
        self.next = None
        self.data = None

    def push(self, data):
        stack = Stack()
        stack.data = data
        stack.next = self.head
        self.head = stack

    def pop(self):
        """Дополнительно возвращает удалённое значение"""

        data = self.head.data
        self.head = self.head.next
        return data


if __name__ == '__main__':
    s = Stack()
    s.push('hello')
    s.push('12')
    s.push('egor')

    print(s.pop())
    print(s.pop())
    s.push('privet')
    s.push('xyz')

    print(s.pop())
