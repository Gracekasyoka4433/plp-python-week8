
import random

# Store tasks entered by the user
tasks = []

# Display a welcoming message
print("===================================")
print(" Welcome to My Personal Mini-Toolkit!")
print("===================================")


# TOOL 1: Simple Calculator
# This tool performs basic mathematical calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The answer is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The answer is: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is: {result}")
            else:
                print("Sorry, you cannot divide by zero!")

        else:
            print("Invalid operation. Please try again.")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: To-Do List
# This tool allows users to add, view and remove tasks.
def todo_list():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your new task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty!")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select 1-4.")


# TOOL 3: Number Guessing Game
# This tool challenges users to guess a random number.
def guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 10.")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed correctly!")
                print(f"You needed {attempts} attempts.")
                break

            elif guess < secret_number:
                print("Too low! Try again.")

            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a valid whole number.")


# MAIN MENU
# This loop keeps the toolkit running until the user quits.
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye. Have a wonderful day!")
        break

    else:
        print("Sorry, that is not a valid choice. Please try again.")
