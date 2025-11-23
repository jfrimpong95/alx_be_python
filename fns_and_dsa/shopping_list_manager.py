# shopping_list_manager.py

def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")


def main():
    shopping_list = []  # start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        # Add item
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"✔ '{item}' has been added to the shopping list.")

        # Remove item
        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"✔ '{item}' has been removed from the shopping list.")
            else:
                print(f"❌ '{item}' is NOT in the shopping list.")

        # View list
        elif choice == "3":
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nYour shopping list is empty.")

        # Exit the program
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye! 👋")
            break

        # Handle invalid choices
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
