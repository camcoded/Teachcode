


def Deposit(Amount, Balance, Date, FW):
	newBalance=Balance+Amount
	print(Date+"||"+str(Amount)+"|| ||"+str(newBalance), file=FW)
	return newBalance

def Withdrawal(Amount, Balance, Date, FW):
	newBalance = Balance - Amount
	print(Date+"||"+str(Amount)+" || ||"+str(newBalance), file=FW)
	return newBalance


def printReceipt():
	FR = open("receipt.txt","r")
	for x in FR:
		print(x)

createReceipt=open("receipt.txt","w")
print("date||credit||debit||balance")

 




Balance=0


FW=open("receipt.txt", "a")
Balance = Deposit(1000, Balance, "10/01/2012", FW)

Balance = Deposit(2000, Balance, "13/01/2012", FW)

Balance = Withdrawal(500, Balance, "14/01/2012", FW)




FW.close()
createReceipt.close()
printReceipt()
