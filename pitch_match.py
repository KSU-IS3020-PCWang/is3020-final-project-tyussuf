import csv
from datetime import date

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
    with open("data/clubs.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clubs.append(row)
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
    else:
        raise ValueError("That is not one of the listed options.")


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


def save_result(username, top_clubs):
    try:
        with open("data/results.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            match_names = [club["name"] for club, score in top_clubs]
            writer.writerow([username, date.today().isoformat()] + match_names)
        print("Your result has been saved!\n")
    except IOError as error:
        print(f"Could not save your result: {error}")


def view_saved_results():
    try:
        with open("data/results.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print("No results file found yet.\n")
        return
    if not rows:
        print("No saved results yet.\n")
        return
    print("\nPast Quiz Results:")
    print("=" * 50)
    for row in rows:
        print(f"{row['username']} ({row['date']}): {row['match_1']}, {row['match_2']}, {row['match_3']}")
    print()


def main():
    club_data = load_club_data()
    display_welcome()

    while True:
        print("Main Menu")
        print("1. Take the quiz")
        print("2. View past results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("What's your name? ").strip()
            answers = run_quiz()
            scores = score_clubs(answers, club_data)
            top_clubs = get_top_matches(scores)
            display_matches(top_clubs)
            save_result(username, top_clubs)
        elif choice == "2":
            view_saved_results()
        elif choice == "3":
            print("Thanks for using Pitch Match. Goodbye!")
            break
        else:
            print("That's not a valid option. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()