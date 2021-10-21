import datetime as dt
import smtplib
from random import choice

MY_EMAIL = "sfasfwefw@gmail.com"
PASSWORD = "$8PX8X+#RHKKf"

now_day = dt.datetime.now().weekday()
if now_day == 5:
    with open("quotes.txt") as quotes:
        quotes_list = [quote.strip() for quote in quotes.readlines()]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="tan040724101445@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{choice(quotes_list)}"
        )
