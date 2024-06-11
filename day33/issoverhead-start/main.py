import requests
from datetime import datetime
import smtplib

my_email = "codewithgary@gmail.com"
password = "#############"

MY_LAT = 47.380852  # Your latitude
MY_LONG = -122.237419  # Your longitude
#TODO create a function that return a boolean value if the ISS is within 5 degree of our current location.

def is_issoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    """
    Returns true or false depending on whether or not the issoverhead and within
    5 degrees.
    """
    if iss_latitude >= (MY_LAT + 5) or iss_latitude <= (MY_LAT - 5) and iss_longitude >= (MY_LONG + 5) or iss_longitude <= (MY_LONG - 5):
        return True
    else:
        return False

def is_iss_visble():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



def email_to_lookup_iss():
    # Using context manager we can avoid explicitly closing the connection.

    msg = f"Subject: Look up to see ISS in the sky! \n\n"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Create a tls connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="codewithgary@gmail.com",
                            msg=msg)

if is_issoverhead() and  is_iss_visble():
    email_to_lookup_iss()
