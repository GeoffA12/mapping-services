class simulatedVehicle:
    def __init__(self, vehicle, threadid):
        self.vehicle = vehicle
        self.threadid = threadid

    def driver(self):
        print(f'\n{self.vehicle}')
        if self.vehicle.status is not 'maintenance':
            if self.vehicle.route:
                nextCoor = self.vehicle.route.pop(0)
                self.vehicle.curPos = (nextCoor[0], nextCoor[1])
            if self.vehicle.heartbeatSwitch:
                self.heartbeat()

    def heartbeat(self):
        # print('I just sent a heartbeat')
        #change a bit to adapt to hh/mm/ss.ms
        now = datetime.now().isoformat()
        postBody = {
            'vid': self.vehicle.vid,
            'current_lat': self.vehicle.curPos[0],
            'current_lon': self.vehicle.curPos[1],
            'status': self.vehicle.status,
            'last_heartbeat': now[now.index('T') + 1:]
            }
        # print(postBody)
        postBody = json.dumps(postBody)
        # print(postBody)
        response = requests.post('https://supply.team22.softwareengineeringii.com/updateVehicle', postBody)
        # print(response.status_code)
        # print(response.json())
        if response.json():
            self.vehicle.route = response.json()['route']
