# EXPENSE TRACKER APP
expenseList = []

while True:
    print("===MENU===")
    print("1.Add Expenses")
    print("2.View all Expenses")
    print("3.View total Spendings")
    print("4.Exit")

    choice = int(input("Enter any option(1-4):"))

# 1.ADD EXPENSES
    if (choice == 1):
        date = input("Enter the date:")
        category = input("Enter the category(food,travel,shopping,makeup):")
        description = input("Description(add more details):")
        amount = float(input("Enter the amount:"))

        expenses = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseList.append(expenses)
        print("\n DONE.Expenses added successfully!")


# 2.VIEW ALL EXPENSES
    elif (choice == 2):
        if (len(expenseList) == 0):
            print("No Expenses Added")
        else:
            print("===THESE ARE YOUR EXPENSES===")
            count = 1
            for eachExpense in expenseList:
                print(f"expense number {count} -> {eachExpense["date"]},{eachExpense["category"]},{eachExpense["description"]},{eachExpense["amount"]}")
                count += 1

# 3.VIEW TOTAL SPENDINGS
    elif (choice == 3):
        total = 0
        for eachExpense in expenseList:
            total = total+eachExpense["amount"]

        print("\nYOUR TOTAL SPENDINGS = ",total)

# 4.EXIT
    elif (choice == 4):
        print("THANK YOU")
        break

    else:
        print("INVALID CHOICE.TRY AGAIN")