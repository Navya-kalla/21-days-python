import random
print("Number Guessing Game!!👾")
print("""📜RULES:
      👉 YOU WILL HAVE 5 CHANCES TO GUESS THE NUMBER
      👉 THE NUMBER WIL BE IN THE POSSIBLE RANGE ONLY""")
while True:
    secret_number = random.randint(1,100)
    guess = int(input("🤔 Enter a random number between 1 to 100:"))
    chances=4
    while guess!=secret_number and chances>0:
        if guess<secret_number:
            print("Increase the guess⬆️\n")
        else:
            print("Decrease the guess⬇️\n")
        guess = int(input(f"🤔 Guess again you have {chances} left:"))
        chances-=1
    if guess==secret_number:
        print("🎉You guessed it right!!!🥳")
    else:
        print(f"Sorry you lost😔!!! The number was {secret_number}")
    choice = input("👉One more Round!!(y/n):")
    if choice.lower()=="n":
        break
    