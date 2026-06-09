import random
freq = {1:0,2:0,3:0,4:0,5:0,6:0}
def roll_dice(n):
    for i in range(1,n+1):
        dice = random.randint(1,6)
        print(f"Roll {i} :{dice}")
        freq[dice] +=1
    print(f"\nTotal Rolls: {n}")

def view_frequency():
    print("\n==FREQUENCY REPORT==")
    for number,count in freq.items():
        print(f"{number} appeared {count} times")

def most_frequency():
    print("\n==MOST FREQUENT ROLL==")
    most_frequent = max(freq,key = freq.get)
    print(f"Number: {most_frequent}")
    print(f"Appeared: {freq[most_frequent]} times")

print("🎲DICE ROLLING SIMULATOR!🎲")
while True:
    try:
        n = int(input("How many times do you want to roll the die: "))
        if n>0:
            break
        print("Enter a value greater than 0")
    except:
        print("❌Invalid!!❌")
#Rolling Simulation
roll_dice(n)

print("\n===STATS===")
view_frequency()
most_frequency()

