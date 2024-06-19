print("Welcome to trasure Island")
print("Your mission is to find the treasure")

direction  = input("You want to go left or right? - ")

#First 
if(direction == "right"):
    print("Game Over")

else:#Second
    direction  = input("You want to swin or wait? - ")
    if(direction == "swin"):
        print("Game Over")

    else:#third
        direction  = input("which door? blue, red or yellow - ")
        if(direction == "blue" or direction == "red"):
            print("Game Over")
        else:
            print("You Win")    
    