def timetable(t1,t2):
    while t1<=t2:
        print("timestable of",t1)
        A = 1
        while A <= 10:
            print (t1,"x",A,"=",(A*t1))
            A=A+1
            t1 =t1 + 1

timetable(2,10)            
