contacts = [
    {
        "name" : "Alice",
        "phone" : 739558836,
        "email" : "oba@gmail.com"
    }
]

def add_contact(contact_list, name, phone, email):
    add = {
        "name" : name, 
        "phone" : phone,
        "email" : email
    }
    contact_list.append(add)
    return contact_list

def search_contact(name):
    search_name = name.lower().strip()
    for contact in contacts:
        if contact["name"].lower() == search_name:
            return contact
    return None

def delete_contact(name):
    search_name = name.lower().strip()
    for index, contact in enumerate(contacts):
        if contact["name"].lower() == search_name:

            removed = contacts.pop(index)
            print(f"Success: {removed['name']} has been deleted.")
            return True
    print(f"Error: Contact '{name}' not found.")
    return False
    
def view_all():
    if not contacts:
        print("\n---- No Contacts found in the database ---")
        return


    print(f"\n{'Name':<20} | {'PHONE NUMBER':<15} | {'EMAIL':<25}")
    print("-" * 66)
    
  
    for contact in contacts:
        print(f"{contact['name']:<20} | {str(contact['phone']):<15} | {contact['email']:<25}")
    print("-" * 66 + "\n")
    
while True:
    choice = input("\nEnter a choice: \n1) Add \n2) Search \n3) Delete \n4) View all \n5) Exit \n")
    
   
    if choice == "1":

        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        add_contact(contacts, name, phone, email)
        print(f"Contact '{name}' added successfully!")
        
    elif choice == "2":
        name_to_search = input("Enter name to search: ")
        found = search_contact(name_to_search)
        if found:
            print(f"\nFound: {found['name']} | {found['phone']} | {found['email']}")
        else:
            print("\nContact not found.")
        
    elif choice == "3":
        name_to_delete = input("Enter name to delete: ")
        delete_contact(name_to_delete)
        
    elif choice == "4":
        view_all()
    
    elif choice == "5":
        print("Exiting application. Goodbye!")
        break  
        
    else:
        print("Please enter a valid input")

    
