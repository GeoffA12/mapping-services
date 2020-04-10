class Car:
    def __init__ (self, vehicle_id, vehicle_status, fleet_id, vehicle_make, licence_plate, current_lat, current_long, last_hb):
        #Type : int
        self.vehicle_id = vehicle_id
        #Type: String
        self.vehicle_status = vehicle_status
        #Type : int
        self.fleet_id = fleet_id
        #Type : Vehicle Type
        self.vehicle_make = vehicle_make
        #Type : Boolean
        self.license_plate = licence_plate
        #Type : Float
        self.current_lat = current_lat
        # Type : Array
        self.current_long = current_long
        # Type : Boolean
        self.last_hb = None
        # Type : Boolean
        self.heartbeat = False



    def toString():
        print("Vehicle Information :: ", "\n")
        print("Vehicle ID :: ", self.vehicle_id, "\n")
        print("Vehicle Status :: ", self.vehicle_status, "\n")
        print("Fleet ID :: ", self.fleet_id, "\n")
        print("Vehicle Make :: ", self.vehicle_make, "\n")
        print("Licence Plate # :: ", self.license_plate, "\n")
        print("Current Lat :: ", self.current_lat, "\n")
        print("Current Lon :: ", self.current_long, "\n")
        print("Last Heartbeat :: ", self.last_hb, "\n")






## TODO: print vehicles by fleet,
