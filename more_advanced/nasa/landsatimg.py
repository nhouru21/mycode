#!/usr/bin/python3
import requests
from geopy.geocoders import Nominatim

## Define NEOW URL
NEOURL = "https://api.nasa.gov/planetary/earth/assets?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2022-12-06"
    date = "date=2018-01-01"

    address = input("Please enter a city: ")
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(address)
    
    ## get lat and lon, round to two decimals and convert to string
    lat = str(round((location.latitude), 2))
    lon = str(round((location.longitude), 2))
    print((location.latitude, location.longitude))

    # make a request with the request library
    latimgrequest = requests.get(NEOURL + "lon=" + lon + "&lat=" + lat + "&" + date + "&&" + "dim=0.10" + "&" + nasacreds)

    ## display NASAs Landsat imagery
    latimgrequest = latimgrequest.json()
    print(latimgrequest)

if __name__ == "__main__":
    main()

