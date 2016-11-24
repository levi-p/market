from twilio.rest import TwilioRestClient
from register.models import userprofile as use





class sendMessage():
    

    def __init__(self,phone,msg):

        if str(phone)[0] == '0':
            self.phone = str(phone).replace('0','+265',1)

        elif str(phone)[0] == '2':
            self.phone = str(phone).replace('2','+2',1)

        else:# phone[0] == '+':
            self.phone = str(phone)

        

        self.msg = msg

    
    def go(self):
        account = "AC30b188ff517402a929786e3441ecbdd4"
        token = "76c28d21d6931f8376c4ac312e6c0b39"
        client = TwilioRestClient(account, token)

        message = client.sms.messages.create(to=self.phone,
                                     from_="+12018903924",
                                     body=self.msg)


d=sendMessage(+265881460566,"hih")


class adminSendMessage():

    
    

    def __init__(self,msg):

        
        
        

        self.msg = msg

    def StartList(self):
        Filter=raw_input("filter by :")
        userTosend = use.objects.filter(active=Filter)
        listOfuser =[x for x in userTosend]
        return listOfuser
    def go(self):
        userList=self.StartList()
        
        for i in userList:
          try:
            phone=i.Phone_number
            if str(phone)[0] == '0':
                phone = str(phone).replace('0','+265',1)

            elif str(phone)[0] == '2':
                phone = str(phone).replace('2','+2',1)

            else:# phone[0] == '+':
                phone = str(phone)
            
            account = "AC30b188ff517402a929786e3441ecbdd4"
            token = "76c28d21d6931f8376c4ac312e6c0b39"
            client = TwilioRestClient(account, token)
            
            message = client.sms.messages.create(to=phone,
                                         from_="+12018903924",
                                         body=str(i.first_name) + "! " + str(self.msg))
            print "sent to" + " " + str(i)
          except Exception,e:
              print "failed to send to" + " " + str(i) + " " + "because" + " " + str(e) 

    def test(self):
        d= self.StartList()
        for i in d:
            print i
#it seems you were not able to edit your profile,now visit http://affixmw.com/signUp/profileEditAll/ to complete.


d=sendMessage(+265881460566,"hih")

