

class bankaccount():
	
	name=""
	balance=0.0

	def __init__(self, balance):
		self.balance= balance

	def deposit(self, atm):
		self.balance+=atm
		return self.balance

	def withdraw(self, atm):
		if atm<= self.balance:
			self.balance-=atm


	
			
						
		else:
			print("insufficent funds")

		return self.balance

		



