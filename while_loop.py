

def ones(no):
    result=""
    if no==1:
        result="one"
    elif no==2:
        result="two"
    elif no==3:
        result="three"
    elif no==4:
        result="four"
    elif no==5:
        result="five"
    elif no==6:
        result="six"
    elif no==7:
        result="seven"
    elif no==8:
        result="eight"
    elif no==9:
        result="nine"
    elif no==10:
        result="ten"
    elif no==11:
        result="eleven"
    elif no==12:
        result="twelve"
    elif no==13:
        result="thirteen"
    elif no==14:
        result="fourteen"
    elif no==15:
        result="fifteen"
    elif no==16:
        result="sixteen"
    elif no==17:
        result="seventeen"
    elif no==18:
        result="eighteen"
    else:
        result="nineteen"
    return result

def ty(no):
    result=" "
    if no == 20:
        result="twenty"
    elif no == 30:
        result="thirty"
    elif no == 40:
        result="forty"
    elif no==50:
        result="fify"
    elif no==60:
        result="sixty"
    elif no==70:
        result="seventy"
    elif no==80:
        result="eighty"
    elif no==90:
        result="ninety"


num=int(input("Enter any number:"))

if num > 1:
    print(ones(result))

if num > 99:
    print(ones(int(num/100))+"hundred"+ty(int(num%100/10)*10)+ones(num%100%10))


