from os import path as p
import datetime
file1 = ""
file2 = ""
while p.isfile(file1) == False:
    file1 = str(input("File1 : "))
while p.isfile(file2) == False:
    file2 = str(input("File2 : "))
print("File1 Size :",p.getsize(file1))
print("File2 Size :",p.getsize(file2))
latest = max([file1,file2],key=p.getctime)
print("Latest File %s last edited %s"%(latest,datetime.datetime.fromtimestamp(p.getctime(latest))))
