# IS 3020 Final Project

## Student and Project Information

- Student name: Tolina Yussuf
- GitHub username: tyussuf
- Project title: Pitch Match
- Application purpose: Pitch Match is a Python application that helps newly interested American futbol (soccer) fans decide which club to follow after the World Cup.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.

Required Python version: Python 3.10 or later.

Required files: pitch_match.py, and the data folder containing clubs.csv and results.csv, with the data folder in the same directory as pitch_match.py.

Steps to run in PyCharm:
1. Open this project folder in PyCharm.
2. Confirm that pitch_match.py and the data folder, containing clubs.csv and results.csv, appear in the Project panel.
3. Right-click pitch_match.py and select Run 'pitch_match', or open the file and click the green Run arrow.
4. Follow the on-screen menu in the Run console to take the quiz, view past results, compare two clubs, or exit.


## Major Features

List the major user-facing features implemented in the final application.

Major Features:
- A four-question quiz covering club values, playing style, player type, and city preference.
- A scoring system that compares the user's answers against a database of eight clubs and returns a ranked top-3 list.
- A results log that saves each completed quiz with the username, date, and top 3 matches, and lets the user view past results from the menu.
- A club comparison feature that displays two clubs side by side across their attributes.
- A rivalry warning that alerts the user if two of their top 3 matches are historic rivals.
- Input validation that re-prompts the user instead of crashing when an invalid quiz answer or menu choice is entered.

## Python Concepts Used

Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.

- Functions: the program is broken into functions with a single responsibility each, including load_club_data(), display_welcome(), validate_input(), run_quiz(), score_clubs(), get_top_matches(), display_matches(), check_rivalry(), compare_clubs(), find_club_by_name(), save_result(), view_saved_results(), and main().
- Dictionaries/Collections: dictionaries are used throughout the program. Clubs are stored as a list of dictionaries loaded from clubs.csv, quiz questions are stored as a list of dictionaries, and a user's answers are stored in a dictionary keyed by attribute. Known club rivalries are stored as a list of sets so a pair matches regardless of order.
- Conditionals: if, elif, and else statements drive the main menu, the attribute matching inside score_clubs(), and the rivalry check inside check_rivalry().
- Loops: for loops iterate over quiz questions, clubs, and CSV rows. A while loop inside run_quiz() re-prompts the user until a valid answer is entered, and another while loop drives the main menu until the user chooses to exit.
- File persistence: clubs.csv is read at startup using Python's csv module and loaded into a list of dictionaries. results.csv is appended to after every completed quiz and read back in when the user views past results.
- Exception handling: try and except blocks are used in three places. Invalid quiz or menu input raises and catches ValueError, a missing or unreadable clubs.csv is caught with FileNotFoundError and csv.Error, and file errors when saving or loading results are caught with IOError. Each produces a clear message instead of an unhandled crash.

## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.

- data/clubs.csv: the static club database, with one row per club. Its columns are name, league, founded, city, values, style, players_type, star_players, and honors. The values, style, and players_type columns use a fixed set of category words so they can be matched exactly against the user's quiz answers.
- data/results.csv: the results log, with one row added per completed quiz. Its columns are username, date, match_1, match_2, and match_3. A new row is appended each time a user finishes the quiz, and the file is read back in for the "view past results" menu option.

## Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.

- Normal quiz flow: completing the quiz with valid answers produces a ranked top-3 list with correct scores and profiles.
- Invalid quiz input: entering an option outside the listed choices.
- Invalid menu input: entering a number outside the menu range shows an error message and redisplays the menu.
- Rivalry detection: answering the quiz so two rival clubs (e.g. Real Madrid and FC Barcelona) land in the top 3 triggers the rivalry warning.
- Club comparison: comparing two valid club names prints a correct side-by-side view; entering a misspelled or unknown club name shows an error instead of crashing.
- Saving and viewing results: completing multiple quizzes appends a new row each time, and "View past results" correctly lists every saved entry.
- Missing data file: renaming `clubs.csv` and running the app produces a clear error message and controlled exit instead of a raw traceback.
- Empty results file: viewing past results before any quiz has been completed shows a "No saved results yet" message.

## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.

AI (Claude) was used during the improvement stage after the original working version was complete. 
The most important AI-assisted improvements were, adding try/except handling around loading `clubs.csv` and `results.csv` so missing or corrupted files fail normally, adding docstrings and comments to every function, and implementing the two optional features from the proposal, club comparison and rivalry warnings.