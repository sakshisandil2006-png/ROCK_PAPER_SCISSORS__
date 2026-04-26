from utils import choices
from game_rules import comp_choice,logic
def game():
    you=0
    i=0
    print("Hello there.\nBored??? Let's play rock, paper,scissors. TO EXIT PRESS 0")
    while True:
        choice = input("Rock, paper, scissors shoot!\n").strip().lower()
        if choice=='0':
            print("Let's play some other time")
            if you>i:
                print("🎉 HURRAY! YOU WON 🎉")
            elif i>you:
                print("😎 I WON. BETTER LUCK NEXT TIME I GUESS 😎")
            elif i==you:
                print("OVERALL 👔")
            break
        elif choice not in choices:#elif for independent check and swap(not if)
            print("invalid input")
            continue
        comp =comp_choice()
        print("I choose",comp)
        result=logic(choice,comp)#no direct because count score
        print(result)
        if "--You won--" in result:#typo bugs risk 
            you+=1
        elif "--I won--" in result:
            i+=1
        print(f"Your score: {you} and my score: {i}")
game() 