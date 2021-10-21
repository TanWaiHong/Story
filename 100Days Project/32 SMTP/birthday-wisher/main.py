import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "sfasfwefw@gmail.com"
PASSWORD = "$8PX8X+#RHKKf"
PlACEHOLDER = "[NAME]"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

today_day = dt.datetime.today().date().day
today_month = dt.datetime.today().date().month

for the_data in data_dict:
    if the_data["month"] == today_month and the_data["day"] == today_day:
        try:
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_templates:
                letter = letter_templates.read()
            name = the_data["name"]
            email = the_data["email"]
            letter = letter.replace(PlACEHOLDER, name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Happy birthday\n\n{letter}"
                )
        finally:
            pass
