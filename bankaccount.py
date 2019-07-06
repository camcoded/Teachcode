import time
import datetime
from bankaccountclasses import bankaccount



#name=input("Welcome, what is your name?")

#user2=bankaccount(name,balance)



#todaydate=datetime.date.today()

#print(todaydate)


def bankatm():

	pin=int(input("Welcome, Press 'Enter' pin to to proceed: "))

	if pin==int(1992):
		print("Please choose transaction (Enter number): ")

		print("1.Deposit")
		print("2.Withdraw")
		print("3.Statement")
		option=int(input())

		if option==1:
			
			balance=int(input("how much would you like to deposit? "))

			user1=bankaccount(balance)
			
			print(user1.balance)
			

	else:
		print("Access Denied")

bankatm()





