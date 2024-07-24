def main():
    # Get the inputs
    owed_cents = int(input("Cents: "))

    # Calculate the quaters
    quaters = calc_quaters(owed_cents)
    cents = owed_cents - quaters * 25

    # Calculate the number of dimensions to return to customer
    dimes = calc_dimensions(owed_cents)
    cents = owed_cents - dimes * 10

    # Calculate the nickles to return
    nickles = calc_nickles(owed_cents)
    cents = owed_cents - nickles * 5

    # Calculate the pennies to return 
    pennies = calc_pennies(owed_cents)

    # Sum of coins
    coins = quaters + nickles + dimes + pennies

    print(coins)

# Function for calculate quaters
def calc_quaters(cents):
    return cents / 25

# Function for calculate dimentions
def calc_dimensions(cents):
    return cents / 10

# Function for calculate nickles
def calc_nickles(cents):
    return cents / 5

def calc_pennies(cents):
    return cents

if __name__ == "__main__":
    main()
