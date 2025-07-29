print("welcome to the pizza world")
size=input("what size of pizza do you need\n1=small\n2=medium\n3=large")
if size=='1':
    bill=15
elif size=='2':
    bill=20
else:
    bill=25
peperoni=input("do you need peperoni on your pizza(y/n)")
if peperoni=='y':
    if size=='1':
     bill=bill+2
    elif size=='2':
     bill=bill+3
    elif size=='3':
        bill=bill+3
extra_cheese=input("do you need extra cheese(y/n)")
if extra_cheese=='y':
     bill=bill+1
     print("bill=",bill)




