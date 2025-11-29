print(r"""

   ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 

""")
import random
ask_level = input("Welcome to the Number Guessing Game! \n "
                  "I'm thinking of a number between 1 and 100.\n"
                  "Choose a difficulty. Type 'easy' or 'hard':").lower()
if ask_level == "easy":
    attempts = 10
elif ask_level == "hard":
    attempts = 5
else:
    print("Invalid choice, easy mode selected.")

random_number = random.randint(1, 100)

while attempts > 0:
    guess = int(input(f"You have {attempts} attempts remaining to guess the number.\n"
                      f"Male a guess : "))
    if guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        break
    elif guess < random_number:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1
    if attempts ==0:
        print(f"You've run out of guesses. Refresh the page to run again.\n"
              f"The secret number was {random_number}.")

print("Thank you for playing!")