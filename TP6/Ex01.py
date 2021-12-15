L1 = [0]*3
for item in L1:
    print("Type : %s , ID : %s"%(type(item),id(item)))
L1[1] += 1
print("---------------------------------------------------")
for item in L1:
    print("Type : %s , ID : %s"%(type(item),id(item)))