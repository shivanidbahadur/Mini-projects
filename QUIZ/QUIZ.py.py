import random

print("=" * 50)
print("WELCOME TO THE ULTIMATE QUIZ CHALLENGE!")
print("=" * 50)
print("Think you're a genius? Let's find out")

start_over = 0


def congratulate(score):
    if score == 20:
        print("Perfect score! You're a quiz legend!")
    elif score >= 15:
        print("Excellent job!")
    elif score >= 10:
        print("Well done!")
    else:
        print("Nice try! Play again and beat your score!")

while start_over == 0:
    print("Choose your game mode:")
    print("1. Classic (Answer all 20 questions)")
    print("2. Extreme (One mistake... and it's GAME OVER!)\n")

    game_mode_choice = input().lower()

    print("Excellent choice!!")
    print("\nGet ready...")
    print("Questions are loading...")
    print("Good luck!\n")

    quiz = [
        {"question": "What is the largest planet in our Solar System?", "answer": "jupiter"},
        {"question": "Which is the fastest land animal?", "answer": "cheetah"},
        {"question": "How many continents are there on Earth?", "answer": "7"},
        {"question": "What is the capital of Japan?", "answer": "tokyo"},
        {"question": "Which gas do plants absorb from the atmosphere?", "answer": "carbon dioxide"},
        {"question": "What is the chemical symbol for gold?", "answer": "au"},
        {"question": "Who invented the telephone?", "answer": "alexander graham bell"},
        {"question": "Which is the largest ocean in the world?", "answer": "pacific ocean"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
        {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
        {"question": "How many days are there in a leap year?", "answer": "366"},
        {"question": "Which bird is the national bird of India?", "answer": "peacock"},
        {"question": "Which is the smallest prime number?", "answer": "2"},
        {"question": "Which instrument is used to measure temperature?", "answer": "thermometer"},
        {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
        {"question": "Which country is famous for the Eiffel Tower?", "answer": "france"},
        {"question": "What does CPU stand for?", "answer": "central processing unit"},
        {"question": "Which sport uses a shuttlecock?", "answer": "badminton"},
        {"question": "How many colors are there in a rainbow?", "answer": "7"},
        {"question": "Which is the largest mammal in the world?", "answer": "blue whale"}
    ]

    random.shuffle(quiz)

    if game_mode_choice == "classic" or game_mode_choice=="1":
        score = 0
        for question in quiz:
          
            print(question["question"])
            ans = input("\nAnswer: ").strip().lower()

            if ans == question["answer"]:
                print("Correct!")
                score+=1
            else:
                print("Wrong!")
                print("The correct answer was:", question["answer"])
        print(f"\nYour final score is {score}/{len(quiz)}")
        congratulate(score)

    elif game_mode_choice == "extreme" or game_mode_choice=="2":
        score=0
        for question in quiz:
           
            print(question["question"])
            ans = input("\nAnswer: ").strip().lower()

            if ans == question["answer"]:
                print("Correct!")
                score+=1
            else:
                print("Wrong!")
                print("\nGAME OVER!")
                print("One wrong answer ended your streak!")
                print("The correct answer was:", question["answer"])
                break
        print(f"You survived {score} question(s)!")
        congratulate(score)
    else:
         print("Invalid choice! Please enter 1 or 2.")
         continue
        
    while True:
        user_choice = input("Do you want to play again? (yes/no): ").lower()

        if user_choice == "yes":
            break
        elif user_choice == "no":
            start_over = 1
            break
        else:
            print("Please enter yes or no.")
print("Thank you")