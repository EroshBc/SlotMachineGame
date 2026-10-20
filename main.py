 #Text based slot machine
 # Allow user enter some money and then bet and select choose 1-3 lines
 #determine they won and If they won multiply by number of lines and deposit it to balance
 #let them to play till they cashout or untill run out of the money

 #function for deposit
 #ask user enter the value, check is number and value over zero
 #then add to balance

NUM_LINES = 3
MAX_BET = 100
MIN_BET = 1

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


def main():
    balance = deposit()
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


main()
