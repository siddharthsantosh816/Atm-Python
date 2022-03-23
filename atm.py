class Atm():
    def __init__(self,card,pin,amount):
        self.card=card
        self.pin=pin
        self.amount=amount
      

    def display(self):
        print('Card No: '+ self.card)
        print('Pin: '+self.pin)
        print('Amount: '+self.amount)
        


c=input('Enter your card number')
p=input('Enter your pin')
a=input('Enter amount')


object=Atm(c,p,a)
object.display()