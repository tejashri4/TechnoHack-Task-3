import random

def number_guessing_game():
  
  lower_bound = 1
  upper_bound = 100
  secret_number = random.randint(lower_bound, upper_bound)
  attempts = 0

  print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

  while True:
    try:
      guess = int(input("Take a guess: "))
      attempts += 1

      if guess < secret_number:
        print("Too low!")
      elif guess > secret_number:
        print("Too high!")
      else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  number_guessing_game()
