name = []
contact_number = []

def add():
    name.append(input("Enter the name: "))
    contact_number.append(input("Enter the contact number: "))
    print(name, contact_number)
    print("Successfully added!")

def serch():
    search_name = input("Enter the name: ")
    if search_name in name:
        print("Name: ", search_name, "Contact number: ", contact_number[name.index(search_name)])
    else:
        print("Name not found!")

def delete():
    delete_name = input("Enter the name: ")
    if delete_name in name:
        name.remove(delete_name)
        contact_number.remove(contact_number[name.index(delete_name)])
        print("Successfully deleted!")
    else:
        print("Name not found!")

def update():
    update_name = input("Enter the name: ")
    if update_name in name:
        contact_number[name.index(update_name)] = input("Enter the new contact number: ")
        print("Successfully updated!")
    else:
        print("Name not found!")

def display():
    print(name, contact_number)

while True:
    print("1. Add\n2. Search\n3. Delete\n4. Update\n5. Display\n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        serch()
    elif choice == 3:
        delete()
    elif choice == 4:
        update()
    elif choice == 5:
        display()
    elif choice == 6:
        break
    else:
        print("Invalid choice!")

