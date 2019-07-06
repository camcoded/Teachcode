salary=int("Enter salary: ")

if salary>2000:
	print("tax rate is 27")
	tax=salary*27/100
	print("Net salary is",(salary-tax))
if salary<2000:
	print("tax rate is 118")
	tax=salary*18/100
	print("net salary",(salary-tax))