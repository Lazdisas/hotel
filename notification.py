# coding: utf8
# import sys
# print sys.getdefaultencoding()
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')
from twilio.rest import Client
class Notification:
    def __init__(self,message, number):
        self.message = message
        self.number = number

    def send_text_message(self):
        print("---send sms---")
        account_sid = "AC1b77cc0b7b2e665781f94cef4d812a8"
        auth_token = "3f13cf63cd93c88063c629b620433b0"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = "Sami",
            to = "+213557098309",
            from_ = "+17163303168"
            )
        print(message.sid)
        print(self.message)
        print(self.number)
        print("SMS SENDED OK")
        print("---end send sms---")
        return True
