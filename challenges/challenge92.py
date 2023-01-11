#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lon= resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    ts = resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    locator_resp = rg.search((lat,lon))
    city = locator_resp[0]["name"]
    cc = locator_resp[0]["cc"]

    print(f"""Current Location Of The ISS: 
    Timestamp: {ts}
    Lon: {lon}
    Lat: {lat}
    Currently over: {city},{cc}
    """)

if __name__ == "__main__":
    main()

