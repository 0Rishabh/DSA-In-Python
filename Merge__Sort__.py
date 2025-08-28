

# Merge Sort implemented in Python

# Python program for Merge Sort with menu options







class Merge_Sort():

    def merge_sort_code(self,arr):

        if len(arr) > 1:

            mid = len(arr)//2
            left_arr = arr[:mid] 
            right_arr = arr[mid:]

            self.merge_sort_code(left_arr)
            self.merge_sort_code(right_arr)

            i = j = k = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i+=1

                else:
                    arr[k] = right_arr[j]
                    j+=1

                k+=1


            while i < len(left_arr):
                arr[k] = left_arr[i]
                i+=1
                k+=1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j+=1
                k+=1

def choice_menu():
    print('\n...... Welcome To Merge Sort Menu ......\n')
    print('\t1. Sort A List ')
    print('\t2. Exit ')
    try:
        return int(input("\nEnter Your Choice: "))
    except ValueError:
        return 0
    
def main():
    ms = Merge_Sort()
    while True:
        choice = choice_menu()

        if choice == 1:
            data = input("Enter numbers separated by space: ")
            arr = list(map(int, data.split()))
            ms.merge_sort_code(arr)
            print()
            print(f"Sorted list: {arr}")

        elif choice == 2:
            print("Exiting program.. Goodbye!.......... ")
            break

        else:
            print("\nInvalid choice. Please try again. ")           


if __name__ == "__main__":
    main()
