
#import Car
import requests
import json
import sys
import os
import threading
from Car import Car
import time
from tabulate import tabulate
from prettytable import PrettyTable

print("\t**********************************************")
print("\t*** Welcome to the WeGo Vehicle Simulator! ***")
print("\t**********************************************")
print("\t*** Any time you want you quit just press 'Q' ***")
print("\t**********************************************")

print("\t*** Retrieving your vehicles .... ***")

# Global variables
vehicle_dict = {}
READ_TIME_INTERVAL = 4
WRITE_TIME_INTERVAL = 8
STATUS_OFFSET = 0
heartbeat_set = set([])

def main(): 
    global vehicle_dict
    global heartbeat_set
    
    # Set up the python tables in the console
    carTable = PrettyTable()
    vsim_menu = PrettyTable()
    setPrettyTables(carTable, vsim_menu)

    # Store all vehicles from db inside vehicle_dict where key = vid (primary) and value = [data attribuites related to vid]
    getAllVehicles()
    printVehicleTable(carTable)
    printMenu(vsim_menu)

    # The heartbeat set will be used to track which vehicles should (or shouldn't) be reporting threads inside our daemon thread..
    createHeartbeatSet()
    print(heartbeat_set)
    # reportHeartbeat() daemon will model using an https:// request to push a heartbeat to the server. 
    t1 = threading.Thread(target=reportHeartbeat, daemon=True)
    t1.start()
    
    # Get user input
    again = "y"
    while again == "y":
        x = input("Enter your option here: ")
        vehid = int(input("Enter the vehicle id number you want to stop reporting: "))
        # Kill a vehicle heartbeat
        if x == 'K' or x == 'k':
            if vehid in heartbeat_set:
                heartbeat_set.remove(vehid)
            else:
                print("Vehicle id not found")

        # Start a vehicle heartbeat
        elif x == 'S' or x == 's':
            if vehid in heartbeat_set:
                heartbeat_set.add(vehid)
            else:
                print("Vehicle id not found")
        
        # Change the vehicle status. Remember to use enumerated types here when you add code to check which status the tester wants to change to
        elif x == 'C' or x == 'c':
            if vehid in vehicle_dict:
                changeVehicleStatus(vehid)
        else:
            print("Invalid option")
        again = input("Press y if you want to continue: ")


# Fake a heartbeat report by using a file write.
def reportHeartbeat():
    while True:
        global heartbeat_set
        with open("test.txt", "a") as f:
            # If the vehicle isn't in our heartbeat_set, then it has gone 'silent'. So we won't report this vehicle.
            for vehicle in heartbeat_set:
                f.write(str(vehicle))
                f.write('\n')
            f.close()
        time.sleep(WRITE_TIME_INTERVAL)

# # Read from the database to make sure our vehicle_dict values are always up to date
# def refreshVehicleListData():
#     while True:
#         global vehicle_dict
#         getAllVehicles()
#         time.sleep(READ_TIME_INTERVAL)

# Fake change a vehicle's status by writing it to a file. Note that we'll need tp use enumerated types here
def changeVehicleStatus(vehicleId):
    global vehicle_dict
    #valueArray = vehicle_dict[vehicleId]
    with open("vstatus.txt", "a") as f:
        w = str(vehicleId) + " status has been changed to: inactive"
        f.write(w)
        f.write("\n")
        f.close()

def executeRoute(vid):
    # We could utilize a python event to model a vehicle running along a route returned by Mapbox
    # and update the BE of our new coordinates for a given time interval
    # Use a lock around the event to prevent any shared resource conflicts from occuring
    # 
    # t2 = threading.Thread(target=runRoute)
    # def runRoute(vehicle):
    #   lock = threading.Lock()
    #   lock.acquire()
    #   for coords in route:
    #       do something
    #   lock.release()
    pass

def setPrettyTables(carTable, vsim_menu):
    carTable.field_names = ["Vehicle ID", "Status", "Fleet ID", "Make", "Licence Plate", "Current Longitude", "Current Latitude", "Last Heartbeat"]
    vsim_menu.field_names = ["Simulator Options", "Description", "Command"]


def createHeartbeatSet():
    global vehicle_dict
    global heartbeat_set
    for vehicle in vehicle_dict:
        heartbeat_set.add(vehicle)


def getAllVehicles():
    global vehicle_dict
    request_vehicles = requests.get("https://supply.team22.softwareengineeringii.com/vehicleRequest")
    if request_vehicles:
        vehicles = request_vehicles.json()
        vehicles.pop(0)
        for v in vehicles:
            vehicleAttrList = []
            v_id = v.get("vehicleid")
            vehicleAttrList.append(v.get("status"))
            vehicleAttrList.append(v.get("fleetid"))
            vehicleAttrList.append(v.get("make"))
            vehicleAttrList.append(v.get("licenseplate"))
            vehicleAttrList.append(v.get("current_lon"))
            vehicleAttrList.append(v.get("current_lat"))
            vehicleAttrList.append(v.get("last_hb"))
            vehicle_dict.update({v_id : vehicleAttrList})
        time.sleep(1)
        print("\nVehicles retrieved!")
    else:
        print("ERROR :: ", request_vehicles.status_code)
        print("We were not able to retrieve your vehicles, restarting application ... ")
        python = sys.executable
        os.execl(python, python, * sys.argv)
    print(vehicle_dict)

def printVehicleTable(carTable):
    global vehicle_dict
    for car in vehicle_dict:
        attrList = vehicle_dict[car]
        carTable.add_row([car, attrList[0], attrList[1], attrList[2], attrList[3], attrList[4], attrList[5], attrList[6]])
    print(carTable)
    print('\n')

def printMenu(menuTable):
    menuTable.add_row(["Change Car Status", "Change status of a single vehicle", "C <vehicle id>"])
    menuTable.add_row(["Get Eta", "Get ETA of a single vehicle", "E <vehicle id>"])
    menuTable.add_row(["Get Route", "Get route of a single vehicle", "R"])
    menuTable.add_row(["Kill Heartbeat", "Kill the heartbeat of a vehicle, fleet, or all vehicles", "K <vehicle id, fleet id, NONE>"])
    menuTable.add_row(["Start Heartbeat", "Start the heartbeat of a vehicle, fleet, or all vehicles", "S"])

    print("\n")
    print(menuTable)

if __name__ == '__main__':
    main()



