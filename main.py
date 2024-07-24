import random

# define global variables
MAX_LINES = 3      
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    '🍒': 2,
    '🍋': 4, 
    '🍊': 6,
    '🍉': 8
}

symbol_multiplier = {
    '🍒': 5,
    '🍋': 4, 
    '🍊': 3,
    '🍉': 2
}



def get_slot_machine_spin():
    # creating a list containing all symbols with their occurrences
    all_symbols = []
    for symbol, scount in symbol_count.items():
        for _ in range(scount):
            all_symbols.append(symbol)

    # creating a list of lists where each list is a column
    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]      # creting a copy of the list
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns



def print_slot_machine(columns):
    # print the transpose of the "matrix"
    for row in columns:
        for i in range(len(row)):
            if i != len(columns) - 1:
                print(row[i], end=' | ')
            else: 
                print(row[i], end='')
        print()



def deposit():
    while True:
        try:
            amount = int(input("The amount to deposit: $"))
            if amount <= 0:
                print("Amount must be greater than zero")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        return amount
    


def get_number_lines():
    while True:
        try:
            lines = int(input(f"Number of lines to bet on (1 - {MAX_LINES}): "))
            if lines != 1 and lines != 2 and lines != 3:
                raise ValueError
        except ValueError:
            print("Please Enter a valid number")
            continue
        return lines



def get_bet(balance):
    while True:
        try:
            bet = int(input("Bet on each line ($1 - $100): $"))
            if bet > MAX_BET:
                print(f"Maximum bet is ${MAX_BET}")
                continue
            if bet < MIN_BET:
                print(f"Minimum bet is ${MIN_BET}")
                continue
        except ValueError:
            print("Please Enter a number")
            continue
        return bet
    


def check_win(columns, lines, bet):
    win = 0
    win_lines = []
    for line in range(len(columns)):
        symbol_to_check = columns[line][0]      # get the first symbol in the col
        for col in columns:
            if symbol_to_check != col[line]:
                break
        else:
            win += symbol_multiplier[symbol_to_check] * bet
            win_lines.append(line + 1)
    return win, win_lines



def spin(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet(balance)
        tbet = bet * lines
        if tbet > balance:
            print(f"Insufficient balance for the bet!  Current balance ${balance}")
        else:
            break

    print(f"\nYou are betting ${bet} on {lines} lines.\nTotal bet = ${tbet}\n")

    slots = get_slot_machine_spin()
    print_slot_machine(slots)

    winnings, winnings_lines = check_win(slots, lines, bet)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winnings_lines)    # using the unpack operator to print the elements of the list

    return winnings - tbet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        choice = input("Press Enter to spin (q to quit)")
        if choice.lower() == 'q':
            break
        balance += spin(balance)

    print("-" * 25)
    print(f"You're left with ${balance}")
    print("-" * 25)


if __name__ == "__main__":
    main()