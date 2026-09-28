# ITNT415_CALALANG_KYLE_CalculatorMaster

## StudentName
Kyle Calalang

## Course and Section
ITNT415 — BIT41

## Project Description
CalculatorMaster is a menu-driven calculator written in Python. It was built using Git and GitHub feature branching, where each arithmetic operation was developed on its own branch, committed with descriptive messages, and merged into the main branch through a reviewed Pull Request. The final version on main combines all four operations into a single application that keeps running until the user chooses to exit.

## Branch Structure
The repository uses one main branch and four feature branches. Each feature branch has at least two commits and was merged into main through a Pull Request.

- `main`: holds the calculator skeleton and the final integrated application
- `addition_CALALANG`: adds the addition function, number validation, and menu option 1
- `subtraction_CALALANG`: adds the subtraction function and menu option 2
- `multiplication_CALALANG`: adds the multiplication function and menu option 3
- `division_CALALANG`: adds the division function, division-by-zero handling, and menu option 4

## Program Features
- Menu-driven interface with options for Addition, Subtraction, Multiplication, Division, and Exit
- Continuous execution, so the menu repeats after every calculation until Exit (option 5) is chosen
- User input validation that rejects non-numeric entries and asks the user to try again
- Invalid menu choice handling that shows an error message and returns to the menu
- Division-by-zero handling that displays "Cannot divide by zero." instead of crashing
- Proper function definitions: `get_number()`, `add()`, `subtract()`, `multiply()`, `divide()`, and `main()`

## How to Run
The program requires Python 3. Open a terminal in the project folder and run `python calculator.py`. Follow the on-screen menu by typing a number from 1 to 5, then enter the numbers when prompted.

## Sample Execution
The screenshot below shows a typical session, and the same session in words is:

- The user selects option 1 (Addition), enters 10 and 5, and the program displays Result: 15.0
- The user selects option 4 (Division), enters 10 and 0, and the program displays Error: Cannot divide by zero.
- The user selects option 5, and the program displays Exiting calculator. Goodbye!

## Commit Examples
- Initial addition function
- Improve addition validation and integrate into menu
- Add division-by-zero handling and finalize menu validation
