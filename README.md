* Name:TEJASHRI SOMNATH MANDLIK.
* Company:TechnoHacks Solutions Pvt.Ltd.
* Domain:Python Development Programming.
* Duration:1 month.
* Mentor:Sandip Gawali.

# Overview of the Project
# Project: Develop a Number Guessing Game

**Project Goal:**

* To create an interactive game where the user attempts to guess a randomly generated number within a specified range.

**Key Features:**

* **Random Number Generation:** Utilizes Python's `random` library to generate a secret number within a defined range (e.g., 1 to 100).
* **User Input:** Prompts the user to enter their guess through the console.
* **Feedback Mechanism:** Provides informative feedback to the user after each guess:
    * "Too low!" if the guess is below the secret number.
    * "Too high!" if the guess is above the secret number.
* **Multiple Attempts:** Allows the user to continue guessing until they correctly identify the secret number.
* **Win Condition:** Congratulates the user upon a successful guess, displaying the number of attempts taken.

**Basic Implementation:**

1. **Import the `random` library:** This line imports the necessary library to generate random numbers.
2. **Generate a random number:** A random integer within the specified range is generated using `random.randint()`.
3. **User input and feedback loop:**
   - The game enters a loop where the user is repeatedly prompted for their guess.
   - The user's input is validated and converted to an integer.
   - The guess is compared to the secret number, and appropriate feedback is provided.
4. **Win condition:** 
   - When the user guesses correctly, the loop breaks.
   - A congratulatory message is displayed, along with the number of attempts.

**Potential Enhancements:**

* **Difficulty levels:** Allow the user to choose a difficulty level (e.g., easy, medium, hard) which adjusts the range of numbers.
* **Limited attempts:** Set a maximum number of attempts for the user.
* **Hints:** Provide hints to the user, such as revealing the first or last digit of the secret number.
* **Graphical User Interface (GUI):** Create a more visually appealing and interactive game using libraries like Tkinter or PyQt.
* **Scoring system:** Award points based on the number of attempts or the difficulty level.

This project provides a foundation for learning basic game development concepts in Python, such as:

* **Input/Output:** Handling user input and providing output to the console.
* **Control flow:** Using loops and conditional statements to control the game's logic.
* **Randomness:** Utilizing the `random` library to introduce an element of chance.
* **Error handling:** Handling potential input errors (e.g., invalid input).


