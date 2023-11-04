
import random
random1 = random.randint(1, 100)
print(random1)
tries = 1
while tries <= 5:

    if tries == 1:
        guess = int(input(f"Try {tries}: Enter a number between 1 and 100 (or -1 to end): "))
        tries+=1

    else:
        guess = int(input(f"Try {tries}: Guess again, enter a number between 1 and 100 (or -1 to end): "))
        tries += 1

    if guess == -1:
        print("Bye-bye!")
        break
             
    if guess > random1:
         print(guess, "is too high.")
         
    elif guess < random1:
         print(guess, "is too low.")
        
    else:
        print("Bingo, you've got it right!")
        print("\nBye-bye!")
        break

    if tries == 6 and guess != random1:
        print("Game over")
        break

    
              
 
              
