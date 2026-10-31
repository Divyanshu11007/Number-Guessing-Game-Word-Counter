# Number Guessing Game & Word Counter

Two beginner-friendly, standalone Python command-line programs in one project:

1. **Number Guessing Game** — a terminal game with randomized secrets, an attempt counter, and a scoring system.
2. **Word Counter** — a file-based tool that reads a text file and performs word frequency analysis.

Built as a practice project to understand loops, the `random` module, and basic string manipulation in Python.

## Features

### Number Guessing Game

- Secret number generated with **Python's `random` module** (`random.randint`).
- Three difficulty levels:
  - Easy — 1 to 50
  - Medium — 1 to 100
  - Hard — 1 to 200
- **Attempt counter** that only counts real guesses (invalid input does not count against you).
- **Scoring system** — you start with 100 points and lose 10 for every extra attempt (minimum 10 points). Fewer guesses means a higher score.
- Hints after every guess: "Too low!" or "Too high!".
- Tracks the **best score of the session** across multiple rounds.

### Word Counter

- Reads any text file you specify (loops until a readable file is provided).
- **Text file reading** with friendly error handling for missing or unreadable files.
- Counts **total words** and **unique words**.
- **Word frequency analysis**: words are lowercased, punctuation is stripped, and each word is tallied in a dictionary.
- Shows the **top N most frequent words** (you choose N).
- Optionally saves a full frequency report to `word_frequency_report.txt`.

## Getting Started

### Prerequisites

- Python 3 installed on your machine (no external libraries required).

### Running the Programs

1. Clone the repository:

   ```bash
   git clone https://github.com/Divyanshu11007/Number-Guessing-Game---Word-Counter.git
   cd Number-Guessing-Game---Word-Counter
   ```

2. Run either program:

   ```bash
   # Start the guessing game
   python number_guessing_game.py

   # Analyze a text file
   python word_counter.py
   ```

## Example Sessions

### Number Guessing Game

```
Choose an option (1-3): 2
I am thinking of a number... let's see how fast you find it!
Guess a number between 1 and 100: 50
Too low! Try again.
Guess a number between 1 and 100: 75
Too high! Try again.
Guess a number between 1 and 100: 63

Well done! The number was 63.
Attempts: 3 | Score: 80
New best score this session: 80
```

### Word Counter

```
Enter the name of the text file: sample.txt

Total words: 42
Unique words: 27

How many top words to show (1-27)? 5
--- Top 5 most frequent words ---
1. the - 4 time(s)
2. and - 4 time(s)
3. python - 3 time(s)
4. is - 3 time(s)
5. fox - 2 time(s)

Save the full frequency report to word_frequency_report.txt? (y/n): y
Report saved as word_frequency_report.txt.
```

## Notes

- The `word_counter.py` program works with plain `.txt` files; point it at any file you like.
- `word_frequency_report.txt` is only created when you choose to save a report, so it is safe to delete or ignore.
- Input validation with `while` loops is used throughout — neither program crashes on bad input.

## Project Goal

These programs demonstrate:

- `while` loops, `for` loops, and loop-controlled repetition
- The `random` module (`random.randint`)
- Basic string manipulation (`split`, `strip`, `lower`) and `string.punctuation`
- Dictionaries for counting and `sorted` for ranking
- File reading with `open` / `with` and error handling with `try` / `except`
- Functions, return values, and modular program design

## License

This project is free to use and modify for learning purposes.
