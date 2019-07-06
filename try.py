def findandreplace(message,find,replace):
    i=0
    newmessage=" "
    while i<len(message): #start of the message
        if message[i:i+1]==find[0:1]: #message from 0:1 is the same as find first letter
            if message[i:i+len(find)]==find:
                newmessage+=replace
                i=i+len(find)-1
            else:
                newmessage+=message[i:i+1]
        else:
            newmessage+=message[i:i+1] #put the first letter in newmessage

        i+=1
    print(newmessage)

findandreplace("hello peter, my name is peterp","peter","cameron")
