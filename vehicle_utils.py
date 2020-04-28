
import requests
import json




#route request API
def getRoute(begin_long,begin_lat,end_long, end_lat ):
        #Make request for mapbox driving data given two coordinates
        mapbox_driving_req = requests.get('https://api.mapbox.com/directions/v5/mapbox/driving/'+str(begin_long)+','+str(begin_lat)+';'+str(end_long)+','+str(end_lat)+'?geometries=geojson&access_token=pk.eyJ1IjoiY3N5Y2hldiIsImEiOiJjazZsbmg4c2gwYXU3M21zOG55aTljcTBuIn0.G5UXjF-3_0mXKo6huFgLwg')
        #encode data
        data = mapbox_driving_req.json()
        #json dump coordinates data
        coords = json.dumps(data.get("routes")[0].get("geometry").get("coordinates"))
        return coords

def getHumanReadable(begin_long,begin_lat):
        #Make request for mapbox driving data given a set of coordinates
        mapbox_driving_req = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/'+str(begin_long)+','+str(begin_lat)+'.json?access_token=pk.eyJ1IjoiY3N5Y2hldiIsImEiOiJjazZsbmg4c2gwYXU3M21zOG55aTljcTBuIn0.G5UXjF-3_0mXKo6huFgLwg&place_name')
        #encode data
        data = mapbox_driving_req.json()
        #json dump place name data
        address = json.dumps(data.get("features")[0].get('place_name'))
        return address


#eta request API
def getEta(begin_long,begin_lat,end_long, end_lat ):
        #Make request for mapbox driving data given two coordinates
        mapbox_driving_req = requests.get('https://api.mapbox.com/directions/v5/mapbox/driving/'+str(begin_long)+','+str(begin_lat)+';'+str(end_long)+','+str(end_lat)+'?geometries=geojson&access_token=pk.eyJ1IjoiY3N5Y2hldiIsImEiOiJjazZsbmg4c2gwYXU3M21zOG55aTljcTBuIn0.G5UXjF-3_0mXKo6huFgLwg')
        #encode data
        data = mapbox_driving_req.json()
        #json dump distance traveled along route data and cast it as a float
        #distance is given in meters
        distance = float(json.dumps(data.get("routes")[0].get("distance")))
        #calculate mock eta from distance data with mock mph
        eta = ((distance/1609.34)/30)*60
        #print("ETA IS:", "%.2f" % eta, "MINUTES")
        return "ETA IS:", "%.2f" % eta, "MINUTES"
if __name__ == '__main__':
    print(getHumanReadable(-73.989,40.733))
