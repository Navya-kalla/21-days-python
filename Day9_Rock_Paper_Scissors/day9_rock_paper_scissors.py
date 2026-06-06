import random

moves = ["Rock","Paper","Scissors"]

def determine_winner(user_move,computer_move):
    if (user_move == "Rock" and computer_move == "Scissors") or (user_move == "Scissors" and computer_move == "Paper") or (user_move == "Paper" and computer_move == "Rock"):
        return "user"
    elif (user_move==computer_move):
        return "draw"
    else:
        return "computer"

def game(user_move):
    computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")
    return determine_winner(user_move,computer_move)

def final_score(user_score,computer_score,draw_score):
    print("\n===== FINAL SCORE =====")
    print(f"Your score : {user_score}")
    print(f"Computer score : {computer_score}")
    print(f"Draw score : {draw_score}")

while True:
    user_score = 0
    computer_score = 0
    draw_score = 0

    print("🗿📄✂️ ROCK PAPER SCISSORS!! 🗿📄✂️")

    try:
        no_of_times = int(input("👉 Do you want to a best of (3 or 5): "))
        if no_of_times not in [3,5]:
            print("👉 Please enter only 3 or 5")
            continue
    except ValueError:
        print("❌ Invalid number is entered ❌")
        continue

    winning_score = no_of_times // 2 + 1
    while(user_score<winning_score and computer_score<winning_score):
        user_move = input("Enter your move(rock / paper / scissors):  ").strip().capitalize()
        if user_move not in moves:
            print("❌ Invalid move! ❌")
            continue
        winner = game(user_move)

        if winner == "user":
            user_score +=1
            print("You won this round!!")
        elif winner == "computer":
            computer_score +=1
            print("Computer won this round!!")
        else:
            draw_score +=1
            print("It's a draw!")
        
    final_score(user_score,computer_score,draw_score)

    if user_score > computer_score:
        print(f"🎉 You won the match by reaching {winning_score} points!")    
    else:
        print("Computer won the match!!")

    choice = input("Wanna play again(y/n) : ")
    if choice.lower()=='n':
        print("🤗 Thanks for playing!! 🤗")
        break