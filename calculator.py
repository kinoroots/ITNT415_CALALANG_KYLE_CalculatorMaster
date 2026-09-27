def main():
    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Operation not implemented yet.")

if __name__ == "__main__":
    main()

    def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def add(a, b):
    return a + b

    