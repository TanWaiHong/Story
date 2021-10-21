from twilio.rest import Client

TWILIO_SID = "AC184c635820228eb7b63cf52a0a3848b0"
TWILIO_AUTH_TOKEN = "4389a7c0db4cb9d09a1913e5d2ce4fc6"
TWILIO_VIRTUAL_NUMBER = '+12162424248'
TWILIO_VERIFIED_NUMBER = '+60192259076'


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

