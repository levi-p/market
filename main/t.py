from twilio.rest import TwilioRestClient

class sendMessage():
    def __init__(self,phone,msg):
        self.phone = str(phone).replace('0','+265',1)
        self.msg = msg
    def go(self):
        account = "AC30b188ff517402a929786e3441ecbdd4"
        token = "76c28d21d6931f8376c4ac312e6c0b39"
        client = TwilioRestClient(account, token)

        message = client.sms.messages.create(to=self.phone,
                                     from_="+12018903924",
                                     body=self.msg)


d=sendMessage(+265881460566,"hih")

