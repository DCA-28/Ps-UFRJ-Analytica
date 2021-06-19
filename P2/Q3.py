import math

class CashMachine:
    def __init__(self):
        self.cash_notes = [100, 50, 20, 10, 5, 2]
        self.cash_coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
        self.withdraw_dict = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0,
            0.5: 0,
            0.25: 0,
            0.1: 0,
            0.05: 0,
            0.01: 0,
        }

    def withdraw(self, total_value):
        amount = total_value
        # first let's see how many notes we need for the withdraw
        for note in self.cash_notes:
            units = amount // note
            if units > 0:
                amount -= units * note
                self.withdraw_dict[note] += units
        remaining_amount = amount
        # and let's fetch the coins
        for coin in self.cash_coins:
            units = remaining_amount // coin
            if units > 0:
                remaining_amount -= units * coin
                self.withdraw_dict[coin] += units
        #verifying if the lost due the innerent limitation to represent float numbers caused some miss counted
        #value, in that case we sum 0.01 to the amount that will be withdrawn """
        if magnitude(remaining_amount) == -3:
            self.withdraw_dict[0.01] += 1
        return self.withdraw_dict

    # function to print the withdraw
    def cash_returned(self, total_value):
        print(f">> {total_value}", end="\n\n")
        print("NOTAS:")
        for note in self.cash_notes:
            notes_quantity = int(self.withdraw_dict[note])
            print(f"{notes_quantity} nota(s) de R$ {note:.2f}")
        print("\nMOEDAS:")
        for coin in self.cash_coins:
            print(f"{self.withdraw_dict[coin]:.0f} moeda(s) de R$ {coin:.2f}")

# calculates a number's order of magnitude
def magnitude(number):
    return math.floor(math.log(number, 10))

def main():
    value = float(input())
    cash_machine = CashMachine()
    cash_machine.withdraw(value)
    cash_machine.cash_returned(value)

main()
