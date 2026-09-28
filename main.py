#Initial dictionary


fleet = []

def register_vehicle():

    vehicle = {
        "name" : "nameplace",
        "type" : "typeplace",
        "battery" : 100,
        "status" : "statusplace",
        "mission" : "missionplace"
    }

    while True:
        vehicle["name"] = input("name?")
        for v in fleet:
            if v["name"].lower() == vehicle["name"].lower():
                print("A vehicle with this name already exists.")
                break
        else:
            break

    #Request and validate type input
    ValidTypes = ["Rover", "Drone", "Submarine"]
    while True: #Loop until a valid type is entered
        vehicle["type"] = input("type?").title()
        if vehicle["type"] not in ValidTypes:
            print("Invalid type. Please enter Rover, Drone, or Submarine.")
            continue
        break



    #Request and validate battery input
    while True: #Loop until input is a valid number
        try:
            vehicle["battery"] = int(input("battery?"))
            if vehicle["battery"] < 0 or vehicle["battery"] > 100: #Keep input within valid range
                print("Battery must be between 0 and 100.")
                continue
            break
        except ValueError: #Handle non-integer input
            print("That isn't a valid number.")


    vehicle["status"] = "Available"
    vehicle["mission"] = "None"

    fleet.append(vehicle)


def view_vehicles():
    if len(fleet) > 0:
        for vehicle in fleet:
            print("vehicle name: ", vehicle["name"]) 
            print("vehicle type: ", vehicle["type"]) 
            print("vehicle battery: ", vehicle["battery"])
            print("vehicle status: ", vehicle["status"])
            print("vehicle mission: ", vehicle["mission"])
            print()  # Add a blank line between vehicles
    else:
        print("No vehicles registered.")

while True:
    print("1. Register Vehicle")
    print("2. View Vehicles")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        register_vehicle()
    elif choice == "2":
        view_vehicles()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")


