import datetime
expenses = []
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            try:
                description, amount, category, date = line.strip().split(" - ")
                date = datetime.datetime.strptime(
                    date, "%Y-%m-%d %H:%M:%S.%f"
                )
                expenses.append((float(amount), description, category, date))

            except ValueError:
                print("Skipping invalid expense record.")
            except Exception as e:
                print(f"An error occurred while processing the line: {e}")

except FileNotFoundError:
    open("expenses.txt", "w").close()


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Update Expense")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    

    if choice == "1":
        # Add expense
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        description = input("Enter the expense description: ")
        category = input("Enter the expense category: ")
        date = datetime.datetime.now()
        expenses.append((amount, description, category, date))
        with open("expenses.txt", "a") as file:
            file.write(f"{description} - {amount} - {category} - {date}\n")
            


    elif choice == "2":
        # View expenses
        if not expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for amount, description, category, date in expenses:
                print(f"  {description}: ${amount:.2f} - {category} - {date}")

    elif choice == "3":
        # Calculate total
        total = sum(amount for amount, _, _, _ in expenses)
        print(f"Total Expenses: ${total:.2f}")
    elif choice == "4":
        # View category summary
        category_totals = {}

        for amount, description, category, date in expenses:
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        if not category_totals:
            print("No expenses recorded.")
        else:
            print("\n===== CATEGORY SUMMARY =====")
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")    
    elif choice == "5":
        # Delete expense
        if not expenses:
            print("No expenses to delete.")
        else:
            print("\n===== EXPENSES =====")

            for i, (amount, description, category, date) in enumerate(expenses, start=1):
                print(f"{i}. {description}: ${amount:.2f} - {category}")

            try:
                number = int(input("Enter the expense number to delete: "))

                if number < 1 or number > len(expenses):
                    print("Invalid expense number.")
                    continue
                deleted = expenses.pop(number - 1)
                print(f"Deleted: {deleted[1]}")
                with open("expenses.txt", "w") as file:
                    for amount, description, category, date in expenses:
                        file.write(f"{description} - {amount} - {category} - {date}\n")

            except ValueError:
                print("Please enter a valid number.")
    elif choice == "6":
        if not expenses:
            print("No expenses to update.")
        else:
            print("\n===== EXPENSES =====")

            for i, (amount, description, category, date) in enumerate(expenses, start=1):
                print(f"{i}. {description}: ${amount:.2f} - {category}")

            try:
                number = int(input("Enter the expense number to update: "))

                if number < 1 or number > len(expenses):
                    print("Invalid expense number.")
                    continue

                

                index = number - 1

                amount = float(input("Enter new amount: "))

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                description = input("Enter new description: ")
                category = input("Enter new category: ")

                old_date = expenses[index][3]

                expenses[index] = (amount, description, category, old_date)

                with open("expenses.txt", "w") as file:
                    for amount, description, category, date in expenses:
                        file.write(f"{description} - {amount} - {category} - {date}\n")

                print("Expense updated successfully!")

            except ValueError:
                print("Please enter valid values.")            

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
    