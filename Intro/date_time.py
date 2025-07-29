import datetime as dt
x = dt.datetime.now()

def printTime():
    print("Time: ",x.strftime("%X"))
def printDate():
    print("Date: ",x.strftime("%x"))

printTime()
printDate()