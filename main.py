#Initial dictionary


vehicle = {
    "name" : "nameplace",
    "type" : "typeplace",
    "battery" : 100,
    "status" : "statusplace",
    "mission" : "missionplace"
}

vehicle["name"] = input("name?")

#Request and validate type input
ValidTypes = ["Rover", "Drone", "Submarine"]
while True: #Loop until a valid type is entered
    vehicle["type"] = input("type?")
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

print("Name: ", vehicle["name"])
print("Type: ", vehicle["type"])
print("Battery: ", vehicle["battery"],"%")
print("Status: ",vehicle["status"])
print("Mission: ", vehicle["mission"])

print(type(vehicle["battery"]))