import random

print("Random Number Generator")

start_over = 0

while start_over == 0:

    print("Choose a difficulty level (Range):")
    print("Easy: 1-50")
    print("Medium: 1-100")
    print("Hard: 1-500")

    option = 0
    while option == 0:
        diff_level = input().lower()

        if diff_level == "easy":
            n = 51
            option += 1

        elif diff_level == "medium":
            n = 101
            option += 1

        elif diff_level == "hard":
            n = 501
            option += 1

        else:
            print("Invalid entry")

    print("Feeling brave? Set an attempt limit! (yes/no)")
    attempt_choice = input().lower()

    if attempt_choice == "yes":
        print("Ohh great, what is your limit?")
        limit = int(input())

    elif attempt_choice == "no":
        limit = n

    print("Excellent choice!!")

    secret_number = random.randint(1, n - 1)

    print("I have chosen a secret number between 1 and", n - 1, ". Can you guess it?")
    print("Guess the secret number:")

    attempt = 1
    choice = 0

    while choice < n:

        if attempt <= limit:

            user_num = int(input())

            if user_num >= n or user_num < 1:
                print("Please guess a number within the chosen range")

            elif user_num < secret_number:
                print("Too low! Try a higher number.")
                attempt += 1

            elif user_num > secret_number:
                print("Too high! Try a lower number.")
                attempt += 1

            elif user_num == secret_number:

                print("Congratulations! You have guessed the number in",
                      attempt, "attempts!!")

                print("Do you want to play again? (yes/no)")
                user_choice = input().lower()

                if user_choice == "no":
                    choice = n + 1
                    start_over = 1

                else:
                    choice = n + 1
                    start_over = 0

        elif attempt > limit:

            print("You're out of attempts! Good game :)")
            print("The secret number was", secret_number)

            print("Do you want to play again? (yes/no)")
            user_choice = input().lower()

            if user_choice == "no":
                choice = n + 1
                start_over = 1

            else:
                choice = n + 1
                start_over = 0

print("Thank you!!")