# Number Guessing Game 

A fun command-line number guessing game built using Python.

The computer randomly selects a secret number based on the chosen difficulty level, and the player must guess it using the hints provided. Players can also choose to make the game more challenging by setting a limit on the number of attempts.

---

## Features

-  Random secret number generation
-  Three difficulty levels:
  - Easy (1–50)
  - Medium (1–100)
  - Hard (1–500)
-  Higher/Lower hints after each guess
-  Optional attempt limit (Challenge Mode)
-  Counts the number of attempts
-  Input validation for guess range
-  Play Again option
-  Reveals the secret number if the player runs out of attempts

---

## Technologies Used

- Python 3
- `random` module

---

## Concepts Practiced

- Variables
- User Input
- Conditional Statements (`if`, `elif`, `else`)
- Nested Loops
- Random Number Generation
- Input Validation
- Loop Control
- Counters
- Basic Game Logic

---

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or any Python IDE.
3. Run the program:

```bash
python guessing_game.py
```

---

## Future Improvements

- Difficulty-based default attempt limits
- Scoreboard and high scores
- Timed mode
- Input error handling for non-numeric values
- Graphical User Interface (GUI)
- Two-player mode
- Hint system (e.g., "You're within 10 numbers!")

---

## Sample Gameplay

```text
Choose a difficulty level:
Easy: 1-50
Medium: 1-100
Hard: 1-500

Feeling brave? Set an attempt limit! (yes/no)
yes

Ohh great, what is your limit?
5

I have chosen a secret number between 1 and 100.
Guess the secret number:
50
Too high! Try a lower number.
25
Too low! Try a higher number.
37
Congratulations! You have guessed the number in 3 attempts!!
```

---

## Author

**Shivani Dev Bahadur**