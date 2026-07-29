import csv
from datetime import date

CLUBS_FILE = "data/clubs.csv"
RESULTS_FILE = "data/results.csv"

RIVALRIES = [
    {"Real Madrid", "FC Barcelona"},
    {"Real Madrid", "Atletico Madrid"},
    {"Manchester City", "Manchester United"},
    {"Arsenal", "Chelsea"},
]

QUIZ_QUESTIONS = [
    {
        "prompt": "What do you value most in a club?\n  a) Glory and trophies\n  b) Club identity and community\n  c) Attacking flair\n  d) Underdog story",
        "options": {"a": "glory", "b": "identity", "c": "flair", "d": "underdog"},
        "attribute": "values"
    },
    {
        "prompt": "What style of play do you enjoy watching?\n  a) Possession-based build up\n  b) High pressing intensity\n  c) Physical and direct\n  d) Fast counterattacks",
        "options": {"a": "possession", "b": "pressing", "c": "physical", "d": "counterattack"},
        "attribute": "style"
    },
    {
        "prompt": "What kind of player do you enjoy watching most?\n  a) Global superstars\n  b) Homegrown/local talent\n  c) Gritty, hard-working players\n  d) Young breakout stars",
        "options": {"a": "superstars", "b": "homegrown", "c": "gritty", "d": "breakout"},
        "attribute": "players_type"
    },
    {
        "prompt": "Which city are you drawn to?\n  a) London\n  b) Manchester\n  c) Madrid\n  d) Barcelona",
        "options": {"a": "London", "b": "Manchester", "c": "Madrid", "d": "Barcelona"},
        "attribute": "city"
    },
]


def load_club_data():
    clubs = []
    try:
        with open(CLUBS_FILE, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                clubs.append(row)
    except FileNotFoundError:
        print(f"Error: could not find {CLUBS_FILE}. Make sure the data folder "
              "is in the same directory as pitch_match.py.")
        raise SystemExit(1)
    except csv.Error as error:
        print(f"Error: {CLUBS_FILE} could not be read as a CSV file ({error}).")
        raise SystemExit(1)

    if not clubs:
        print(f"Error: {CLUBS_FILE} was found but contains no club data.")
        raise SystemExit(1)

    return clubs


def display_welcome():
    print("=" * 50)
    print("Welcome to Pitch Match!")
    print("=" * 50)
    print("Answer a few quick questions and we'll match you with your top 3 clubs.\n")


def validate_input(answer, valid_options):
    answer = answer.strip().lower()
    if answer in valid_options:
        return answer
    raise ValueError(f"'{answer}' is not one of the listed options.")


def run_quiz():
    answers = {}
    for question in QUIZ_QUESTIONS:
        print(question["prompt"])
        while True:
            user_answer = input("Your answer: ")
            try:
                valid_answer = validate_input(user_answer, question["options"])
                real_value = question["options"][valid_answer]
                answers[question["attribute"]] = real_value
                break
            except ValueError as error:
                print(f"Invalid input: {error} Please try again.")
        print()
    return answers


def score_clubs(answers, club_data):
    scores = []
    for club in club_data:
        score = 0
        for attribute, user_value in answers.items():
            if club.get(attribute) == user_value:
                score += 1
        scores.append((club, score))
    return scores


def get_top_matches(scores):
    sorted_scores = sorted(scores, key=lambda item: item[1], reverse=True)
    return sorted_scores[:3]


def display_matches(top_clubs):
    print("\nYour Top 3 Club Matches:")
    print("=" * 50)
    for rank, (club, score) in enumerate(top_clubs, start=1):
        print(f"{rank}. {club['name']} ({club['league']}) - Match score: {score}")
        print(f"   Founded: {club['founded']}")
        print(f"   City: {club['city']}")
        print(f"   Style: {club['style']}")
        print(f"   Star Players: {club['star_players']}")
        print(f"   Honors: {club['honors']}")
        print()


def check_rivalry(top_clubs):
    names = [club["name"] for club, score in top_clubs]
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pair = {names[i], names[j]}
            if pair in RIVALRIES:
                print(f"Rivalry note: {names[i]} and {names[j]} are historic "
                      "rivals - you may feel some tension supporting both!\n")


def compare_clubs(club_a, club_b):
    fields = [
        ("League", "league"),
        ("Founded", "founded"),
        ("City", "city"),
        ("Values", "values"),
        ("Style", "style"),
        ("Star Players", "star_players"),
        ("Honors", "honors"),
    ]
    print(f"\n{club_a['name']:<20} vs {club_b['name']}")
    print("-" * 55)
    for label, key in fields:
        print(f"{label:<14} {club_a[key]:<22} {club_b[key]}")
    print()


def find_club_by_name(club_data, name):
    for club in club_data:
        if club["name"].lower() == name.lower():
            return club
    return None


def save_result(username, top_clubs):
    try:
        with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            match_names = [club["name"] for club, score in top_clubs]
            writer.writerow([username, date.today().isoformat()] + match_names)
        print("Your result has been saved!\n")
    except IOError as error:
        print(f"Could not save your result: {error}")


def view_saved_results():
    try:
        with open(RESULTS_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print(f"No results file found yet ({RESULTS_FILE}).\n")
        return
    except IOError as error:
        print(f"Could not read saved results: {error}")
        return

    if not rows:
        print("No saved results yet.\n")
        return

    print("\nPast Quiz Results:")
    print("=" * 50)
    for row in rows:
        print(f"{row['username']} ({row['date']}): "
              f"{row['match_1']}, {row['match_2']}, {row['match_3']}")
    print()


def main():
    club_data = load_club_data()
    display_welcome()

    while True:
        print("Main Menu")
        print("1. Take the quiz")
        print("2. View past results")
        print("3. Compare two clubs")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("What's your name? ").strip()
            answers = run_quiz()
            scores = score_clubs(answers, club_data)
            top_clubs = get_top_matches(scores)
            display_matches(top_clubs)
            check_rivalry(top_clubs)
            save_result(username, top_clubs)
        elif choice == "2":
            view_saved_results()
        elif choice == "3":
            name_a = input("First club name: ").strip()
            name_b = input("Second club name: ").strip()
            club_a = find_club_by_name(club_data, name_a)
            club_b = find_club_by_name(club_data, name_b)
            if club_a and club_b:
                compare_clubs(club_a, club_b)
            else:
                print("One or both club names weren't found. Check the spelling and try again.\n")
        elif choice == "4":
            print("Thanks for using Pitch Match. Goodbye!")
            break
        else:
            print("That's not a valid option. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()