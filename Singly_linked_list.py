

### Singly linked list using python code



class Node: # Create Node
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_first(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            n = Node(data)
            temp.next = n
        else:
            n = Node(data)
            self.start = n

    def insert_at_mid(self, afterdata, data):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                if temp.item == afterdata:
                    n = Node(data, temp.next)
                    temp.next = n
                    break
                temp = temp.next
        else:
            print("List is empty.")

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
        else:
            print("List is empty.")

    def delete_last(self):
        if self.start is not None:
            if self.start.next is None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            print("List is empty.")

    def delete_mid(self, data):
        if self.start is not None:
            if self.start.item == data:
                self.start = self.start.next
            else:
                temp = self.start
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
        else:
            print("List is empty.")

    def print_item(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    linked_list = SLL()

    while True:
        print("\n__________Choose an operation:__________")
        print("""
            1. Insert at First
            2. Insert at Last
            3. Insert at Middle
            4. Delete First
            5. Delete Last
            6. Delete Middle
            7. Display List
            8. Exit\n""")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at first: "))
            linked_list.insert_at_first(data)
        elif choice == 2:
            data = int(input("Enter data to insert at last: "))
            linked_list.insert_at_last(data)
        elif choice == 3:
            after_data = int(input("Enter the data after which to insert: "))
            data = int(input("Enter data to insert: "))
            linked_list.insert_at_mid(after_data, data)
        elif choice == 4:
            linked_list.delete_first()
        elif choice == 5:
            linked_list.delete_last()
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            linked_list.delete_mid(data)
        elif choice == 7:
            linked_list.print_item()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")
            break




