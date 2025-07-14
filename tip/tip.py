def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = d.replace("$", "") # replaces the dollar sign with an empty space
    return float(dollars)


def percent_to_float(p):
    percent = p.replace("%", "") # repalces percentage sign with empty space
    return float(percent) / 100  # /100 convert the percentage into a decimal

main()
