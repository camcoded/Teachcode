#!/usr/bin/python

def grades(per):

    name = input("Enter your name")
    phy = int(input("Enter physics marks"))
    che = int(input("Enter chemistory marks"))
    total = phy + che
    per = total * 100/300

    if per >= 90:
        print("A")
    elif per >= 80 and per < 90:
        print("B")
    elif per >= 70 and per < 80:
        print("C")
    else:
        print("fail")
    

    
    print("name:", name)
    print("totalmakrs:",total)
    print("percentary:",per)
    print("grade:", grades(total*100/300)