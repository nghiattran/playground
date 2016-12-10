class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def append(self, node):
        if self.next is None:
            self.next = node
        else:
            tmp = self
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node
        return self


def delete(head, value):
    if head is None:
        print('Nothing to delete')
        return head

    if head.data == value:
        return head.next

    tmp = head
    while tmp.next is not None:
        if tmp.next.data == value:
            tmp.next = tmp.next.next
            return head
        tmp = tmp.next
    return head


def remove_duplicate(head):
    tmp = head
    dict = {head.data : 0}

    while tmp.next is not None:
        if tmp.next.data in dict:
            tmp.next = tmp.next.next
        else:
            dict[tmp.next.data] = 0
            tmp = tmp.next


def print_list(head):
    tmp = head
    print(tmp.data, end=' ')
    while tmp.next is not None:
        print(tmp.next.data, end=' ')
        tmp = tmp.next
    print()


def get_n_last(head, n):
    tmp = head
    dict = {0: head}
    counter = 1

    while tmp.next is not None:
        dict[counter] = tmp.next
        counter += 1
        tmp = tmp.next
    return dict[counter - n]


def delete_node(node):
    if node.next is None:
        print("Can't to that")
        return

    node.data = node.next.data
    node.next = node.next.next


def add_list(list1, list2):
    first = list1
    second = list2
    zero = Node(0)

    value = (first.data + second.data) % 10
    tmp = int((first.data + second.data) / 10)

    head = Node(value)
    while first.next is not None or second.next is not None or tmp > 0:
        first = first.next if first.next is not None else zero
        second = second.next if second.next is not None else zero

        value = (first.data + second.data + tmp) % 10
        tmp = int((first.data + second.data + tmp) / 10)
        head.append(Node(value))
    return head


def add_list1(list1, list2):
    first = list1
    first_string = ''
    while first is not None:
        first_string = str(first.data) + first_string
        first = first.next

    second = list2
    second_string = ''
    while second is not None:
        second_string = str(second.data) + second_string
        second = second.next

    total = int(first_string) + int(second_string)
    head = None
    for char in str(total):
        if head is None:
            head = Node(int(char))
        else:
            head.append(Node(int(char)))
    return head


def detect_circular(list):
    tmp = list
    dict = {}
    while tmp is not None:
        if tmp in dict:
            return tmp
        dict[tmp] = None
        tmp = tmp.next
    return None

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(1)
# node6 = Node(4)
# node7 = Node(5)
# node8 = Node(1)
# node9 = Node(1)
# node10 = Node(1)
# node1.append(node2).append(node3).append(node4).append(node5).append(node6).append(node7).append(node8).append(node9).append(node10)


# print_list(node1)
# delete(node1, 4)
# delete(node1, 3)
# remove_duplicate(node1)
# print_list(node1)
# delete_node(node7)
# print_list(node1)
# print(get_n_last(node1, 5).data)

# list1 = Node(3).append(Node(1))
# list2 = Node(5).append(Node(9)).append(Node(2))
# head = add_list1(list1, list2)
# print_list(head)

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeE
nodeE.next = nodeA



# print(detect_circular(nodeA).data)