# Snake Water Gun Game
"""Created BY Anubhav Chaurasia"""

# Importing Modules Required
import random

# Global Scores
User_Score = 0
Computer_Score = 0

# Welcome Message
def Greetings():
    global User_Score, Computer_Score
    User_Score = 0
    Computer_Score = 0
    print("")
    print("Welcome To Snake Water Gun Game")
    print("Created By Anubhav Chaurasia")
    print("")
    Name = input("Enter Your Name : ")
    print("")
    print(f"Hello , {Name} ,Let's Start The Game")
    print("Rules: Snake Drinks Water, Water Rusts Gun, Gun Shoots Snake.")
    print("Type 'quit' To Exit The Game.")
    print("")
    Game01()

# List Of Choice And Input
List = ["Snake" , "Water" , "Gun"]

# Game System
def Game01():
    global User_Score, Computer_Score
    # Random Choice Of Computer - Moved Inside The Function So It Changes Each Round
    Random = random.choice(List)
    # User Input
    while True:
        Input = input("Choose Any Thing :=> (Snake , Water , Gun) Or 'Quit' To Exit The Game : ").strip().capitalize()
        if Input == "Quit":
            print(f"\nFinal Scores - You: {User_Score}, Computer: {Computer_Score}")
            if User_Score > Computer_Score:
                print("You Won The Game!")
            elif User_Score < Computer_Score:
                print("Computer Won The Game!")
            else:
                print("It's a Tie!")
            return  # Exit The Game
        # Error Handling
        if Input not in List:
            print("Invalid Input !! Error , You Have To Choose : 'Snake' , 'Water' , 'Gun' or 'Quit'")
        else:
            Result = MainGame(Input, Random)
            if Result == "Win":
                User_Score += 1
            elif Result == "Lose":
                Computer_Score += 1
            print(f"Scores - You: {User_Score}, Computer: {Computer_Score}")
            break 

# Conditions Of Game
def MainGame(Input, Random):
    # Print What Computer Choose
    print("")
    print("Computer Choose :" , Random)
    print("You Choose:", Input)
    
    # Determine Winner
    if Random == Input:
        print("Draw ...")
        return "Draw"
    elif (Random == "Snake" and Input == "Water") or \
         (Random == "Water" and Input == "Gun") or \
         (Random == "Gun" and Input == "Snake"):
        print("You Lose This Chance Let's Do It Again")
        return "Lose"
    else:
        print("You Won This Chance Let's Do It Again")
        return "Win" 

# Executing The Game From Greeting Function
Greetings()