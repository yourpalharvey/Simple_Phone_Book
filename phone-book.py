# Used to store the entries in the telephone book
entries = []

# Create flag to decide when the program ix exited
exit_program = False

# Define function for printing the entries' details


def list_entries():
    print("Surname: "+entry['Surname'])
    print("First Name: "+entry['First Name'])
    print("Age: "+str(entry['Age']))
    print("Phone Number: "+str(entry['Phone Number']))
    print("Personal Notes: ")
    # List the notes numerically (1... 2...) to allow for countless notes to be added to an entry
    line = 0
    for notes in entry['Personal Notes']:
        line += 1
        print(str(line) + "." + str(notes))
    print("------------------------------------\n")

# Define function for user inputs


def input_entries(entries):
    surname = input('Enter surname:\n')
    surname = surname.title().replace(" ", "")
    first_name = input('Enter first name:\n')
    first_name = first_name.title().replace(" ", "")
    # Check if age is an integer and in the correct range
    age_flag = True
    while age_flag:
        age = input('Enter age:\n')
        if age.isnumeric() == False:
            print("Incorrect age, please try again")
            continue
        else:
            if int(age) > 150:
                print("Incorrect age, please try again")
                continue
            elif int(age) <= 0:
                print("Incorrect age, please try again")
                continue
            else:
                age_flag = False
    # Check if phone number is integer and 11 digits long
    phone_flag = True
    while phone_flag:
        phone_number = input('Enter phone number:\n')
        if phone_number.isnumeric() == False:
            print("Incorrect phone number, please try again")
            continue
        else:
            if len(phone_number) != 11:
                print("Incorrect phone number, please try again")
                continue
            else:
                phone_flag = False
    personal_notes = []
    # Setting the details as a list
    new_entry = {'Surname': surname, 'First Name': first_name, 'Age': age,
                 'Phone Number': phone_number, 'Personal Notes': personal_notes}
    entries.append(new_entry)


while exit_program == False:
    print("Welcome to the EG-244 Telephone Book")
    print("------------------------------------\n")
    print("Please select from one of the following options:")
    print("\t1. Add a new entry")
    print("\t2. List entries")
    print("\t3. Search for an entry")
    print("\t4. Delete an entry")
    print("\t5. Add a personal note")
    print("\t6. Remove a personal note")
    print("\t7. Quit")

    menu_input = int(input())

    if menu_input == 1:  # Add a new entry
        # Refers to the input fuction to allow user to add details
        print("Please entry your details below:\n")
        input_entries(entries)
        print("\nEntry added to the phonebook.")

    elif menu_input == 2:  # Listing all entries
        # Checks if there are entries in the entries list
        if len(entries) == 0:
            print(
                "There are currently no entries in the phonebook, please add an entry from the main menu")
        else:
            print("Here is a list of all the entries:\n")
            # Sorts the entries alphabetically by the surname key
            entries = sorted(entries, key=lambda k: k['Surname'])
            for entry in entries:
                # Refers to the print fuction to output the entries
                list_entries()
            # Checks how many entries are in the enrty list
            print("\nThere are "+str(len(entries)),
                  "entries in the phonebook"+"\n")

    elif menu_input == 3:  # Search for an entry
        if len(entries) == 0:
            print(
                "There are currently no entries in the phonebook, please add an entry from the main menu")
        else:
            flag = False
            search_surname = input(
                'Enter surname of the person your searching for:\n')
            # If the surname typed in matches the items in the list then they are printed
            for entry in entries:
                if entry['Surname'] == search_surname.title().replace(" ", ""):
                    list_entries()
                    flag = True
            # If the Surname typed doesn't match then the error message is printed and the program retuns to the main menu
            if flag == False:
                print(
                    "That surname does not match the names in the phonebook, please try again:\n")

    elif menu_input == 4:  # Delete an entry
        if len(entries) == 0:
            print(
                "There are currently no entries in the phonebook, please add an entry from the main menu")
        else:
            # Sets variables for deleted entries and entry
            deleted_entries = 0
            entry = 0
            search_surname_del = input(
                'Enter the surname of the entry you wish to delete:\n')
            search_first_name_del = input(
                'Entre the first name of the entry you wish to delete:\n')
            # Checks if there any entries to allow them to be deleted
            while entry < len(entries):
                # If the names searched is in the list if so then said entry is deleted and added to the deleted entries variable
                if entries[entry]['Surname'] == search_surname_del.title().replace(" ", "") and entries[entry]['First Name'] == search_first_name_del.title().replace(" ", ""):
                    del entries[entry]
                    deleted_entries += 1
                # If the name searched is not in the list the entry varible counts up to stop the while loop and prints the error message
                else:
                    entry += 1
            if deleted_entries == 0:
                print(
                    "The names you have searched for do not match the names in the phonebook, please try again:\n")
            # lets the user know how many entries were deleted
            print("You have deleted "+str(deleted_entries), "entries.")

    elif menu_input == 5:  # Add a personal note
        if len(entries) == 0:
            print(
                "There are currently no entries in the phonebook, please add an entry from the main menu")
        else:
            name_flag = False
            print(
                "To add a personal note, type the first and last name of the entry you wish to edit\n")
            search_first_name = input('Enter first name:\n')
            search_surname = input('Enter surname:\n')
            # Checks if the searched names are in the entries list
            for entry in entries:
                if entry['First Name'] == search_first_name.title().replace(" ", "") and entry['Surname'] == search_surname.title().replace(" ", ""):
                    # If the searched names are in the list a typed personal note is added to the 'Personal Notes' item in the list
                    personal_note = input('Enter personal note:\n')
                    entry['Personal Notes'].append(personal_note)
                    print("Personal note has been added\n")
                    name_flag = True
            # If names searched isn't in the list then an error code is printed and the program goes back to the main menu
            if name_flag == False:
                print(
                    "The names you have searched for do not match the names in the phonebook, please try again:\n")

    elif menu_input == 6:  # Remove a personal note
        if len(entries) == 0:
            print(
                "There are currently no entries in the phonebook, please add an entry from the main menu")
        else:
            remove_notes_flag = False
            print(
                "To remove a personal note, type the first and last name of the entry you wish to edit\n")
            search_first_name = input('Enter first name:\n')
            search_surname = input('Enter surname:\n')
            # Again checks if the names searched are in the list
            for entry in entries:
                if entry['First Name'] == search_first_name.title() and entry['Surname'] == search_surname.title():
                    print("Personal Notes: ")
                    # Prints the notes in a numeric list
                    line = 0
                    for notes in entry['Personal Notes']:
                        line += 1
                        print(str(line) + "." + str(notes))
                    # Allows the user to input the note that is to be deleted and adjust the users input to the correct index in the list
                    note_sel = True
                    while note_sel:
                        remove_notes = int(
                            input("Select the personal note you wish to delete:\n"))
                        remove_notes -= 1
                        # Check that the input is in the correct range of the notes list
                        if int(remove_notes) > int(line):
                            print("Incorrect input, please try again")
                            continue
                        else:
                            note_sel = False
                            del (entry['Personal Notes'][remove_notes])
                            remove_notes_flag = True
                            print("The selected personal note has been deleted")
            if remove_notes_flag == False:
                print(
                    "The names you have searched for do not match the names in the phonebook, please try again:\n")

    elif menu_input == 7:  # Quit the program
        exit_program = True

    else:
        print("Error: You entered an invalid choice. Please try again.")

print("Thank you for using the EG-244 Telephone Book")
