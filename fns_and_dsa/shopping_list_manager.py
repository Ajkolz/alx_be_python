

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter name of item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to shopping list")

        elif choice == '2':
            item = input("Enter name of item to remove: ")
            if item in shopping_list: 
                shopping_list.remove(item)
                print(f"{item} has been removed from shopping list")
            else: 
                print("item not found on the list")

        elif choice == '3':
            if shopping_list:
                print("\nCurrent shopping list:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("No item on shopping list")
            

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1 to 4.")

if __name__ == "__main__":
    main()
