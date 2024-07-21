class List:
    __head = None
    __tail = None

    def __init__(self):
        self.next = None
        self.prev = None

    def append(self, data):
        list = List()
        list.data = data
        list.prev = self.__head
        if self.__head:
            self.__head.next = list
        else:
            list.next = None
            self.__tail = list
        self.__head = list

    def insert(self, number, data):
        list = List()
        list.data = data
        if number == 0:
            self.__tail.prev = list
            list.next = self.__tail
            list.prev = None
            self.__tail = list
        elif number == -1:
            self.__head.next = list
            list.prev = self.__head
            list.next = None
            self.__head = list
        else:
            if number > 0:
                k = 0
                header = self.__tail
                while k != number:
                    k += 1
                    if header.next:
                        header = header.next
                    else:
                        self.__head.next = list
                        list.next = None
                        list.prev = self.__head
                        self.__head = list
                        return
            elif number < 0:
                k = -1
                header = self.__head
                while k != number:
                    k -= 1
                    if header.prev:
                        header = header.prev
                    else:
                        self.__tail.prev = list
                        list.next = self.__tail
                        list.prev = None
                        self.__tail = list
                        return
            list.prev = header
            list.next = header.next
            header.next.prev = list
            header.next = list

    def pop(self, element=-1):
        if element == 0:
            data = self.__tail.data
            self.__tail = self.__tail.next
            self.__tail.prev = None
        else:
            try:
                if element > 0:
                    header = self.__tail
                    k = 0
                    while k != element:
                        k += 1
                        header = header.next
                elif element < 0:
                    header = self.__head
                    k = -1
                    while k != element:
                        k -= 1
                        header = header.prev
                data = header.data
                if header == self.__head:
                    self.__head = header.prev
                    self.__head.next = None
                elif header == self.__tail:
                    self.__tail = header.next
                    self.__tail.prev = None
                else:
                    header.next.prev = header.prev
                    header.prev.next = header.next
            except:
                raise IndexError('List index out of range')
        return data


if __name__ == '__main__':
    """РАБОТАЕТ"""
    lst = List()
    lst.append('hello')
    lst.append(908)
    lst.append('egor')
    lst.insert(7, 'qwerty')
    print(lst.pop())
    lst.append('304')
    print(lst.pop())
