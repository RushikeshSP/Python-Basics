# 13)	 Menu-driven Python Program to store, update and delete contact numbers. (Look up what menu-driven means.)


class contacts:
    # Contact list of all contacts
    Contact_list = {}

    # Function to add/store a new contact.
    def addContact(self):
        name = input("\nEnter the Name : ")
        number = int(input("Enter the number : "))
        if(name in contacts.Contact_list or number in contacts.Contact_list.values() or len(str(number))!=10):
            if(name in contacts.Contact_list):
                print(f"\nContact with name {name} is already Exist")
            if(number in contacts.Contact_list.values()):
                print(f"\nContact with Number {number} is already Exist")
            if(len(str(number))!=10):
                print("\nEnter Valid number with 10 digits.")
        else:
            contacts.Contact_list[name] = number
            print("\nNew Contact is added...")

            print("The Contacts list is : ")
            print(contacts.Contact_list)

    # Function to Update an Existing Contact.
    def updateContact(self):
        name = input("\nEnter the contact Name which you want to update : ")
        if(name not in contacts.Contact_list):
            print(f"\nContact with name {name} is Not Exist.")
        else:
            new_name = input("\nEnter the Updated Name : ")
            new_number = int(input("Enter the Updated Number : "))
            if(len(str(new_number))!=10):
                if(len(str(new_number))!=10):
                    print("\nEnter Valid number with 10 digits.")
            else:
                contacts.Contact_list.pop(name)
                contacts.Contact_list[new_name] = new_number
                print("\nContact Updated Successfully...")

                print("The Contacts list is : ")
                print(contacts.Contact_list)

    # Function to Delete an Contact.
    def deleteContact(self):
        name = input("\nEnter the Contact Name which you want to Delete : ")
        if(name not in contacts.Contact_list):
            print(f"\nContact with name {name} is Not Exist.")
        else:
            contacts.Contact_list.pop(name)
            print("\nContact Deleted Successfully...")

            print("The Contacts list is : ")
            print(contacts.Contact_list)

def main():
    choice = 1
    obj = contacts()

    # Menu of the program
    while(choice!=0):
        print("\nSelect One Choice from following... ")
        print("0. To Stop")
        print("1. To Store a New Contact.")
        print("2. To Update an Existing Contact.")
        print("3. To Delete a Contact.")
        choice = int(input("Enter Choice : "))

        if (choice == 1):
            obj.addContact()
        elif (choice == 2):
            obj.updateContact()
        elif (choice == 3):
            obj.deleteContact()
        elif (choice == 0):
            break
        else:
            print("Invalid Choice...")


if __name__ == "__main__":
    main()
