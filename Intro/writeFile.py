import datetime as dt
msg = input("Enter message: ")
time = str(dt.datetime.now())
with open("sample.txt",'w') as file:
    file.write(msg)
    file.write(time)