contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"\n Contact for {name} added successfully!\n")

def view_contacts():
    if not contacts:
        print("\n No contacts found.\n")
        return
    print("\n Contact List:")
    for name, info in contacts.items():
        print(f"\n Name: {name}")
        for key, value in info.items():
            print(f"   {key}: {value}")
    print()

def search_contact():
    search_name = input(" Enter name to search: ")
    if search_name in contacts:
        print(f"\n Contact found:\nName: {search_name}")
        for key, value in contacts[search_name].items():
            print(f"{key}: {value}")
    else:
        print(f"\n Contact '{search_name}' not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("\nEnter new details (leave blank to keep existing):")
        phone = input(f"Phone [{contacts[name]['Phone']}]: ") or contacts[name]['Phone']
        email = input(f"Email [{contacts[name]['Email']}]: ") or contacts[name]['Email']
        address = input(f"Address [{contacts[name]['Address']}]: ") or contacts[name]['Address']
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"\n Contact for {name} updated successfully!\n")
    else:
        print(f"\n Contact '{name}' not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"\n Contact '{name}' deleted successfully!\n")
    else:
        print(f"\n Contact '{name}' not found.\n")

def contact_menu():
    while True:
        print("======= 📘 CONTACT BOOK MENU =======")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" !Invalid choice. Please select from 1 to 6.\n")


contact_menu()
