class ATM:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def balance(self):
        print("Your balance is:10000000")
    def withdrawal(self,amount):
        newAmount=10000000-amount
        print("Your new balnce is ",newAmount)
def main():
    cardNumber=input("Please enter your card number: ")
    pinNumber=input("Please enter your pin number: ")
    A1=ATM(pinNumber,cardNumber)
    print("Choose your activity(Enter 1 for balnceEnquiry and 2 for withdrawal): ")
    activity=int(input("Enter your activity:"))
    if activity==1:
        A1.balance()
    elif activity==2:
        amount=int(input("Enter the amount you want to withdraw: "))
        A1.withdrawal(amount)
    else:
        print("enter a valid number")
if __name__=="__main__":
    main()
