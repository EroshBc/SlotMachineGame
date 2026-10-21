 #Text based slot machine
 # Allow user enter some money and then bet and select choose 1-3 lines
 #determine they won and If they won multiply by number of lines and deposit it to balance
 #let them to play till they cashout or untill run out of the money

 #function for deposit
 #ask user enter the value, check is number and value over zero
 #then add to balance

import random

NUM_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COL = 3

symbol_count = {   
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {   
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

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

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

#function to deposit money
def deposit():
    while True:
        amount = input("What would you like to depsoit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break;
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount


# Function to get number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(NUM_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= NUM_LINES:
                break
            else:
                print("Please enter a valid number of lines (1-" + str(NUM_LINES) + ").")
        else:
            print("Please enter a valid number.")
    return lines

#Function to get bit
def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return bet

def spin(balance):
    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        tot_bet = lines * bet

        if tot_bet > balance:
            print(f"You don't have enough money to place that bet. Your current balance is: ${balance}.")
        else:
            break

    print(f"You have deposited: ${balance} and are betting on {lines} lines.")
    print(f"Your total bet is: ${tot_bet}")

    slots = get_slot_machine_spin(ROWS, COL, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = get_winnings(slots, lines, bet, symbol_value)
    print(f"You won: ${winnings}")
    print(f"You won on lines : ", *winning_lines)\

    return winnings - tot_bet

def main():
    balance = deposit()

    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    

main()
