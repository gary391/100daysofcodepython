import requests
from datetime import datetime
from pprint import pprint
MY_LAT = 47.380852
MY_LONG = -122.237419
#
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
#
# # Using the build in exception in the request module.
# response.raise_for_status()
#
# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

url = "https://api.sunrise-sunset.org/json"

# we need to provide the location

parameter = {"lat": MY_LAT, "lng": MY_LONG,  "formatted": 0}

response = requests.get(url, params=parameter)
response.raise_for_status()
data = response.json()
# pprint(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_time = (sunrise.split("T")[1])
# print(sunrise_time)
sunrise_time_hour = sunrise_time.split(":")[0]
print(sunrise_time_hour)
sunset_time = (sunset.split("T")[1])
# print(sunset_time)
sunset_time_hour = sunset_time.split(":")[0]
print(sunset_time_hour)

time_now = datetime.now()
print(time_now.hour)
