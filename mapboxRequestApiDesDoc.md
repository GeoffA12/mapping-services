# Mapping Services REST Request API

## HTTP Method Familiarity
| Method    | URI          | Has Request Body?
|:---       |:---          |:---
|GET       |/vehicle_utils |No


## Resources
| Parameter | Semantics  |
|:---       |:---        |
|start_address | Starting Point Address    |
|end_address   | Ending Point Address  |

### By Order ID
**API Call:**\
http://team22.supply.softwareengineeringii.com/api/backend/0.0/vehicle_utils?start_address={yourstartadd}&end_address={yourendadd}\
**Example API Call:**\
http://team22.supply.softwareengineeringii.com/api/backend/0.0/vehicles?oid=East+45th+Street&West+21st+Street


## API Description
API is meant to be able to make API calls to the Mapbox driving mapping services to retrieve a route and derive an eta.

**getRoute():**\
Uses the following API request:
'https://api.mapbox.com/directions/v5/mapbox/driving/{lat;long;-lat:long}?geometries=geojson&access_token={access_token}'
Retrieves general information about a driving route as a JSON body, then only the waypoints across the route are taken and returned as a JSON object.

**getETA():**\
Uses the following API request:
'https://api.mapbox.com/directions/v5/mapbox/driving/{lat;long;-lat:long}?geometries=geojson&access_token={access_token}'
Retrieves general information about a driving route as a JSON body, then the distance (in meters) from that JSON body is taken and converted into miles, after which that distance is divided by a fixed mph to derive the eta.
