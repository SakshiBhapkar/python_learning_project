import budget_utility
income=int(input("Enter your monthly income: "))
fixed_expenses=int(input("Enter your monthly fixed expenses(rent,grocery etc.): "))
shopping=int(input("Shopping: "))
investment=int(input("Investment: "))
gifts=int(input("Gifts: "))
travel=int(input("Travel: "))
other_expenses=int(input("Other Expenses: "))
total_expenses = shopping + investment + gifts + travel + other_expenses+fixed_expenses
'''total expensees tell about total money spent in a month'''
print("Your total expenses are: ", total_expenses)
remaining_budget= budget_utility.calculate_budget(income, total_expenses)
'''remaining budget tell about how much money is left after spending in a month'''
print("Your remaining budget is: ", remaining_budget)


print("\nNow lets calculate your tax")
tax_rate=int(input("Enter your tax rate: "))
income_tax=tax_amount = budget_utility.tax(income, tax_rate)
shopping_tax=budget_utility.tax(shopping, tax_rate)
investment_tax=budget_utility.tax(investment, tax_rate)
gifts_tax=budget_utility.tax(gifts, tax_rate)
travel_tax=budget_utility.tax(travel, tax_rate)
other_expenses_tax=budget_utility.tax(other_expenses, tax_rate)
print("Your income tax is: ", income_tax)
print("Your tax amount on shopping is: ", shopping_tax)
print("Your tax amount on investment is: ", investment_tax)
print("Your tax amount on gifts is: ", gifts_tax)
print("Your tax amount on travel is: ", travel_tax)
print("Your tax amount on other expenses is: ", other_expenses_tax) 

overall_tax = budget_utility.overall_tax(income, shopping, investment, gifts, travel, other_expenses, tax_rate)
'''overall tax tell about total tax amount on all expenses in a month'''
print("Your overall tax amount is: ", overall_tax)

print("\nNow lets calculate your budget after tax")
remaining_budget_after_tax = budget_utility.savings(remaining_budget, overall_tax)
'''this money left at the end of month'''
print("Your savings after tax is: ", remaining_budget_after_tax)

'''Now lets calculate your bill per person if you want to split your bill with your friends'''
print("\nNow lets calculate your bill per person if you want to split your bill with your friends")
total_bill = float(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people to split the bill with: "))
bill_per_person = budget_utility.bill_spliter(total_bill, number_of_people)
print("Each person should pay: ", bill_per_person)

'''digital root'''
print("\nNow lets calculate the digital root of a number")
n = int(input("Enter a number to calculate its digital root: "))
digital_root_result = budget_utility.digital_root(n)
print("The digital root of", n, "is:", digital_root_result)

'''Now lets calculate the discounted amount on a given amount and rate'''
print("\nNow lets calculate the discounted amount on a given amount and rate")
discount = lambda amount, rate: amount * rate / 100
print("The discounted amount is: ", discount(float(input("Enter the amount: ")), float(input("Enter the discount rate: "))))

from rich.console import Console
from rich.table import Table

console = Console()

console.print("[bold cyan]💰 BUDGET PLANNER (Summary)[/bold cyan]")

table = Table(title="Monthly Budget")

table.add_column("Item")
table.add_column("Amount")

table.add_row("Monthly Budget", f"₹{income}")
table.add_row("Fixed Expenses", f"₹{fixed_expenses}")
table.add_row("Shopping", f"₹{shopping}")
table.add_row("Investment", f"₹{investment}")
table.add_row("Gifts", f"₹{gifts}")
table.add_row("Travel", f"₹{travel}")
table.add_row("Other Expenses", f"₹{other_expenses}")
table.add_row("Savings", f"₹{remaining_budget_after_tax}")
table.add_row("Total Expenses", f"₹{total_expenses}")
table.add_row("Total Spend", f"₹{income - remaining_budget_after_tax}")

console.print(table)