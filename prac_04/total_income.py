"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def calculate_cumulative_income():
    # Ask the user for the number of months to enter incomes for
    num_months = int(input("How many months? "))

    # Create an empty list to store the monthly incomes
    incomes = []

    # Loop to get the income for each month
    for month in range(1, num_months + 1):
        # Get the income input from the user
        income = float(input(f"Enter income for month {month}: "))
        # Add the income to the list
        incomes.append(income)

    # Print the income report
    print("\nIncome Report")
    print("-------------")

    # Initialize the cumulative total and the month counter
    cumulative_total = 0
    month_counter = 1

    # Loop through the incomes to display them with cumulative totals
    for income in incomes:
        # Update the cumulative total by adding the current income
        cumulative_total += income
        # Print the income for the current month and the cumulative total
        print(f"Month {month_counter} - Income: $    {income:.2f:>6} Total: $    {cumulative_total:.2f:>6}")
        # Increment the month counter
        month_counter += 1


# Call the function to start the program
calculate_cumulative_income()
