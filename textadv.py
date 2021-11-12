# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from time import sleep
import sys
from os import system, name

# Credits: As per readme credits section - this clear terminal function
# is taken from the methods used by geeksforgeeks.org - see full details
# and links in credits section of readme
def clear():
    """
    Clears the terminal for formatting purposes
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def emoji_assignment(delta):
    """
    Assigns emoji to dashboard categories based on stakeholder sentiment score
    """
    if delta >= 2:
        emoji = "😀"
    elif delta == 1:
        emoji = "🙂"
    elif delta == 0:
        emoji = "😐"
    elif delta == -1:
        emoji = "🙁"
    elif delta <= -2:
        emoji = "😠"

    return emoji


def formatting_plug(a,b):
    """
    Plug spaces to visually align dashboard segregation on terminal display depending on length of variables
    """
    plug = (14 - (len(str(a)) + len(str(b)))) * " "
    return plug


def final_score(a,b,c):
    """
    Calculates player's total score upon conclusion of the final answer
    """
    total_points = a + b + c
    return total_points

def main_menu():
    """
    Displays main menu screen upon game load
    """
    print("\n----------------------------------------------------------------------")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                   W E L C O M E                                    |")
    print("|                                                                    |")
    print("|                       T O                                          |")
    print("|                                                                    |")
    print("|                         P Y T H O N                                |")
    print("|                                                                    |")
    print("|                            T E X T                                 |")
    print("|                                                                    |")
    print("|                               A D V E N T U R E                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                     [ PRESS ENTER TO BEGIN ]                       |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("----------------------------------------------------------------------")
    input()
    clear()


# Credits: This function was sourced from the article below and adapted for my project needs:
# Credits: https://www.codegrepper.com/code-examples/python/typewriter+effect+python+terminal
def typewriter(text, delay):
    """
    Function for presenting text with a delayed/typewriter effect to add to game UX
    """
    for letter in text:
        sleep(delay) 
        sys.stdout.write(letter)
        sys.stdout.flush()


revenue = 1000000
revenue_delta = "     "
expenses = 700000
expense_delta = "     "
profits = revenue - expenses
profit_delta = "     "
shareholders = "Shareholders:      😐"
shareholder_delta = "  "
customers = "Customers:         😐"
customer_delta = "  "
employees = "Employees:         😐"
employee_delta = "  "

dashboard_0 = f"\n------------------------------------------------------------\n\
Financial Projections:         |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue} {revenue_delta}      |      {shareholders} {shareholder_delta}    \n\
Expenses:  €{expenses} {expense_delta}       |      {customers} {customer_delta}    \n\
Profits:   €{profits} {profit_delta}       |      {employees} {employee_delta}    \n\
------------------------------------------------------------\n"

intro = f"- The Year is 2021...\n- FictionalCorp have hired you as their new CEO\
\n- You have been tasked with improving their performance on three fronts:\n\
    \n1. Shareholder Sentiment\
    \n2. Customer Confidence\
    \n3. Employee Engagement\n\
    \n- You will receive one point for each improvement in stakeholder status\
    \n- You will lose one point for each decline in stakeholder status\n\
    \n- Navigate the following series of business decisions, and their respective\
    \nstakeholder impacts\n\
    \n- Your performance will be displayed on a dashboard in the format below:\n" 

main_menu()
typewriter(intro, 0.015)
typewriter(dashboard_0, 0.01)
input("\n[Press Enter To Begin]")


def question_1(revenue, revenue_delta, expenses, expense_delta, profits, profit_delta, shareholders, shareholder_delta, customers, customer_delta, employees, employee_delta, dashboard_0):
    
    clear()
    typewriter(dashboard_0, 0.003)
    scenario_1 = "\nScenario 1: You must decide at what level the selling price for \n\
FictonalCorp's leading product should be set for the coming year:\n\
\nA. Increase Current Selling Price\n\
B. Maintain Current Selling Price \n\
C. Reduce Current Selling Price\n"
    typewriter(scenario_1, 0.015)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_1_answer_1 = "\nYou have chosen Option A\n \n- Increasing Selling Prices by ~5% has resulted in a decrease in projected\n\
units sold, with customers choosing competitor alternatives\n\
- Unfortunately overall Revenue projections have declined\n\
- With expenses unchanged, profit projections have fallen as a result\n"
    scenario_1_answer_2 = "\nYou have chosen Option B\n \n- Maintaining Current Selling Prices has resulted in no change to projected\n\
units sold\n\
- Overall Revenue projections are unchanged\n\
- With expenses flat, profit projections have remained static as a result\n"
    scenario_1_answer_3 = "\nYou have chosen Option C\n \n- Reducing Selling Prices by ~5% has resulted in an increase in projected\n\
units sold, with several new customers interested\n\
- Overall Revenue projections have increased as a result\n\
- With expenses unchanged, profit projections have increased\n"
    
    if input1 == "A":        
        revenue_delta1 = -50000
        revenue1 = revenue + revenue_delta1
        expense_delta1 = 0
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses 
        profit_delta1 = revenue_delta1 - expense_delta1
        profits1 = revenue1 - expenses1        
        shareholder_delta1 = -1
        shareholders1 = "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = -1
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)       
        revenue_plug = formatting_plug(revenue1, revenue_delta1) 
        expense_plug = formatting_plug(expenses1, expense_delta1) 
        profit_plug = formatting_plug(profits1, profit_delta1)

        dashboard_1 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} €{revenue_delta1}{revenue_plug}|   {shareholders1}  {shareholder_delta1}    \n\
Expenses:  €{expenses1} €{expense_delta1}{expense_plug}|   {customers1}  {customer_delta1}    \n\
Profits:   €{profits1} €{profit_delta1}{profit_plug}|   {employees1}  {employee_delta1}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta1 + customer_delta1 + employee_delta1)}\n"
        clear()
        typewriter(scenario_1_answer_1, 0.015)
        typewriter(dashboard_1, 0.003)
        input("\nPress Enter To Proceed to Next Scenario")
    
    elif input1 == "B":
        revenue_delta1 = 0
        revenue1 = revenue + revenue_delta1
        expense_delta1 = 0
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses 
        profit_delta1 = revenue_delta1 - expense_delta1
        profits1 = revenue1 - expenses1
        shareholder_delta1 = 0
        shareholders1 = "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        revenue_plug = formatting_plug(revenue1, revenue_delta1) 
        expense_plug = formatting_plug(expenses1, expense_delta1) 
        profit_plug = formatting_plug(profits1, profit_delta1)

        dashboard_1 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} €{revenue_delta1}{revenue_plug}|   {shareholders1}  {shareholder_delta1}    \n\
Expenses:  €{expenses1} €{expense_delta1}{expense_plug}|   {customers1}  {customer_delta1}    \n\
Profits:   €{profits1} €{profit_delta1}{profit_plug}|   {employees1}  {employee_delta1}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta1 + customer_delta1 + employee_delta1)}\n"
        clear()
        print(scenario_1_answer_2)
        print(dashboard_1)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta1 = 50000
        revenue1 = revenue + revenue_delta1
        expense_delta1 = 0
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses 
        profit_delta1 = revenue_delta1 - expense_delta1
        profits1 = revenue1 - expenses1
        shareholder_delta1 = 1
        shareholders1 = "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        revenue_plug = formatting_plug(revenue1, revenue_delta1) 
        expense_plug = formatting_plug(expenses1, expense_delta1) 
        profit_plug = formatting_plug(profits1, profit_delta1)

        dashboard_1 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} €{revenue_delta1}{revenue_plug}|   {shareholders1}  {shareholder_delta1}    \n\
Expenses:  €{expenses1} €{expense_delta1}{expense_plug}|   {customers1}  {customer_delta1}    \n\
Profits:   €{profits1} €{profit_delta1}{profit_plug}|   {employees1}  {employee_delta1}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta1 + customer_delta1 + employee_delta1)}\n"
        clear()
        print(scenario_1_answer_3)
        print(dashboard_1)
        input("\nPress Enter To Proceed to Next Scenario\n")
    
    return revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1



# print(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1)
# print(dashboard_1)

def question_2(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1):
    
    clear()
    print(dashboard_1)
    scenario_2 = "\nScenario 2: You must decide at what level the marketing budget \n\
should be set for the coming year:\n\
\nA. Increase Marketing Expenditure \n\
B. Maintain Marketing Expenditure \n\
C. Decrease Marketing Expenditure \n"
    print(scenario_2)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_2_answer_1 = "\nYou have chosen Option A\n \n- Increasing the Marketing Budget by ~5% has resulted in an increase in projected\n\
units sold, with increasing customer interest\n\
- Yearly Revenue projection increases run ahead of equivalent expenditure increase projections\n\
- Profit projections have increased as a result\n"
    scenario_2_answer_2 = "\nYou have chosen Option B\n \n- Retaining current marketing expenditure levels has resulted in flat projected\n\
unit sales\n\
- Yearly Revenue projections remain unchanged as a result\n\
- With expenditure forecasts unchanged, Profit projections remained static\n"
    scenario_2_answer_3 = "\nYou have chosen Option C\n \n- Decreasing the Marketing Budget by ~5% has resulted in an decrease in projected\n\
units sold, with cusotmers choosing competitor alternatives\n\
- Yearly Revenue projection decreases are exceeding the equivalent reductions in expenditure projections\n\
- Profit projections have decreased as a result\n"

    
    if input1 == "A":        
        revenue_delta2 = 100000
        revenue2 = revenue1 + revenue_delta2
        expense_delta2 = 50000
        expenses2 = expenses1 + expense_delta2
        profit_delta2 = revenue_delta2 - expense_delta2
        profits2 = revenue2 - expenses2
        shareholder_delta2 = shareholder_delta1 + 1
        shareholders2 = "Shareholders:      " + emoji_assignment(shareholder_delta2)
        customer_delta2 = customer_delta1 + 1
        customers2 = "Customers:         " + emoji_assignment(customer_delta2)
        employee_delta2 = 0
        employees2 = "Employees:         " + emoji_assignment(employee_delta2)
        revenue_plug = formatting_plug(revenue2, revenue_delta2) 
        expense_plug = formatting_plug(expenses2, expense_delta2) 
        profit_plug = formatting_plug(profits2, profit_delta2)
        

        dashboard_2 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue2} €{revenue_delta2}{revenue_plug}|   {shareholders2}  {shareholder_delta2}    \n\
Expenses:  €{expenses2} €{expense_delta2}{expense_plug}|   {customers2}  {customer_delta2}    \n\
Profits:   €{profits2} €{profit_delta2}{profit_plug}|   {employees2}  {employee_delta2}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta2 + customer_delta2 + employee_delta2)}\n"
        clear()
        print(scenario_2_answer_1)
        print(dashboard_2)
        input("\nPress Enter To Proceed to Next Scenario")
    
    elif input1 == "B":
        revenue_delta2 = 0
        revenue2 = revenue1 + revenue_delta2
        expense_delta2 = 0
        expenses2 = expenses1 + expense_delta2
        profit_delta2 = revenue_delta2 - expense_delta2
        profits2 = revenue2 - expenses2
        shareholder_delta2 = shareholder_delta1 + 0
        shareholders2 = shareholders1
        customer_delta2 = customer_delta1 + 0
        customers2 = customers1
        employee_delta2 = 0
        employees2 = employees1        
        revenue_plug = formatting_plug(revenue2, revenue_delta2) 
        expense_plug = formatting_plug(expenses2, expense_delta2) 
        profit_plug = formatting_plug(profits2, profit_delta2)
        

        dashboard_2 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue2} €{revenue_delta2}{revenue_plug}|   {shareholders2}  {shareholder_delta2}    \n\
Expenses:  €{expenses2} €{expense_delta2}{expense_plug}|   {customers2}  {customer_delta2}    \n\
Profits:   €{profits2} €{profit_delta2}{profit_plug}|   {employees2}  {employee_delta2}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta2 + customer_delta2 + employee_delta2)}\n"
        clear()
        print(scenario_2_answer_2)
        print(dashboard_2)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta2 = -50000
        revenue2 = revenue1 + revenue_delta2
        expense_delta2 = -50000
        expenses2 = expenses1 + expense_delta2
        profit_delta2 = revenue_delta2 - expense_delta2
        profits2 = revenue2 - expenses2
        shareholder_delta2 = shareholder_delta1 - 1
        shareholders2 = "Shareholders:      " + emoji_assignment(shareholder_delta2)
        customer_delta2 = customer_delta1 - 1
        customers2 = "Customers:         " + emoji_assignment(customer_delta2)
        employee_delta2 = 0
        employees2 = "Employees:         " + emoji_assignment(employee_delta2)        
        revenue_plug = formatting_plug(revenue2, revenue_delta2) 
        expense_plug = formatting_plug(expenses2, expense_delta2) 
        profit_plug = formatting_plug(profits2, profit_delta2)        

        dashboard_2 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue2} €{revenue_delta2}{revenue_plug}|   {shareholders2}  {shareholder_delta2}    \n\
Expenses:  €{expenses2} €{expense_delta2}{expense_plug}|   {customers2}  {customer_delta2}    \n\
Profits:   €{profits2} €{profit_delta2}{profit_plug}|   {employees2}  {employee_delta2}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta2 + customer_delta2 + employee_delta2)}\n"
        clear()
        print(scenario_2_answer_3)
        print(dashboard_2)
        input("\nPress Enter To Proceed to Next Scenario")
    
    return revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2


def question_3(revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2):
    
    clear()
    print(dashboard_2)
    scenario_3 = "\nScenario 3: You must Choose the new material supplier rate \n\
for the coming year:\n\
\nA. Premium rate - Increase Expenditure \n\
B. Maintain Rate - Maintain Expenditure \n\
C. Low Cost Rate - Decrease Expenditure \n"
    print(scenario_3)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_3_answer_1 = "\nYou have chosen Option A\n \n- Increasing the Material Supplier rate by ~5% has resulted in an increase in material\n\
quality, without increasing units sold\n\
- Yearly Revenue projections are unchanged, whilst expense projections have slightly increased\n\
- Profit projections have slightly decreased for the year as a result\n"
    scenario_3_answer_2 = "\nYou have chosen Option B\n \n- Retaining current material supply rates has resulted in flat projected\n\
unit costs and unit sales\n\
- Yearly Revenue projections remain unchanged as a result\n\
- With expenditure forecasts unchanged, Profit projections remained static\n"
    scenario_3_answer_3 = "\nYou have chosen Option C\n \n- Decreasing the material supply rate by ~5% has resulted in an decrease in projected\n\
unit costs\n\
- Yearly Revenue projections are unchanged, however cost projections have decreased\n\
- Profit projections for the year have improved as a result\n"

    
    if input1 == "A":        
        revenue_delta3 = 0
        revenue3 = revenue2 + revenue_delta2
        expense_delta3 = 50000
        expenses3 = expenses2 + expense_delta3
        profit_delta3 = revenue_delta3 - expense_delta3
        profits3 = revenue3 - expenses3
        shareholder_delta3 = shareholder_delta2 + 0
        shareholders3 = "Shareholders:      " + emoji_assignment(shareholder_delta3)
        customer_delta3 = customer_delta2 + 1
        customers3 = "Customers:         " + emoji_assignment(customer_delta3)
        employee_delta3 = employee_delta2 + 1
        employees3 = "Employees:         " + emoji_assignment(employee_delta3)
        revenue_plug = formatting_plug(revenue3, revenue_delta3) 
        expense_plug = formatting_plug(expenses3, expense_delta3) 
        profit_plug = formatting_plug(profits3, profit_delta3)
        

        dashboard_3 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue3} €{revenue_delta3}{revenue_plug}|   {shareholders3}  {shareholder_delta3}    \n\
Expenses:  €{expenses3} €{expense_delta3}{expense_plug}|   {customers3}  {customer_delta3}    \n\
Profits:   €{profits3} €{profit_delta3}{profit_plug}|   {employees3}  {employee_delta3}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta3 + customer_delta3 + employee_delta3)}\n"
        clear()
        print(scenario_3_answer_1)
        print(dashboard_3)
        input("\nPress Enter To Proceed to Next Scenario")
    
    elif input1 == "B":
        revenue_delta3 = 0
        revenue3 = revenue2 + revenue_delta2
        expense_delta3 = 0
        expenses3 = expenses2 + expense_delta3
        profit_delta3 = revenue_delta3 - expense_delta3
        profits3 = revenue3 - expenses3
        shareholder_delta3 = shareholder_delta2 + 0
        shareholders3 = "Shareholders:      " + emoji_assignment(shareholder_delta3)
        customer_delta3 = customer_delta2 + 0
        customers3 = "Customers:         " + emoji_assignment(customer_delta3)
        employee_delta3 = employee_delta2 + 0
        employees3 = "Employees:         " + emoji_assignment(employee_delta3)
        revenue_plug = formatting_plug(revenue3, revenue_delta3) 
        expense_plug = formatting_plug(expenses3, expense_delta3) 
        profit_plug = formatting_plug(profits3, profit_delta3)
        

        dashboard_3 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue3} €{revenue_delta3}{revenue_plug}|   {shareholders3}  {shareholder_delta3}    \n\
Expenses:  €{expenses3} €{expense_delta3}{expense_plug}|   {customers3}  {customer_delta3}    \n\
Profits:   €{profits3} €{profit_delta3}{profit_plug}|   {employees3}  {employee_delta3}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta3 + customer_delta3 + employee_delta3)}\n"
        clear()
        print(scenario_3_answer_2)
        print(dashboard_3)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta3 = 0
        revenue3 = revenue2 + revenue_delta2
        expense_delta3 = -50000
        expenses3 = expenses2 + expense_delta3
        profit_delta3 = revenue_delta3 - expense_delta3
        profits3 = revenue3 - expenses3
        shareholder_delta3 = shareholder_delta2 + 1
        shareholders3 = "Shareholders:      " + emoji_assignment(shareholder_delta3)
        customer_delta3 = customer_delta2 + -1
        customers3 = "Customers:         " + emoji_assignment(customer_delta3)
        employee_delta3 = employee_delta2 + 0
        employees3 = "Employees:         " + emoji_assignment(employee_delta3)
        revenue_plug = formatting_plug(revenue3, revenue_delta3) 
        expense_plug = formatting_plug(expenses3, expense_delta3) 
        profit_plug = formatting_plug(profits3, profit_delta3)
        

        dashboard_3 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue3} €{revenue_delta3}{revenue_plug}|   {shareholders3}  {shareholder_delta3}    \n\
Expenses:  €{expenses3} €{expense_delta3}{expense_plug}|   {customers3}  {customer_delta3}    \n\
Profits:   €{profits3} €{profit_delta3}{profit_plug}|   {employees3}  {employee_delta3}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta3 + customer_delta3 + employee_delta3)}\n"
        clear()
        print(scenario_3_answer_3)
        print(dashboard_3)
        input("\nPress Enter To Proceed to Next Scenario")
    
    return revenue3, revenue_delta3, expenses3, expense_delta3, profits3, profit_delta3, shareholders3, shareholder_delta3, customers3, customer_delta3, employees3, employee_delta3, dashboard_3



def question_4(revenue3, revenue_delta3, expenses3, expense_delta3, profits3, profit_delta3, shareholders3, shareholder_delta3, customers3, customer_delta3, employees3, employee_delta3, dashboard_3):
    
    clear()
    print(dashboard_3)
    scenario_4 = "\nScenario 4: You must now help set the employee payroll budget \n\
for the coming year:\n\
\nA. Increase Payroll Budget (Increasing Expenditure) \n\
B. Maintain Payroll Budget - (Maintaining Expenditure) \n\
C. Reduce Payroll Budget - (Decreasing Expenditure) \n"
    print(scenario_4)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_4_answer_1 = "\nYou have chosen Option A\n \n- Increasing the payroll budget has resulted in an increase in yearly\n\
expenditure projections, without increasing units sold\n\
- Yearly Revenue projections are unchanged, whilst expense projections have slightly increased\n\
- Profit projections have slightly decreased for the year as a result\n"
    scenario_4_answer_2 = "\nYou have chosen Option B\n \n- Retaining current employee payroll budget has resulted in flat projected\n\
unit costs\n\
- Yearly Revenue projections remain unchanged\n\
- With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_4_answer_3 = "\nYou have chosen Option C\n \n- Decreasing the employee payroll budget has resulted in a decrease in projected\n\
unit costs\n\
- Yearly Revenue projections are unchanged, however cost projections have decreased\n\
- Profit projections for the year have improved as a result - however - employees are not happy!\n"

    
    if input1 == "A":        
        revenue_delta4 = 0
        revenue4 = revenue3 + revenue_delta4
        expense_delta4 = 50000
        expenses4 = expenses3 + expense_delta4
        profit_delta4 = revenue_delta4 - expense_delta4
        profits4 = revenue4 - expenses4
        shareholder_delta4 = shareholder_delta3 - 1
        shareholders4 = "Shareholders:      " + emoji_assignment(shareholder_delta4)
        customer_delta4 = customer_delta3 + 0
        customers4 = "Customers:         " + emoji_assignment(customer_delta4)
        employee_delta4 = employee_delta3 + 1
        employees4 = "Employees:         " + emoji_assignment(employee_delta4)
        revenue_plug = formatting_plug(revenue4, revenue_delta4) 
        expense_plug = formatting_plug(expenses4, expense_delta4) 
        profit_plug = formatting_plug(profits4, profit_delta4)
        

        dashboard_4 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue4} €{revenue_delta4}{revenue_plug}|   {shareholders4}  {shareholder_delta4}    \n\
Expenses:  €{expenses4} €{expense_delta4}{expense_plug}|   {customers4}  {customer_delta4}    \n\
Profits:   €{profits4} €{profit_delta4}{profit_plug}|   {employees4}  {employee_delta4}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta4 + customer_delta4 + employee_delta4)}\n"
        clear()
        print(scenario_4_answer_1)
        print(dashboard_4)
        input("\nPress Enter To Proceed to Next Scenario")
    
    elif input1 == "B":
        revenue_delta4 = 0
        revenue4 = revenue3 + revenue_delta4
        expense_delta4 = 0
        expenses4 = expenses3 + expense_delta4
        profit_delta4 = revenue_delta4 - expense_delta4
        profits4 = revenue4 - expenses4
        shareholder_delta4 = shareholder_delta3 + 0
        shareholders4 = "Shareholders:      " + emoji_assignment(shareholder_delta4)
        customer_delta4 = customer_delta3 + 0
        customers4 = "Customers:         " + emoji_assignment(customer_delta4)
        employee_delta4 = employee_delta3 + 0
        employees4 = "Employees:         " + emoji_assignment(employee_delta4)
        revenue_plug = formatting_plug(revenue4, revenue_delta4) 
        expense_plug = formatting_plug(expenses4, expense_delta4) 
        profit_plug = formatting_plug(profits4, profit_delta4)
        

        dashboard_4 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue4} €{revenue_delta4}{revenue_plug}|   {shareholders4}  {shareholder_delta4}    \n\
Expenses:  €{expenses4} €{expense_delta4}{expense_plug}|   {customers4}  {customer_delta4}    \n\
Profits:   €{profits4} €{profit_delta4}{profit_plug}|   {employees4}  {employee_delta4}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta4 + customer_delta4 + employee_delta4)}\n"
        clear()
        print(scenario_4_answer_2)
        print(dashboard_4)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta4 = 0
        revenue4 = revenue3 + revenue_delta4
        expense_delta4 = -50000
        expenses4 = expenses3 + expense_delta4
        profit_delta4 = revenue_delta4 - expense_delta4
        profits4 = revenue4 - expenses4
        shareholder_delta4 = shareholder_delta3 + 1
        shareholders4 = "Shareholders:      " + emoji_assignment(shareholder_delta4)
        customer_delta4 = customer_delta3 + 0
        customers4 = "Customers:         " + emoji_assignment(customer_delta4)
        employee_delta4 = employee_delta3 - 1
        employees4 = "Employees:         " + emoji_assignment(employee_delta4)
        revenue_plug = formatting_plug(revenue4, revenue_delta4) 
        expense_plug = formatting_plug(expenses4, expense_delta4) 
        profit_plug = formatting_plug(profits4, profit_delta4)
        

        dashboard_4 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue4} €{revenue_delta4}{revenue_plug}|   {shareholders4}  {shareholder_delta4}    \n\
Expenses:  €{expenses4} €{expense_delta4}{expense_plug}|   {customers4}  {customer_delta4}    \n\
Profits:   €{profits4} €{profit_delta4}{profit_plug}|   {employees4}  {employee_delta4}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta4 + customer_delta4 + employee_delta4)}\n"
        clear()
        print(scenario_4_answer_3)
        print(dashboard_4)
        input("\nPress Enter To Proceed to Next Scenario")
    
    return revenue4, revenue_delta4, expenses4, expense_delta4, profits4, profit_delta4, shareholders4, shareholder_delta4, customers4, customer_delta4, employees4, employee_delta4, dashboard_4



def question_5(revenue4, revenue_delta4, expenses4, expense_delta4, profits4, profit_delta4, shareholders4, shareholder_delta4, customers4, customer_delta4, employees4, employee_delta4, dashboard_4):
    
    clear()
    print(dashboard_4)
    scenario_5 = "\nScenario 5: You must now choose a 'Workplace Improvement Strategy' expenditure level \n\
for the coming year:\n\
\nA. Increase (Increasing Expenditure) \n\
B. Maintain - (Maintaining Expenditure) \n\
C. Reduce - (Decreasing Expenditure) \n"
    print(scenario_5)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_5_answer_1 = "\nYou have chosen Option A\n \n- Increasing the Workplace Improvement budget has resulted in an increase in yearly\n\
expenditure projections, without increasing units sold\n\
- Yearly Revenue projections are unchanged, whilst expense projections have slightly increased\n\
- Profit projections have slightly decreased for the year as a result\n"
    scenario_5_answer_2 = "\nYou have chosen Option B\n \n- Retaining the current Workplace Improvement budget has resulted in flat projected\n\
unit costs\n\
- Yearly Revenue projections remain unchanged\n\
- With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_5_answer_3 = "\nYou have chosen Option C\n \n- Decreasing the Workplace Improvement budget has resulted in a decrease in projected\n\
unit costs\n\
- Yearly Revenue projections are unchanged, however cost projections have decreased\n\
- Profit projections for the year have improved as a result - however - employees are not happy!\n"

    
    if input1 == "A":        
        revenue_delta5 = 0
        revenue5 = revenue4 + revenue_delta5
        expense_delta5 = 50000
        expenses5 = expenses4 + expense_delta5
        profit_delta5 = revenue_delta5 - expense_delta5
        profits5 = revenue5 - expenses5
        shareholder_delta5 = shareholder_delta4 - 1
        shareholders5 = "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 + 1
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5) 
        expense_plug = formatting_plug(expenses5, expense_delta5) 
        profit_plug = formatting_plug(profits5, profit_delta5)
        

        dashboard_5 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue5} €{revenue_delta5}{revenue_plug}|   {shareholders5}  {shareholder_delta5}    \n\
Expenses:  €{expenses5} €{expense_delta5}{expense_plug}|   {customers5}  {customer_delta5}    \n\
Profits:   €{profits5} €{profit_delta5}{profit_plug}|   {employees5}  {employee_delta5}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta5 + customer_delta5 + employee_delta5)}\n"
        clear()
        print(scenario_5_answer_1)
        print(dashboard_5)
        input(f"\n This completes the final scenario - you have scored {final_score(shareholder_delta5, customer_delta5, employee_delta5)} Please Press Enter")
        
    
    elif input1 == "B":
        revenue_delta5 = 0
        revenue5 = revenue4 + revenue_delta5
        expense_delta5 = 0
        expenses5 = expenses4 + expense_delta5
        profit_delta5 = revenue_delta5 - expense_delta5
        profits5 = revenue5 - expenses5
        shareholder_delta5 = shareholder_delta4 + 0
        shareholders5 = "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 + 0
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5) 
        expense_plug = formatting_plug(expenses5, expense_delta5) 
        profit_plug = formatting_plug(profits5, profit_delta5)
        

        dashboard_5 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue5} €{revenue_delta5}{revenue_plug}|   {shareholders5}  {shareholder_delta5}    \n\
Expenses:  €{expenses5} €{expense_delta5}{expense_plug}|   {customers5}  {customer_delta5}    \n\
Profits:   €{profits5} €{profit_delta5}{profit_plug}|   {employees5}  {employee_delta5}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta5 + customer_delta5 + employee_delta5)}\n"
        clear()
        print(scenario_5_answer_2)
        print(dashboard_5)
        input(f"\n This completes the final scenario - you have scored {final_score(shareholder_delta5, customer_delta5, employee_delta5)} Please Press Enter")
        

    elif input1 == "C":
        revenue_delta5 = 0
        revenue5 = revenue4 + revenue_delta5
        expense_delta5 = -50000
        expenses5 = expenses4 + expense_delta5
        profit_delta5 = revenue_delta5 - expense_delta5
        profits5 = revenue5 - expenses5
        shareholder_delta5 = shareholder_delta4 - 1
        shareholders5 = "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 + 1
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5) 
        expense_plug = formatting_plug(expenses5, expense_delta5) 
        profit_plug = formatting_plug(profits5, profit_delta5)
        

        dashboard_5 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue5} €{revenue_delta5}{revenue_plug}|   {shareholders5}  {shareholder_delta5}    \n\
Expenses:  €{expenses5} €{expense_delta5}{expense_plug}|   {customers5}  {customer_delta5}    \n\
Profits:   €{profits5} €{profit_delta5}{profit_plug}|   {employees5}  {employee_delta5}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta5 + customer_delta5 + employee_delta5)}\n"
        clear()
        print(scenario_5_answer_3)
        print(dashboard_5)
        input(f"\n This completes the final scenario - you have scored {final_score(shareholder_delta5, customer_delta5, employee_delta5)} Please Press Enter")        
    
    return revenue5, revenue_delta5, expenses5, expense_delta5, profits5, profit_delta5, shareholders5, shareholder_delta5, customers5, customer_delta5, employees5, employee_delta5, dashboard_5



def main():
    """
    Main function containing questions for game execution
    """
    revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1 = question_1(revenue, revenue_delta, expenses, expense_delta, profits, profit_delta, shareholders, shareholder_delta, customers, customer_delta, employees, employee_delta, dashboard_0)
    revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2 = question_2(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1)
    revenue3, revenue_delta3, expenses3, expense_delta3, profits3, profit_delta3, shareholders3, shareholder_delta3, customers3, customer_delta3, employees3, employee_delta3, dashboard_3 = question_3(revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2)
    revenue4, revenue_delta4, expenses4, expense_delta4, profits4, profit_delta4, shareholders4, shareholder_delta4, customers4, customer_delta4, employees4, employee_delta4, dashboard_4 = question_4(revenue3, revenue_delta3, expenses3, expense_delta3, profits3, profit_delta3, shareholders3, shareholder_delta3, customers3, customer_delta3, employees3, employee_delta3, dashboard_3)
    revenue5, revenue_delta5, expenses5, expense_delta5, profits5, profit_delta5, shareholders5, shareholder_delta5, customers5, customer_delta5, employees5, employee_delta5, dashboard_5 = question_5(revenue4, revenue_delta4, expenses4, expense_delta4, profits4, profit_delta4, shareholders4, shareholder_delta4, customers4, customer_delta4, employees4, employee_delta4, dashboard_4)
    return shareholder_delta5, customer_delta5, employee_delta5


shareholder_delta5, customer_delta5, employee_delta5 = main()


def finish_game():
    """
    Closing game loop triggered post completion of final question
    """
    loop = True
    while loop:
        clear()
        choice = input(f"Press E to exit or if you would like to try to improve your score, press any key followed by enter to play again:")
        if choice.upper() == "E":
            print("Goodbye")
            loop = False
        else:
            shareholder_delta5, customer_delta5, employee_delta5 = main()


finish_game()