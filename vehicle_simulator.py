
#import Car
import requests
import json
import threading
from Car import Car
from simulatedVehicle from simulatedVehicle
from time import sleep
from tabulate import tabulate
from prettytable import PrettyTable
import sys

vehicle_list = []

class Controller:
    def __init__(self):
        self.vehicleArr = []
        self.models = []

    def startThreads(self):
        while True:
            if len(self.vehicleArr) != 0:
                for index, vehicle in enumerate(self.vehicleArr, 1):
                    self.models.append(VehicleModel(vehicle, index))
            for model in self.models:
                thread = threading.Thread(target=model.driver, name=f"model-{model.threadid}")
                thread.start()
            time.sleep(5)
            self.models = []



def main():
    print("\t*************************************************")
    print("\t**** Welcome to the WeGo Vehicle Simulator!  ****")
    print("\t*************************************************")
    print("\t*** Any time you want you quit just press 'Q' ***")
    print("\t*************************************************")
    print("\t********* Retrieving your vehicles .... *********")

    vehicle_db_dictionary = retrieveVehicles()
    printCurrentState(vehicle_db_dictionary)
    updatingVehicles = True
    #threading.Thread(target=heartbeat_manager).start()

def printCurrentState(vehicle_dict):
    simulatorOptions = PrettyTable()
    simulatorOptions.field_names = ["Simulator Options", "Description", "Command"]
    carTable = PrettyTable()
    carTable.field_names = ["Vehicle ID", "Status", "Fleet ID", "Make", "Licence Plate", "Current Longitude", "Current Latitude", "Last Heartbeat"]
    simulatorOptions.add_row(["Kill Heartbeat", "Kill the heartbeat of a vehicle", "K"])
    simulatorOptions.add_row(["Start Heartbeat", "Start the heartbeat of a vehicle, fleet, or all vehicles", "S"])

    # keep asking user for input
    # if they do anything but start route, do backend data changes
    # if they do start route:
    #   create new thread for that car with function executeCarRoute
    for car in vehicle_db_dict.values():
        carTable.add_row([car.vehicle_id,car.vehicle_status,car.fleet_id,car.vehicle_make,car.license_plate,car.current_long,car.current_lat,car.last_hb] )
    print(carTable)
    print("\n")
    print(simulatorOptions)

def view(inputVar):
    while True:
        print('Input the vehicle id you want to spin up!')
        userInput = input("> ")
        if userInput.lower() == 'all':
            inputVar.extend([vehicle for vehicle in vehicleDict.values()])
        #put something for turnoff heartbeat
        else:
            try:
                vehicle = vehicleDict[int(userInput)]
                inputVar.append(vehicle)
            except KeyError as ke:
                print(ke)
                print('Key doesn\'t exist in dictionary!')
#returns a list of vehicles of type Car
#Want to make a thread for each of these? Don't know if I should do this inside this function or somewhere else
#Wherever I end up making the vehicle threads, have those threads send updates to the db updating it's car Information
#However this is done Here's what needs to get done:
    #for every vehicle, a request should be sent to the BE to update the info of that vehicle in the DB
    #how that gets done with threading i'm not sure yet
def retrieveVehicles():
    request_vehicles = requests.get("https://supply.team22.softwareengineeringii.com/vehicleRequest")
    #v_list = []
    v_dict = {}
    if request_vehicles:
        vehicles = request_vehicles.json()
        vehicles.pop(0)
        for v in vehicles:
            v_id = v.get("vehicleid")
            v_stat = v.get("status")
            f_id  = v.get("fleetid")
            v_make = v.get("make")
            l_plate = v.get("licenseplate")
            c_long = v.get("current_lon")
            c_lat = v.get("current_lat")
            last_hb = v.get("last_hb")
            simulated_vehicle = Car(v_id, v_stat, f_id, v_make, l_plate, c_long, c_lat, last_hb)
            v_dict.update({v_id : simulated_vehicle})
        #return v_list
        #for a car to be on it's not in maintenance
        return v_dict
        # for i,j in hb_dict.items():
        #     print("Key :: " + i)
        #     print("\nValue :: " + j)
    else:
        print("ERROR :: ", request_vehicles.status_code)
        print("We were not able to retrieve your vehicles, restarting application ... ")
        sys.exit


#group vehicles by fleet id
#an option to select a fleet and send heartbeats for a fleet
#heartbeat goes in model??
#Always updating position
#For interface: keep track of vehicles being simulated

    #sendHB's??????3
    #getback a status?????
    #logic for checking its status for a routes
    #


#Was trying to flesh out an idea about executing a route, this ideally will be used later?


# If button is pressed, make request for the id of that vehicle ?
# How does this work with threading?? So if I click a button for an option, does it call that function with that car? In that thread?


if __name__ == '__main__':
    main()
    controller = Controller()
    thread1 = threading.Thread(target=controller.startThreads, name="controller")
    thread2 = threading.Thread(target=view, args=(controller.vehicleArr,), name="UI")
    thread2.start()
    thread1.start()
