print("welcome to the roller_cost")
height=int(input("enter you height"))

if height>=120:
    print("yes you can ride the roller_cost")
    age=int(input("enter your age"))
    if age<12:
        print("you have to pay $5")
        bill=5
    elif age<=18:
        print("you have to pay $7")
        bill=7
    else:
        print("you have to pay $12")
        bill=12

    want_photo=input("do you want to take a photo(y/n)")
    if want_photo== 'y':
         bill=bill+3
         print("bill amount is ",bill)
