from random import randint

class Train :
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print (f"Ticket is booked in train no.{self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no : {self.trainNo} in running on time !")
    def getFare(self,fro,to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(200,3000)}")
t=Train(21565)
t.book("Odisha","Delhi")
t.getStatus()
t.getFare("Odisha","Delhi")