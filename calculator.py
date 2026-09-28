import random
import sys
import time

SPIN_SPEED = 0.05
BASE_SPINS = 12
EXTRA_SPINS = 4


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def format_result(value):
    value = round(value, 6)
    if value == int(value):
        return str(int(value))
    return str(value)


def draw_reels(display):
    reels = "".join(f"[{ch}]" for ch in display)
    sys.stdout.write(f"\r  >> {reels} <<  ")
    sys.stdout.flush()


def slot_reveal(text):
    display = list(text)
    locked = [not ch.isdigit() for ch in text]

    for i, ch in enumerate(text):
        if locked[i]:
            continue
        for _ in range(BASE_SPINS + i * EXTRA_SPINS):
            for j in range(len(text)):
                if not locked[j]:
                    display[j] = random.choice("0123456789")
            draw_reels(display)
            time.sleep(SPIN_SPEED)
        display[i] = ch
        locked[i] = True
        draw_reels(display)
    print()


def show_result(value):
    text = format_result(value)
    print("\nSpinning the reels...")
    slot_reveal(text)
    digits = [c for c in text if c.isdigit()]
    if len(digits) >= 2 and len(set(digits)) == 1:
        print("*** JACKPOT! All reels match! ***")
    print(f"Result: {text}")


def ask_continue(name, current):
    while True:
        print("\nWhat would you like to do next?")
        print(f"1. Continue {name} (starting from {format_result(current)})")
        print("2. Back to main menu")
        choice = input("Enter your choice (1-2): ").strip()
        if choice == "1":
            return True
        if choice == "2":
            return False
        print("Invalid choice. Please select 1 or 2.")


def run_operation(name, func):
    a = get_number("Enter first number: ")
    prompt = "Enter second number: "

    while True:
        b = get_number(prompt)
        try:
            result = func(a, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        else:
            show_result(result)
            a = result

        if not ask_continue(name, a):
            return
        prompt = "Enter next number: "


def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice in operations:
            name, func = operations[choice]
            run_operation(name, func)
        elif choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()