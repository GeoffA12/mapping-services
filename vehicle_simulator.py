
#import Car
import requests
import json
from Car import Car
from time import sleep
from tabulate import tabulate
from prettytable import PrettyTable


print("\t**********************************************")
print("\t*** Welcome to the WeGo Vehicle Simulator! ***")
print("\t**********************************************")
sleep(1)
print("\t*** Any time you want you quit just press 'Q' ***")
print("\t**********************************************")

print("\t*** Retrieving your vehicles .... ***")

carTable = PrettyTable()
simulatorOptions = PrettyTable()

carTable.field_names = ["Vehicle ID", "Status", "Fleet ID", "Make", "Licence Plate", "Current Longitude", "Current Latitude", "Last Heartbeat"]
simulatorOptions.field_names = ["Simulator Options", "Description", "Command"]

while(True):
    request_vehicles = requests.get("https://supply.team22.softwareengineeringii.com/vehicleRequest")
    vehicle_list = []
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
            vehicle_list.append(simulated_vehicle)
        sleep(1)
        print("\nVehicles retrieved!")
        sleep(200)

    else:
        print("ERROR :: ", request_vehicles.status_code)
        print("We were not able to retrieve your vehicles, restarting application ... ")
        python = sys.executable
        os.execl(python, python, * sys.argv)



simulatorOptions.add_row(["Change Car Status", "Change status of a single vehicle", "C <vehicle id>"])
simulatorOptions.add_row(["Get Eta", "Get ETA of a single vehicle", "E <vehicle id>"])
simulatorOptions.add_row(["Get Route", "Get route of a single vehicle", "R"])
simulatorOptions.add_row(["Kill Heartbeat", "Kill the heartbeat of a vehicle, fleet, or all vehicles", "K <vehicle id, fleet id, NONE>"])
simulatorOptions.add_row(["Start Heartbeat", "Start the heartbeat of a vehicle, fleet, or all vehicles", "S"])

for car in vehicle_list:
    carTable.add_row([car.vehicle_id,car.vehicle_status,car.fleet_id,car.vehicle_make,car.license_plate,car.current_long,car.current_lat,car.last_hb] )
print(carTable)
print("\n")
print(simulatorOptions)

# prompt user for command
#   response: <command letter>
# go to that function
# prompt user for target
#   response: <vehicle_id>, <fleet_id>, all
# call jeffy man's backend with the function

"""
GET /changeStatus/{id}
    changes status
car = GET /vehicle/{id}
    gets new status
vehicle{id} = car

"""

# If button is pressed, make request for the id of that vehicle ?
# How does this work with threading?? So if I click a button for an option, does it call that function with that car? In that thread?
