# MAPPING SERVICES #



### What is this repository for? ###

* Summary:
* This repository serves as a reference for any mapping/routing features needed for WeGo's supply/demand
* The mapping API's are provided by Mapbox



### Route and Eta Retrieval ###

* Python API collection using Mapbox API requests  
* Uses the Directions API for both functions
* getRoute() function retrieves a route based on a start and end point
* getEta() function retrives an a distance and derives an ETA
* For further documentation look to vehicle_utils_doc.md 


### Vehicle Rendering ###

* Starter code to render vehicles using WeGo's vehicle retrieval API 
* Can be used for Deman FE and Supply FE
* Renders the vehicles from the vehicle database onto a mapbox map
* Purpose for WeGo: For fleet managers to see their 
* filename: render_vehicle_to_map.html


### Address Utils ###

* Provides a starter to enter a human readable address and have a mapbox map go to that location 
* Also provides ways in which to retrieve address data from the geocoder
* file name : address_mapping_utils.html


### Contribution guidelines ###

* All maps and map data are provided by mapbox
* © Mapbox © OpenStreetMap 
* https://www.mapbox.com/about/maps/ , http://www.openstreetmap.org/about/, https://www.mapbox.com/map-feedback/#/-74.5/40/10



