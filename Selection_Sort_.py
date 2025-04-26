


def selection_sort(data_list):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i], data_list[min_index] = data_list[min_index],data_list[i]


choice = input("Do you want to sort integers or strings? (int/str): ").strip().lower()

if choice == "int":
    nums = input("Enter integers separated by spaces: ")
    data = list(map(int, nums.split()))
    selection_sort(data)
    print("Sorted integers:", data)

elif choice == "str":
    words = input("Enter strings separated by spaces: ")
    data = words.split()
    selection_sort(data)
    print("Sorted strings:", data)

else:
    print("Invalid choice! Please enter 'int' or 'str'.")

