t1=int(input("enter first no.: "))
t2=int(input("enter second no.: "))

while t1<=t2:
	print("_________________|")
	print("Times table of",t1,"|")
	i=1
	while i<=10:
		print(t1,"x",i,"=",(t1*i),"|")
		i=i+1
	t1=t1+1