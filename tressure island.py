print("Welcome to Treasure Island\nYour mission is to find the treasure")
direction=input("you are at a cross road .where do you need to go?\n       Type left or right")
if direction=='left':
    option=input("do you need to go for option swim or wait for a boat")
    if option=='swim':
        print("attacked by trout \m   GAME OVER")
    elif option=='wait':
        option_door=input("A boat have arrived and you reached on land and you can see some houses\n     which door you need to go?\n      red,blue,yellow")
        if option_door=='red':
            print("Burned by fire .Game over ")
        elif option_door=='blue':
            print("Game over")
        elif option_door=='yellow':
            print("you win!!!!")
        else:
            print("you loose")
elif direction=='right':
    print("game over ")
else:
    print("game over")
