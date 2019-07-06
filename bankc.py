from bankaccountclasses import bankaccount

def printReceipt():
	FR = open("receipt.txt","r")
	for x in FR:
		print(x)


createReceipt=open("receipt.txt","w")
print("date  ||  credit  ||  debit  ||  balance", file=createReceipt)
FW=open("receipt.txt", "a")


user = bankaccount(1000.0)



balance = user.deposit(1000.0, "02/01/2012", FW)
user.withdraw(500.0)

FW.close()
printReceipt()
