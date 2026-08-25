#function
def calculate_budget(income, fixed_expenses):
    remaining_budget = income - fixed_expenses
    return remaining_budget

DEFAULT_TAX_RATE = 18
def tax(income, tax_rate):
    tax_amount = income * (tax_rate / 100)
    return tax_amount


def overall_tax(income, shopping, investment, gifts, travel, other_expenses, tax_rate):
    income_tax = tax(income, tax_rate)
    shopping_tax = tax(shopping, tax_rate)
    investment_tax = tax(investment, tax_rate)
    gifts_tax = tax(gifts, tax_rate)
    travel_tax = tax(travel, tax_rate)
    other_expenses_tax = tax(other_expenses, tax_rate)
    overall_tax_amount = income_tax + shopping_tax + investment_tax + gifts_tax + travel_tax + other_expenses_tax
    return overall_tax_amount

def savings(remaining_budget, overall_tax):
    remaining_budget_after_tax = remaining_budget - overall_tax
    return remaining_budget_after_tax

def bill_spliter(total_bill, number_of_people):
    bill_per_person = total_bill / number_of_people
    return bill_per_person

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))

