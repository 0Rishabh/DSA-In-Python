
## Circular linked list

class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self,last = None):
        self.last = last

    
    def insert_at_start(self,data):
        n = Node(data)
        if self.last is None:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self,data):
        if self.last is not None:
            n = Node(data,self.last.next)
            self.last.next = n
            self.last = n
        else:
            n = Node(data)
            n.next = n
            self.last = n

    def print_item(self):
        if self.last is not None:
            temp = self.last.next
            while temp!= self.last:
                print(temp.item,end=' ')
                temp = temp.next

            print(temp.item,end=' ')
        else:
            print("The list is empty:")
        
    def insert_at_mid(self,afterdata,data):
        if self.last is not None:
            temp = self.last.next
            while temp is not self.last:
                if temp.item == afterdata:
                    n = Node(data,temp.next)
                    temp.next = n
                    break
                temp = temp.next
            if temp.item == afterdata:
                if temp == self.last:
                    n = Node(data,self.last.next)
                    self.last.next = n
                    self.last = n

    def delete_at_start(self):
        if self.last is not None:
            if self.last.next != self.last:
                self.last.next = self.last.next.next
            else:
                self.last = None

    def delete_at_last(self):
        if self.last is not None:
    
            if self.last == self.last.next:
                self.last = None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp = temp.next

                temp.next = self.last.next
                self.last = temp



    def delete_at_mid(self,data):
        if self.last is not None:
            if self.last.next.item == data:
                if self.last == self.last.next:
                    self.last = None
                else:
                    self.last.next = self.last.next.next

            else:
                temp = self.last.next
                while temp != self.last:
                    if temp.next.item == data:
                        if temp.next == self.last:
                            self.last = temp

                        temp.next = temp.next.next

                        break
                    temp = temp.next

if __name__ == "__main__":
    linked_list = CLL()

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
            linked_list.insert_at_start(data)
        elif choice == 2:
            data = int(input("Enter data to insert at last: "))
            linked_list.insert_at_last(data)
        elif choice == 3:
            after_data = int(input("Enter the data after which to insert: "))
            data = int(input("Enter data to insert: "))
            linked_list.insert_at_mid(after_data, data)
        elif choice == 4:
            linked_list.delete_at_start()
        elif choice == 5:
            linked_list.delete_at_last()
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            linked_list.delete_at_mid(data)
        elif choice == 7:
            linked_list.print_item()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")
            break

            
