import pandas as pd
st = pd.read_csv('State_Individual_Income_Tax_Rates_Brackets_2022.csv')
import dict_of_states.py as ds

def annual_salary():
    salary = float(input("Enter your salary: "))
    salary = round(salary, 2)
    print(f"Gross income is ${salary}\n")
    print(f"Monthly gross income breakdown is ${salary / 12}\n")
    return salary

def fed_tax():
    salary = annual_salary()
    esbi = None
    while esbi not in ["1", "2", "3", "4"]:
        esbi = input("Enter your employment status: \n 1) Employee\n 2) Self Employed\n 3) Business owner\n 4) Investor \n")
    if esbi == "1":
        fed_income_tax = .37 * salary
    elif esbi == "2":
        fed_income_tax = .35 * salary
    elif esbi == "3":
        fed_income_tax = .20 * salary
    elif esbi == "4":
        fed_income_tax = .15 * salary
    else:
        print("Incorrect answer!")
    fed_income_tax = round(fed_income_tax, 2)
    print(f"Your Federal Income Tax is ${fed_income_tax}\n")
    return salary, fed_income_tax

def state_tax():
    salary, fed_income_tax = fed_tax()
    marrital_status = input("Are you single or married? ")

    state_income_tax_single = 
    state_income_tax_married = 

    state = input("Enter your state: ")
    if state == "Florida" or "florida" or "FL" or "fl":
        print(f"Your state income tax is ${state_income_tax_singe}")
        state_income_tax = 0
    
    if marrital_status is single and state is :
        state_income_tax =  salary * state_income_tax_single
    elif marrital_status is not single and state is :
        state_income_tax = salary * state_income_tax_married
    
    net_income = salary - fed_income_tax - state_income_tax
    print(f"Net income after Federal Income Tax and State Tax is ${net_income}\n")
    return net_income

def monthly_budget(net_income):
    monthly_budget = net_income / 12
    monthly_budget = round(monthly_budget, 2)
    print(f"Your monthly budget is ${monthly_budget} \n")
    return monthly_budget


def savings(monthly_budget):
    rec_savings = .10 * monthly_budget
    rec_savings = round(rec_savings, 2)
    rec_savings_one_year = rec_savings * 12
    rec_savings_one_year = round(rec_savings_one_year, 2)
    print(f"Recommended amount placed in savings each month is ${rec_savings}")
    print(f"The recommended amount saved after 1 year is ${rec_savings_one_year}\n")

def investing(monthly_budget):
    rec_investing = .20 * monthly_budget
    rec_investing = round(rec_investing, 2)
    rec_investings_one_year = rec_investing * 12
    rec_investings_one_year = round(rec_investings_one_year, 2)
    print(f"Recommended amount invested each month is ${rec_investing}")
    print(f"The recommended amount invested after 1 year is ${rec_investings_one_year}\n")

def expenses(monthly_budget):
    expenses = float(input("What are your actual expenses each month? "))
    perc_act_expenses = expenses / monthly_budget
    perc_act_expenses = round(perc_act_expenses, 2)
    print(f"Your actual expenses are {expenses} and that is {perc_act_expenses * 100}% of your monthly budget.") 
    rec_expenses = .50 * monthly_budget
    rec_expenses = round(rec_expenses, 2)
    print(f"Recommended amount spent on expenses each month is ${rec_expenses}\n")

def wants(monthly_budget):
    rec_wants = .20 * monthly_budget
    rec_wants = round(rec_wants, 2)
    print(f"Recommended amount spent for your wants each month is ${rec_wants}\n")

while True:
    net_income = state_tax()
    monthly_budget = monthly_budget(net_income)
    savings(monthly_budget)
    investing(monthly_budget)
    expenses(monthly_budget)
    wants(monthly_budget)
    start_over = None
    while start_over not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]:
        start_over = input("Would you like to start over? Y/N: ")
        if start_over != "Yes" or "yes" or "Y" or "y":
            break
