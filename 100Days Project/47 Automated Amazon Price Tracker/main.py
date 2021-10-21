import smtplib
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B0863JB424/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B0863JB424&pd_rd_w=xtS95&pf_rd_p=9fd3ea7c-b77c-42ac-b43b-c872d3f37c38&pd_rd_wg=DVjZf&pf_rd_r=N1GF66K4FPBQS8BBAESJ&pd_rd_r=c1b6922e-f949-4503-9736-411bc33b11df&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVE4zVUVHVlZMODBPJmVuY3J5cHRlZElkPUEwOTU4NzQ3MkFHUllPTlBFVEkxSiZlbmNyeXB0ZWRBZElkPUExMDQ4NTYyTDRaN09CMVJURElDJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

response = requests.get(url=URL, headers=header)

website_html = response.content

soup = BeautifulSoup(website_html, "lxml")

price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = float(price.split("$")[1])


if price_without_currency < 200:
    title = soup.find(id="productTitle").get_text().strip()

    MY_EMAIL = "sfasfwefw@gmail.com"
    PASSWORD = "$8PX8X+#RHKKf"
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="tan040724101445@gmail.com",
            msg=message
        )
