import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Print an empty line for spacing
        guess = int(input("Enter a new guess: "))
    
    print("Congrats! The number was: " + str(secret_number))

# Required line to run the main function
if __name__ == '__main__':
    main()
