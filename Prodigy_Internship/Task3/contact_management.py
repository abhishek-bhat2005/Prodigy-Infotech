import json

# Load contacts from file
def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit contact
def edit_contact(contacts):
    view_contacts(contacts)
    choice = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= choice < len(contacts):
        contacts[choice]['name'] = input("Enter new name: ")
        contacts[choice]['phone'] = input("Enter new phone number: ")
        contacts[choice]['email'] = input("Enter new email address: ")
        print("Contact updated successfully!")
    else:
        print("Invalid selection!")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    choice = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= choice < len(contacts):
        contacts.pop(choice)
        print("Contact deleted successfully!")
    else:
        print("Invalid selection!")

# Main program loop
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
