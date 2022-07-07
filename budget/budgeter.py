import State-Individual-Income-Tax-Rates-and-Brackets-for-2022-v.csv1

def salary():
    salary = int(input("Enter your salary: "))
    print(f"Gross income is ${salary}")
    print(" ")

def fed_tax():
    fed_income_tax = .20 * salary
    fed_income_tax = round(fed_income_tax, 2)

def state_tax(salary):
    state_income_tax = input("Enter your state: ")
    print(f"Your state income tax is ${}")
    net_income = salary - fed_income_tax - state_income_tax 
    print(f"Net income after Federal Income Tax and State Tax is ${net_income}")
    print(" ")

def savings():
    savings = .10 * monthly_budget
    savings = round(savings, 2)
    savings_one_year = savings * 12
    savings_one_year = round(savings_one_year, 2)
    print(f"Amount placed in savings each month is ${savings}")
    print(f"The amount saved after 1 year is ${savings_one_year}")
    print(" ")

def investing():
    investing = .25 * monthly_budget
    investing = round(investing, 2)
    investings_one_year = investing * 12
    investings_one_year = round(investings_one_year, 2)
    print(f"Amount invested each month is ${investing}")
    print(f"The amount invested after 1 year is ${investings_one_year}")
    print(" ")

def expenses():
    expenses = .60 * monthly_budget
    expenses = round(expenses, 2)
    print(f"Amount spent on expenses each month is ${expenses}")
    print(" ")

def wants():
    wants = .05 * monthly_budget
    wants = round(wants, 2)
    print(f"Amount spent on wants each month is ${wants}")
    print(" ")

def budget():
    monthly_budget = net_income / 12
    monthly_budget = round(monthly_budget, 2)
    salary()
    fed_tax()
    state_tax(salary)
    savings()
    investing()
    expenses()
    wants()

budget()
