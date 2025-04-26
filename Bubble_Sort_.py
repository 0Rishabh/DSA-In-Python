



def Bubble_sort(data):
    for i in range(1, len(data)):
        flag = False
        for j in range(len(data) - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        if not flag:
            break

choice = input("Do you want to sort integers or strings? (int/str): ").strip().lower()

if choice == "int":
    nums = input("Enter integers separated by spaces: ")
    data = list(map(int, nums.split()))
    Bubble_sort(data)
    print("Sorted integers:", data)

elif choice == "str":
    words = input("Enter strings separated by spaces: ")
    data = words.split()
    Bubble_sort(data)
    print("Sorted strings:", data)

else:
    print("Invalid choice! Please enter 'int' or 'str'.")


