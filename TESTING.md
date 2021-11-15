# Testing

## Generic Testing - PEP8 Validation
I have used the PEP8 Python code validation service to test the entire program code and resolved all errors & addressed all recommendations. The confirmation output has passed without any errors, notifications or warnings as shown in screenshot below:

![PEP8 Validation](readme/testing/pep8validation.png)

## Specific Testing - Hangman

**Welcome Screen:**
----


 Test Case | Expected Result | Actual Result | Pass/Fail
 ------------- | ------------- | ------------ | -------------
 Welcome Message Functionality | Welcome screen should load as intended, should present user with a prompt to press any key to continue, and upon pressing any key, the program should proceed to the Main Game Screen | Screen displays and functions as expected | Pass





**Main Game Screen:**
----


 Test Case | Expected Result | Actual Result | Pass/Fail
 ------------- | ------------- | ------------- | -------------
Word Selection is Random | Upon game commencement, a word should be selected at random from the list of available words programmed into the back-end | Each game load triggers a random choice of word | Pass
Answer displays with letters obscured | The Random word selected should be displayed in the answer area, with a blank underscore for each letter - visually guiding the player as to the length of the word | Word displays as expected in the answer area | Pass
Guess counters run as expected | The counters for both "Guesses remaining" and "Incorrect Guesses" should both start at their maximum and minimum values (respectively) and should increment/decrement correctly with each additional guess from the user | Both counters start at the expected values, and increment/decrement appropriately as guesses are made by the player | Pass
Gallows builds correctly | The Hangman "Gallows" graphic should start at the correct point (as an empty gallows) and should build appropriately with each incorrect guess from the User. Correct guesses and invalid guesses should not trigger a gallows-build | The gallows builds in the correct sequence as expected, and invalid guesses do not trigger a gallows-buildout | Pass
Previous guess tracking functions correctly | The previous guess tracker should update, logging each valid guess from the user, whether the letter is in the answer or not. Any invalid guesses should not trigger an addition to the previous guesses tracker | Previous guesses tracker functions as expected - valid guesses are added, and invalid guesses are not displayed | Pass

**Data Entry & Validation:**
----


 Test Case | Expected Result | Actual Result | Pass/Fail
 ------------- | ------------- | ------------- | -------------
Non-letter entry validation | A notification should display to the user the appropriate error/warning message upon entry of a non-letter for their guess, helping the user understand why their input was invalid, and what action to take next | Error message displays correctly as expected, and game re-prompts user for a valid input | Pass
Duplicate guess validation | A notification should be displayed to the user with an appropriate error/warning message upon entry of a duplicate guess, helping the user understand why their input was invalid, and what action to take next | Error message displays correctly as expected, and game re-prompts user for a valid input | Pass











