import random
import sys
import time

SPIN_SPEED = 0.05      - seconds per animation frame
BASE_SPINS = 12        - how long the first reel spins
EXTRA_SPINS = 4        - each next reel spins this much longer


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
    """Turn 15.0 into '15' and trim long decimals so the reels stay readable."""
    value = round(value, 6)
    if value == int(value):
        return str(int(value))
    return str(value)


def draw_reels(display):
    reels = "".join(f"[{ch}]" for ch in display)
    sys.stdout.write(f"\r  >> {reels} <<  ")
    sys.stdout.flush()


def slot_reveal(text):
    """Spin every digit reel, then lock them in one by one from left to right."""
    display = list(text)
    locked = [not ch.isdigit() for ch in text]   # '.', '-' are fixed symbols

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


def main():
    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            show_result(add(a, b))
        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            show_result(subtract(a, b))
        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            show_result(multiply(a, b))
        elif choice == "4":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            try:
                show_result(divide(a, b))
            except ZeroDivisionError as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()