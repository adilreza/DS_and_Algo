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

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
        else:
            print(f"Key '{key}' not found in the linked list.")

    def delete(self, key):
        if self.is_empty():
            print("Linked list is empty.")
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                break
            current = current.next
        else:
            print(f"Key '{key}' not found in the linked list.")

    def display(self):
        if self.is_empty():
            print("Linked list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.append(60)

linked_list.display()
linked_list.prepend(5)
linked_list.display()
linked_list.insert_after(40, 45)
linked_list.display()
linked_list.delete(10)
linked_list.display()
