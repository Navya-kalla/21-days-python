import random

print("PASSWORD GENERATOR")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="!@#$%^&*_"
digits = "0123456789"
while True:
    password_length=int(input("Length of the password: "))
    symbols_choice = input("Do you want any symbols in the password(y/n):").lower()
    digit_choice = input("Do you want any digits in your password(y/n): ").lower()

    for i in range(5):
        password=""
        if(symbols_choice=="y" and digit_choice == "y"):
            pool = characters+symbols+digits
        elif(symbols_choice=="n" and digit_choice == "y"):
            pool = characters+digits
        elif(symbols_choice=="y" and digit_choice == "n"):
            pool = characters+symbols
        else:
            pool = characters
        for i in range(password_length):
            password += random.choice(pool)

        has_upperchar = False
        has_lowerchar = False
        has_digits = False
        has_symbols = False

        for char in password:
            if char.isupper():
                has_upperchar = True
            elif char.islower():
                has_lowerchar = True
            elif char.isdigit():
                has_digits = True
            elif char in symbols:
                has_symbols = True
        variety_score = sum([has_digits,has_lowerchar,has_symbols,has_upperchar])

        if password_length>10 and variety_score>=3:
            strength = "VERY STRONG"
        elif password_length>5 and variety_score>=2:
            strength = "GOOD"
        else:
            strength = "WEAK"
        print(f"{password}-->{strength}")
    break
