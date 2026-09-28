mobiles = []


def add_mobile():
    mobile_id = int(input("Enter mobile ID: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("Mobile ID already exists.")
            return

    brand = input("Enter brand: ")
    model = input("Enter model: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    mobiles.append([mobile_id, brand, model, price, quantity])

    print("Mobile added successfully.")


def display_mobiles():
    if not mobiles:
        print("No mobiles available.")
        return

    print("\nID\tBrand\t\tModel\t\tPrice\tQuantity")

    for mobile in mobiles:
        print(
            mobile[0], "\t",
            mobile[1], "\t\t",
            mobile[2], "\t\t",
            mobile[3], "\t",
            mobile[4]
        )


def search_mobile():
    mobile_id = int(input("Enter mobile ID to search: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile found")
            print("ID:", mobile[0])
            print("Brand:", mobile[1])
            print("Model:", mobile[2])
            print("Price:", mobile[3])
            print("Quantity:", mobile[4])
            return

    print("Mobile not found.")


def update_mobile():
    mobile_id = int(input("Enter mobile ID to update: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            mobile[1] = input("Enter new brand: ")
            mobile[2] = input("Enter new model: ")
            mobile[3] = float(input("Enter new price: "))
            mobile[4] = int(input("Enter new quantity: "))

            print("Mobile updated successfully.")
            return

    print("Mobile not found.")


def delete_mobile():
    mobile_id = int(input("Enter mobile ID to delete: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            choice = input("Are you sure? (y/n): ")

            if choice.lower() == "y":
                mobiles.remove(mobile)
                print("Mobile deleted successfully.")
            else:
                print("Delete cancelled.")

            return

    print("Mobile not found.")


def main():
    while True:
        print("\n--- Mobile Shop ---")
        print("1. Add Mobile")
        print("2. Display Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_mobile()

        elif choice == "2":
            display_mobiles()

        elif choice == "3":
            search_mobile()

        elif choice == "4":
            update_mobile()

        elif choice == "5":
            delete_mobile()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()