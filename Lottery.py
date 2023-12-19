import random

def lottery_draw():
    # Function to generate 6 random numbers between 1 and 49
    return random.sample(range(1, 50), 6)

def create_lottery_ticket():
    # Function to allow the user to create a lottery ticket with 6 different numbers between 1 and 49
    ticket = []
    while len(ticket) < 6:
        number = int(input("Please enter a number between 1 and 49: "))
        if 1 <= number <= 49 and number not in ticket:
            ticket.append(number)
        else:
            print("Invalid input. Please try again.")
    return ticket

def lottery_game():
    # Function to perform the lottery game
    print("Welcome to the Numerical Lottery game.")
    
    # User creates their ticket
    user_numbers = create_lottery_ticket()
    print(f"User's ticket: {user_numbers}")
    
    # Computer draws the lottery
    computer_numbers = lottery_draw()
    
    # Check matching numbers
    matching_numbers = set(computer_numbers) & set(user_numbers)
    
    # Print the results
    print(f"\nComputer's draw: {computer_numbers}")
    print(f"User's ticket: {user_numbers}")
    print(f"Matching numbers: {matching_numbers}")
    
    if len(matching_numbers) == 6:
        print("Congratulations! You've won the jackpot by matching all numbers.")
    elif len(matching_numbers) > 0:
        print(f"Congratulations! You've won a prize by matching {len(matching_numbers)} numbers.")
    else:
        print("Sorry, you didn't win this time. Try again for better luck next time!")

# Start the lottery game
lottery_game()
