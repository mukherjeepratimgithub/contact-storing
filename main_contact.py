import phonebook

def main():
    choice = ''
    while choice != '4':

        phonebook.printMenu()
        choice = input("Enter you choice [0-4]: ")

        if choice == '0':
            phonebook.retrieveEntry()
        elif choice == '1':
            phonebook.addEntry()
        elif choice == '2':
            phonebook.retrieveAll()
        elif choice == '3':
            phonebook.deleteEntry()
        elif choice == '4':
            print("\nThank You for using our services \nBest Regards")
        else:
            print("\n Invalid selection. Select from options [0-4] \n")

    print("\nExiting.")

    phonebook.c.close()


if __name__ == '__main__':
    main()