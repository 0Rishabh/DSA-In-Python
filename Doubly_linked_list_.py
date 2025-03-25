
##  Doubly Linked List using Python Code

class Node:
    def __init__(self,prev = None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start=None):
        self.start = start


    def insert_at_start(self,data):
        n = Node(None,data,self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n

    def insert_at_last(self,data):
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            n = Node(temp,data,None)
            temp.next = n
        else:
            n = Node(None,data,None)
            self.start = n

    
    def insert_at_mid(self,afterdata,data):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                if temp.item==afterdata:
                    n = Node(temp,data,temp.next)
                    
                    if temp.next is not None:
                       n.next.prev = n
                    temp.next = n
                temp = temp.next

    def delete_at_start(self):
        if self.start is not None:
            temp = self.start
            if temp.next is None:
                self.start = None
            else:
                 temp.next.prev = None
                 self.start = temp.next
                 temp.next = None
            

    def delete_at_last(self):
        if self.start is not None and self.start.next is not None:
            temp = self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next = None
            temp.prev = None # Not requirment 
           
    def delete_at_mid(self,data):
        if self.start is not None:
            if self.start.item == data:
                self.start = self.start.next
                if self.start is not None:
                     self.start.prev = None
            else:
               temp = self.start
               while temp is not None:
                   if temp.item == data:
                       temp.prev.next = temp.next
                       if temp.next is not None:
                           temp.next.prev = temp.prev
                       temp = None
                       break
    
                   temp = temp.next
        


    def print_item(self):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                print(temp.item,end=' ')
                temp = temp.next

        else:
            print("The list is empty")




if __name__ == "__main__":
    linked_list = DLL()

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


