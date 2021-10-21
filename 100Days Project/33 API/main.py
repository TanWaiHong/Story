import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "sfasfwefw@gmail.com"
PASSWORD = "$8PX8X+#RHKKf"

MY_LAT = 3.047268
MY_LONG = 101.498566


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude - MY_LONG < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now > sunset or time_now < sunrise:
        return True


while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_EMAIL)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="tan040724101445@gmail.com",
            msg="Subject:Look Up \n\nThe ISS is above you in the sky."
        )
    time.sleep(60)
