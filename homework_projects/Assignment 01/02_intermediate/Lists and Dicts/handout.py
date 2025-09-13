# Program 1

def main():
    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]
    print(len(fruit_list))
    fruit_list.append("Mango")
    print(fruit_list)

main()    

# Program 2

my_list = [10, "apple", 3.14, "banana", 42]

def access_element(lst, index):
    if 0 <= index :
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    if 0 <= index :
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'"
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Start or end index out of range!"
    else:
        return lst[start:end]

def index_game():
    while True:
        print("\nCurrent list:", my_list)
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            try:
                idx = int(input("Enter index to access: "))
                print(access_element(my_list, idx))
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "2":
            try:
                idx = int(input("Enter index to modify: "))
                new_val = input("Enter new value: ")
                print(modify_element(my_list, idx, new_val))
            except ValueError:
                print("Invalid input!")
        
        elif choice == "3":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "4":
            print("Thanks for playing! 👋")
            break
        else:
            print("Invalid choice. Try again!")

index_game()