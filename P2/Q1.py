# Solution of the first question, group P2
#todo: comment and test again

def average_value() -> float:
    integer_values = []
    while True:
        try:
            entry = input()
            integer = int(entry)
            integer_values.append(integer)
        except ValueError:
            if entry == "f":
                break
            else:
                print("Please, enter a integer or the " "f" " character:")
    print("")
    try:
        total_sum = sum(integer_values)
        average = total_sum / len(integer_values)
        print("With the numbers:")
        for number in integer_values:
            print(f">>{number}")
        print(f"The average value is: {average:.2f}")
    except ZeroDivisionError:
        print("No numbers were inserted, couldn't calculate an average value.")


def main():
    average_value()


if __name__ == "__main__":
    main()
