def printreverse(message):
    i=len(message)-1
    word=" "
    while i >= 0:
        if message[i:i+1]==" ":
            print(word)
            word=" "
        else:
            word=message[i:i+1] + word
        i-=1
        print(word)
