import random

MAX_LINES = 3  # Global constant
MIN_BET = 1  # Amounts are in $
MAX_BET = 100

HORIZONTAL_REEL = 3  # Horizontal reel
VERTICAL_REEL = 3  # Vertical reel

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 2 
} 

def play_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns 

def print_professional_slot_machine(columns):
    rows = len(columns[0])
    border = '+---' * len(columns) + '+'

    for row in range(rows):
        if row == 1:  # Middle row with a box
            print(border)
            for col in columns:
                print(f'| {col[row]} ', end='')
            print('|')
            print(border)
        else:
            for col in columns:
                print(f'  {col[row]}  ', end='')
            print()

def deposit():
    while True:
        amount = input(f"What will be the amount that you would like to deposit? (${MIN_BET}-${MAX_BET})") 
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

def get_no_of_lines():
    while True:
        lines = input("Please enter the number of lines you would like to bet on (1-" + str(MAX_LINES) +") ?") 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

def get_bet():
    while True:
        amount = input("Please enter the amount you would like to bet on each line? ") 
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

def main():
    balance = deposit()

    while True:  # Main game loop
        lines = get_no_of_lines()
        
        while True:
            bet = get_bet()
            total_bet_amount = lines * bet

            if total_bet_amount > balance:
                print(f"You do not have enough balance to bet that amount; Your current balance is: ${balance}.")
            else:
                break

        print(f"You are betting ${bet} on {lines} lines. Your total bet amount is {total_bet_amount}.")

        # Simulate slot machine play
        columns = play_slot_machine(VERTICAL_REEL, HORIZONTAL_REEL, symbol_count)
        print_professional_slot_machine(columns)

        # Example win/lose logic
        if random.choice(['win', 'lose']) == 'win':
            winnings = total_bet_amount * 2
            balance += winnings
            print(f"Congratulations! You won ${winnings}. Your new balance is ${balance}.")
        else:
            balance -= total_bet_amount
            print(f"Sorry, you lost this round. Your new balance is ${balance}.")

        # Check if the player has enough balance to continue
        if balance < MIN_BET:
            print("You don't have enough balance to continue playing. Game over.")
            break

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Your final balance is ${balance}.")
            break

main()
