
# Expense Tracker
count = 0
total_expenses = 0
small_expenses = 0
medium_expenses = 0
large_expenses = 0
smallest = None
largest = None

# Have user enter expenses

user_enter_expense = float(input("Enter an expense: or 0 to finish: $"))


# make an if else statement asking if expense is less than 25, 25 - 100, or greater than 100


while user_enter_expense != 0:
    if user_enter_expense < 0:
        print("Expenses can't be negative. Try again")
    else: 
        if user_enter_expense < 25:
            print("Small Expense")
            small_expenses += 1
        elif 25 <= user_enter_expense <= 100:
            print("Medium Expense")
            medium_expenses += 1
        else:
            print("Large Expense")
            large_expenses += 1

        
        if smallest is None or user_enter_expense < smallest:
            smallest = user_enter_expense
        if largest is None or user_enter_expense > largest:
            largest = user_enter_expense

        total_expenses += user_enter_expense
        count += 1

    user_enter_expense = float(input("Enter an expense: or 0 to finish: $"))


#Expense Summary
print("---------------")
print("Expense Summary")
print("---------------")

print(f"Number of expenses: {count}")

print(f"Total expenses: ${total_expenses:.2f}")

# print average, smallest, and largest expenses
if count > 0:
    print(f"Average expense: ${total_expenses / count:.2f}")
    print(f"Smallest expense: ${smallest:.2f}")
    print(f"Largest expense: ${largest:.2f}")

# print number of small, medium, and large expenses
print(f"Small expenses: {small_expenses}")
print(f"Medium expenses: {medium_expenses}")
print(f"Large expenses: {large_expenses}")