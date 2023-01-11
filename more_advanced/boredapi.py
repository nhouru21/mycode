#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests

URL= "http://www.boredapi.com/api/activity/"
def main():
    resp= requests.get(URL).json()
    activity = resp["activity"]
    activity_type = resp["type"]
    participants = resp["participants"]
    price = resp["price"]

    print(f"Are you bored and looking for an activity? Have you considered \'{activity}\'.\nIt is an {activity_type} type of activity for {participants} people and has a price rating of {price}.")

if __name__ == "__main__":
    main()

