# AI Improvement Record

## Original Development

Explain how you developed the original version and describe any AI assistance used before the first required commit. AI use during this stage should be minimal.

The original version of Pitch Match, including the quiz, scoring, and top-3 matching, was developed by referring back to my previous coursework and W3Schools. 
I used AI, specifically Claude, in a minimal way during this stage. AI explained Python concepts I needed, such as how csv.DictReader() works. 
I wrote every line of code myself and tested it before committing it as my original working version.

## AI Tools Used

List each AI tool used while improving the application.

1. Error handling: The original version assumed `clubs.csv` and `results.csv` would always be present. AI helped add try/except handling so a missing or malformed `clubs.csv` prints a clear message and exits cleanly instead of crashing, and a missing `results.csv` is treated as "no results yet" instead of an error.
2. Documentation: AI expanded comments explaining what each function does and why. For example, explaining why `RIVALRIES` is stored as a list of sets.
3. Optional features from the proposal: My proposal listed two optional improvements that weren't part of the required baseline: a club-comparison view and a rivalry warning. 
AI helped implement both:
   - `compare_clubs()` prints two clubs side by side across their attributes, added as menu option 3.
   - `check_rivalry()` checks the user's top 3 matches against a list of known rival pairs and prints a warning if two of the top matches are rivals.

## Improvements Requested

Describe the important prompts or requests you gave the AI. Do not paste a complete chat transcript.

After I had a working baseline that included the quiz, scoring, top-3 matching, and the ability to save and view results, I asked AI to help with several improvements. 
I wanted error handling added so the application wouldn't crash if 'clubs.csv' or 'results.csv' was missing or malformed. 
I also wanted docstrings and comments added to explain what each function does. 
I asked AI to help implement two optional features from my proposal, a club comparison view and a rivalry warning between the users top-3 matches. 
 Finally, I asked AI to help design test scenarios that would confirm the app fails normally instead of crashing.


## Changes Accepted

For each major accepted change, explain what changed, why you accepted it, and how you verified that you understood it.

I accepted the try/except error handling in load_club_data() and view_saved_results() because I tested it myself. 
I renamed clubs.csv and deleted results.csv, then confirmed the app showed a clear message instead of crashing. 
I accepted the compare_clubs() and check_rivalry() functions because I ran them with real inputs, such as comparing Real Madrid and FC Barcelona and answering the quiz so that two rivals landed in my top 3. 
The output matched what I expected in both cases. I understood both functions because I could trace through exactly which club attributes they were reading and comparing.

## Changes Rejected or Revised

Describe any AI suggestion you rejected or modified and explain why.

I rejected the term "workhorses" for one of my players_type categories after I flagged it as racially-coded or insensitive language, and I replaced it with "gritty" instead. 
This kept the same meaning without the loaded connotation.
I also decided to keep my city quiz question as an additional fourth question rather than replacing my players_type question, since I wanted to preserve the dataset I had already built and tested rather than redo it.


## What I Learned

Explain what you learned by reviewing and applying the AI-assisted improvements.

In moving through this process one step at a time before the final push taught me several things. 
I learned why file and function ordering matters in Python, since a function must be defined before it is called, and this caused one of my early errors. 
I learned how csv.DictReader() turns rows into dictionaries automatically. I also learned how to use try/except to catch specific error types, such as FileNotFoundError and ValueError, instead of letting the whole program crash. 
This process reaffirmed for me why testing edge cases like bad input and missing files matters just as much as testing the normal flow of the program. 
I also learned how to commit and push code to GitHub, including how to fix a mistyped commit message before it went out. 
I now understand the jokes about engineers pushing finicky code!
