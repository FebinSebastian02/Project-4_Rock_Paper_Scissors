#imports are done
import random
def main():
    print("\n!!!Welcome to the game!!!")
    userScore = 0
    comScore = 0
    while True:
        list = ['rock', 'paper', 'scissors']
        comTurn = random.choice(list)
        userTurn = int(input("\nEnter an option...1) rock 2) paper 3) scissors 4) exit"))

        if userTurn == 1:
            if comTurn == 'rock':
                print("User:- rock")
                print("Computer:- " + comTurn)
                print("It's a tie")
            elif comTurn == 'paper':
                print("User:- rock")
                print("Computer:- " + comTurn)
                print("Computer scores")
                comScore += 10
            elif comTurn == 'scissors':
                print("User:- rock")
                print("Computer:- " + comTurn)
                print('User scores')
                userScore += 10
        elif userTurn == 2:
            if comTurn == 'rock':
                print("User:- paper")
                print("Computer:- " + comTurn)
                print("User scores")
                userScore += 10
            elif comTurn == 'paper':
                print("User:- paper")
                print("Computer:- " + comTurn)
                print("It's a tie")
            elif comTurn == 'scissors':
                print("User:- paper")
                print("Computer:- " + comTurn)
                print('Computer scores')
                comScore += 10
        elif userTurn == 3:
            if comTurn == 'rock':
                print("User:- scissors")
                print("Computer:- " + comTurn)
                print("Computer scores")
                comScore += 10
            elif comTurn == 'paper':
                print("User:- scissors")
                print("Computer:- " + comTurn)
                print("User scores")
                userScore += 10
            elif comTurn == 'scissors':
                print("User:- scissors")
                print("Computer:- " + comTurn)
                print("It's a tie")
        elif userTurn == 4:
            print("\nUser scored:- {}\nComputer scored:- {}".format(userScore, comScore))
            if userScore > comScore:
                print("\nUser wins...")
            elif userScore == comScore:
                print("\nIt's a tie...")
            else:
                print("\nComputer wins...")
            print("\n!!!Bye,See you soon!!!")
            quit()
        else:
            print("Invalid choice entered")
main()