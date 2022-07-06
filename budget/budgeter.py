def budget():
    salary = int(input("Enter your salary: "))
    print(f"Gross income is ${salary}")
    print(" ")

    fed_income_tax = .20 * salary
    fed_income_tax = round(fed_income_tax, 2)
    
    net_income = salary - fed_income_tax 
    print(f"Net income after Federal Income Tax is ${net_income}")
    print(" ")

    monthly_budget = net_income / 12
    monthly_budget = round(monthly_budget, 2)

    savings = .10 * monthly_budget
    savings = round(savings, 2)
    savings_one_year = savings * 12
    savings_one_year = round(savings_one_year, 2)
    print(f"Amount placed in savings each month is ${savings}")
    print(f"The amount saved after 1 year is ${savings_one_year}")
    print(" ")

    investing = .25 * monthly_budget
    investing = round(investing, 2)
    investings_one_year = investing * 12
    investings_one_year = round(investings_one_year, 2)
    print(f"Amount invested each month is ${investing}")
    print(f"The amount invested after 1 year is ${investings_one_year}")
    print(" ")

    expenses = .60 * monthly_budget
    expenses = round(expenses, 2)
    print(f"Amount spent on expenses each month is ${expenses}")
    print(" ")

    wants = .05 * monthly_budget
    wants = round(wants, 2)
    print(f"Amount spent on wants each month is ${wants}")
    print(" ")

budget()