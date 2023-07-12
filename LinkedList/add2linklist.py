class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.is_empty():
            print("Linked list is empty")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


def add_linked_list(li1, list2):
    result = LinkedList()
    carry = 0
    current1 = list1.head
    current2 = list2.head

    while current1 or current2:
        sum_val = carry
        if current1:
            sum_val = current1.data + sum_val
            current1 = current1.next
        if current2:
            sum_val = current2.data + sum_val
            current2 = current2.next

        carry = sum_val//10
        sum_val = sum_val %10

        result.append(sum_val)

    if carry:
        result.append(carry)
    return result


list1 = LinkedList()
list1.append(12)
list1.append(14)
list1.append(16)
list1.append(18)

list1.display()
print()

list2 = LinkedList()
list2.append(11)
list2.append(13)
list2.append(15)
list2.append(17)

list2.display()

summation = add_linked_list(list1, list2)
print()
summation.display()
