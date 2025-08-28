

# his project implements the **Quick Sort algorithm** in Python using an **object-oriented approach**.  
# It also includes a **menu-driven interface** that allows users to:
# - Enter a new list
# - Sort the current list using Quick Sort
# - Display the current list
# - Exit the program







class QuickSort:
    def __init__(self):
        self.arr = []

    def quick_sort(self, arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1

        if left < right:
            pivot = arr[left]
            i, j = left, right

            # Partition logic
            while i < j:
                while arr[i] <= pivot and i < right:
                    i += 1
                while arr[j] > pivot and j > left:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]

            arr[left], arr[j] = arr[j], arr[left]

            # Recursive calls
            self.quick_sort(arr, left, j - 1)
            self.quick_sort(arr, j + 1, right)

    def take_input(self):
        # Taking input from user
        n = int(input("Enter number of elements: "))
        self.arr = []
        print("Enter elements:")
        for _ in range(n):
            val = int(input())
            self.arr.append(val)

    def choice_menu(self):
        while True:
            print("\n------ Quick Sort Menu ------")
            print("\t1. Enter a new list")
            print("\t2. Sort current list")
            print("\t3. Display current list")
            print("\t4. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 1:
                self.take_input()
            elif choice == 2:
                if not self.arr:
                    print("List is empty! Please enter elements first.")
                else:
                    self.quick_sort(self.arr)
                    print("List sorted successfully!")
            elif choice == 3:
                print("Current List:", self.arr)
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Try again.")


# Run the menu
if __name__ == "__main__":
    sorter = QuickSort()
    sorter.choice_menu()
