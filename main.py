# Snake beats water, Water beats gun, and gun beats snake
print("Welcome to the Snake Water Gun Game!")

player1=input("Please enter your name, player 1: ")
player2=input("Please enter your name, player 2: ")
turns = int(input(f"How many times would you like to play the game, {player1} and {player2}: "))

num=0
wins=[0,0]

while num<turns:
    choice1=input(f"{player1}, enter your move. s for Snake, w for water, and g for gun.")
    choice2=input(f"{player1}, enter your move. s for Snake, w for water, and g for gun.")

    choice1.strip()
    choice2.strip()

    if(choice1==choice2):
        print("You tied!")
        pass

    elif(choice1=='s' and choice2 =='w'):
        wins[0]+=1
        num+=1
        print(f"{player1}, you have won!")

    elif(choice1=='s' and choice2 =='g'):
        wins[1]+=1
        num+=1
        print(f"{player2}, you have won!")
        
    elif(choice1=='w' and choice2 =='g'):
        wins[0]+=1
        num+=1
        print(f"{player1}, you have won!")

    elif(choice1=='w' and choice2 =='s'):
        wins[1]+=1
        num+=1
        print(f"{player2}, you have won!")

    elif(choice1=='g' and choice2 =='s'):
        wins[0]+=1
        num+=1
        print(f"{player1}, you have won!")

    elif(choice1=='g' and choice2 =='w'):
        wins[1]+=1
        num+=1
        print(f"{player2}, you have won!")
   
print(f"{player1} has won {wins[0]} times and {player2} has won {wins[1]} times!")





