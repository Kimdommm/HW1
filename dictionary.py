def main():
    # Create an empty dictionary
    mydict = {}

    # Initialize shopping items
    items = ["underwear", "tank top", "jacket"]
    for i, item in enumerate(items):
        mydict[i] = item

    print(f"You have {len(mydict)} items in the cart")

    while True:
        action = input(
            "\nWhat would you like to do [A]dd [C]hange items [R]emove [D]isplay S[earch] ?  "
        ).strip().lower()

        if action == "d":
            print("\nDisplaying Values")
            print("Key      Value")
            for k, v in mydict.items():
                print(f"{k:<9}{v}")

        elif action == "s":
            key_or_value = input("\nEnter item to search (key or value): ")

            # Try search by key (if numeric input)
            if key_or_value.isdigit():
                key = int(key_or_value)
                value = mydict.get(key)
                if value is not None:
                    print(f"Found {value} item")
                else:
                    print("Im sorry, not in the cart")
            else:
                # Search by value
                found = False
                for k, v in mydict.items():
                    if v.lower() == key_or_value.lower():
                        print(f"Found {v} item")
                        found = True
                        break
                if not found:
                    print("Im sorry, not in the cart")

        elif action == "r":
            key_to_remove = input("\nEnter key to search: ")
            if key_to_remove.isdigit():
                key_to_remove = int(key_to_remove)
                value = mydict.pop(key_to_remove, None)
                if value is not None:
                    print(f"The key {key_to_remove} with value {value} has been deleted")
                else:
                    print("Key not found")
            else:
                print("Key not found")

        elif action == "c":
            key_to_change = input("\nEnter key to search: ")
            if key_to_change.isdigit():
                key_to_change = int(key_to_change)
                value = mydict.get(key_to_change)
                if value is not None:
                    print(f"Found {value} item")
                    new_value = input("Enter value: ")
                    mydict[key_to_change] = new_value
                else:
                    print("Im sorry, not in the cart")
            else:
                print("Im sorry, not in the cart")

        elif action == "a":
            new_value = input("\nEnter item to add: ")
            # New key will be next available integer
            new_key = max(mydict.keys(), default=-1) + 1
            mydict[new_key] = new_value
            print(f"Added {new_value} with key {new_key}")

        elif action == "*":
            print("Bye")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
