


def insertion_sort(data_list):
    for i in range(1,len(data_list)):
        temp = data_list[i]
        j = i-1
        while j>=0 and temp < data_list[j]:
            data_list[j+1] = data_list[j]
            j-=1

        data_list[j+1] = temp

choice = input("Do you want to sort integers or strings? (int/str): ").strip().lower()

if choice == "int":
    nums = input("Enter integers separated by spaces: ")
    data = list(map(int, nums.split()))
    insertion_sort(data)
    print("Sorted integers:", data)

elif choice == "str":
    words = input("Enter strings separated by spaces: ")
    data = words.split()
    insertion_sort(data)
    print("Sorted strings:", data)

else:
    print("Invalid choice! Please enter 'int' or 'str'.")


