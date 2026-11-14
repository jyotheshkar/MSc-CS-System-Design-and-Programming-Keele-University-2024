from carpark import carParkingSystem

def mainMenu():
    parking_system = carParkingSystem()
    while True:
        print("\nWelcome to the Car Parking System\n")
        print("1. Enter the car park {Hourly rate £2}")
        print("2. Exit the car park")
        print("3. View available parking spaces")
        print("4. Query parking record by ticket number")
        print("5. Quit")

        selection = input("Please enter your choice: ")

        if selection == '1':
            parking_system.enterCarPark()
        elif selection == '2':
            parking_system.exitCarPark()
        elif selection == '3':
            parking_system.availableParkingSpaces()
        elif selection == '4':
            parking_system.queryParkingRecords()
        elif selection == '5':
            print("You have exited the car parking system. See you next time!")
            break
        else:
            print("Invalid choice. Kindly select a valid option.")

if __name__ == "__main__":
    mainMenu()
