
#import Car
import requests
import json
import threading
from Car import Car
from time import sleep
from tabulate import tabulate
from prettytable import PrettyTable

vehicle_list = []

def main():
    print("\t*************************************************")
    print("\t**** Welcome to the WeGo Vehicle Simulator!  ****")
    print("\t*************************************************")
    print("\t*** Any time you want you quit just press 'Q' ***")
    print("\t*************************************************")
    print("\t********* Retrieving your vehicles .... *********")

    vehicle_list = retrieveVehicles()
    printCurrentState(vehicle_list)
    updatingVehicles = True
    #threading.Thread(target=heartbeat_manager).start()

def printCurrentState(vehicle_list):
    simulatorOptions = PrettyTable()
    simulatorOptions.field_names = ["Simulator Options", "Description", "Command"]
    carTable = PrettyTable()
    carTable.field_names = ["Vehicle ID", "Status", "Fleet ID", "Make", "Licence Plate", "Current Longitude", "Current Latitude", "Last Heartbeat"]

    simulatorOptions.add_row(["Change Car Status", "Change status of a single vehicle", "C <vehicle id>"])
    simulatorOptions.add_row(["Get Eta", "Get ETA of a single vehicle", "E <vehicle id>"])
    simulatorOptions.add_row(["Start Route", "Get route of a single vehicle", "R"])
    simulatorOptions.add_row(["Kill Heartbeat", "Kill the heartbeat of a vehicle, fleet, or all vehicles", "K <vehicle id>"])
    simulatorOptions.add_row(["Start Heartbeat", "Start the heartbeat of a vehicle, fleet, or all vehicles", "S"])

    # keep asking user for input
    # if they do anything but start route, do backend data changes
    # if they do start route:
    #   create new thread for that car with function executeCarRoute
    for car in vehicle_list:
        carTable.add_row([car.vehicle_id,car.vehicle_status,car.fleet_id,car.vehicle_make,car.license_plate,car.current_long,car.current_lat,car.last_hb] )
    print(carTable)
    print("\n")
    print(simulatorOptions)
#returns a list of vehicles of type Car
#Want to make a thread for each of these? Don't know if I should do this inside this function or somewhere else
#Wherever I end up making the vehicle threads, have those threads send updates to the db updating it's car Information
#However this is done Here's what needs to get done:
    #for every vehicle, a request should be sent to the BE to update the info of that vehicle in the DB
    #how that gets done with threading i'm not sure yet
def retrieveVehicles():
    request_vehicles = requests.get("https://supply.team22.softwareengineeringii.com/vehicleRequest")
    v_list = []
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
            v_list.append(simulated_vehicle)
        return v_list
    else:
        print("ERROR :: ", request_vehicles.status_code)
        print("We were not able to retrieve your vehicles, restarting application ... ")
        python = sys.executable
        os.execl(python, python, * sys.argv)

# def heartbeat():
#     for car in vehicle_list if car.heartbeat:
#         # send heartbeat to backend for that carLoop
#         pass
#         print("car ", car.id, " heartbeat")
#         #if no hb continue
#     sleep(10)

#Was trying to flesh out an idea about executing a route, this ideally will be used later?
def executeCarRoute(car):
    route_request = "https://supply.team22.softwareengineeringii.com/getRoute{vid}"
    route = None #assume we did some json things to get route
    for coords in route:
        #change the current_lat and current_long of that car every 3 seconds
        #use sleep(3)
        pass



"""
GET /changeStatus/{id}
    changes status
car = GET /vehicle/{id}
    gets new status
vehicle{id} = car

"""

# If button is pressed, make request for the id of that vehicle ?
# How does this work with threading?? So if I click a button for an option, does it call that function with that car? In that thread?


if __name__ == '__main__':
     main()
