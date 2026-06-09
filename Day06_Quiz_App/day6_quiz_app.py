import random
score = 0 # inital score

#List of questions
questions = [
  {
    "question": "What is the largest ocean on Earth?",
    "options": [
      "A. Atlantic Ocean",
      "B. Indian Ocean",
      "C. Arctic Ocean",
      "D. Pacific Ocean"
    ],
    "answer": "D"
  },
  {
    "question": "What is 12 times 12?",
    "options": [
      "A. 132",
      "B. 144",
      "C. 154",
      "D. 164"
    ],
    "answer": "B"
  },
  {
    "question": "Which planet is known as the Red Planet?",
    "options": [
      "A. Venus",
      "B. Mars",
      "C. Jupiter",
      "D. Saturn"
    ],
    "answer": "B"
  },
  {
    "question": "Who painted the Mona Lisa?",
    "options": [
      "A. Vincent van Gogh",
      "B. Pablo Picasso",
      "C. Leonardo da Vinci",
      "D. Claude Monet"
    ],
    "answer": "C"
  },
  {
    "question": "What is the chemical symbol for gold?",
    "options": [
      "A. Go",
      "B. Gd",
      "C. Au",
      "D. Ag"
    ],
    "answer": "C"
  },
  {
    "question": "Which country is home to the Great Barrier Reef?",
    "options": [
      "A. Brazil",
      "B. Australia",
      "C. South Africa",
      "D. Egypt"
    ],
    "answer": "B"
  },
  {
    "question": "What is the boiling point of water at sea level?",
    "options": [
      "A. 90°C",
      "B. 100°C",
      "C. 110°C",
      "D. 120°C"
    ],
    "answer": "B"
  },
  {
    "question": "How many continents are there on Earth?",
    "options": [
      "A. 5",
      "B. 6",
      "C. 7",
      "D. 8"
    ],
    "answer": "C"
  },
  {
    "question": "What is the square root of 64?",
    "options": [
      "A. 6",
      "B. 7",
      "C. 8",
      "D. 9"
    ],
    "answer": "C"
  },
  {
    "question": "Which is the longest river in the world?",
    "options": [
      "A. Amazon River",
      "B. Nile River",
      "C. Yangtze River",
      "D. Mississippi River"
    ],
    "answer": "B"
  }
]
random.shuffle(questions) #shuffling the order of questions

for index,q in enumerate(questions,start=1):
    print(f"\nQuestion {index}")
    print(q["question"])

    for o in q["options"]:
        print(o)

    while True:
        answer = input("Enter the option(A/B/C/D): ").strip().upper()
        if answer in ['A','B','C','D']:
            break
        else:
            print("Invalid option!")

    if answer == q["answer"]:
        score +=1
    else:
        print(f"Incorrect. The correct answer was {q['answer']}.\n")

print(f"Your score : {score}/{len(questions)}")
percentage = (score/len(questions))*100
print(f"Percentage : {percentage}%")

if percentage == 100:
    print("Perfect score!!")
elif percentage>=90:
    print("Excellent!!")
elif percentage>=70:
    print("Goodd")
elif percentage>=50:
    print("Average")
else:
    print("Need Improvement")