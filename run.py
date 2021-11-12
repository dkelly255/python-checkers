# Initial import of required external libraries & functions
from os import system, name
from random import choice
from time import sleep
import sys

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


def formatting_plug(a, b):
    """
    Plug spaces to visually align dashboard segregation on terminal display
    depending on length of variables
    """
    plug = (14 - (len(str(a)) + len(str(b)))) * " "
    return plug


def final_score(a, b, c):
    """
    Calculates player's total score upon conclusion of the final answer
    """
    total_points = a + b + c
    return total_points


def main_menu():
    """
    Displays main menu screen upon game load
    """
    print("\n----------------------------------------------------------------")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                   W E L C O M E                                |")
    print("|                                                                |")
    print("|                       T O                                      |")
    print("|                                                                |")
    print("|                         P Y T H O N                            |")
    print("|                                                                |")
    print("|                            T E X T                             |")
    print("|                                                                |")
    print("|                               A D V E N T U R E                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                     [ PRESS ENTER TO BEGIN ]                   |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("------------------------------------------------------------------")
    input()
    clear()


# Credits: This function was sourced from the article below and adapted for my
# project needs:
# Credits:
# www.codegrepper.com/code-examples/python/typewriter+effect+python+terminal
def typewriter(text, delay):
    """
    Function for presenting text with a delayed/typewriter effect to add to
    game User Experience UX
    """
    for letter in text:
        sleep(delay)
        sys.stdout.write(letter)
        sys.stdout.flush()


def question_1(
    revenue, revenue_delta, expenses, expense_delta,
        profits, profit_delta, shareholders, shareholder_delta,
        customers, customer_delta, employees, employee_delta, dashboard_0):

    clear()
    typewriter(dashboard_0, 0.0003)
    scenario_1 = "\n    Scenario 1: You must decide at what level the selling price for \n\
    FictonalCorp's leading product should be set for the coming year:\n\
    \n    A. Increase Current Selling Price\n\
    B. Maintain Current Selling Price \n\
    C. Reduce Current Selling Price\n"
    typewriter(scenario_1, 0.0015)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_1_answer_1 = "\nYou have chosen Option A\
    \n \n\
    - Increasing Selling Prices by ~5% has resulted in a decrease in\n\
    projected units sold, with customers choosing competitor alternatives\n\
    \n    - Unfortunately overall Revenue projections have declined\n\
    \n    - With expenses flat, profit projections have fallen as a result\n"
    scenario_1_answer_2 = "\nYou have chosen Option B\
    \n \n\
    - Maintaining Current Selling Prices has had no effect on projected\n\
    units sold\n\
    - Overall Revenue projections are unchanged\n\
    - With expenses flat, profit projections are unchanged as a result\n"
    scenario_1_answer_3 = "\nYou have chosen Option C\
    \n \n\
    - Reducing Selling Prices by ~5% results in an increase in projected\n\
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
        shareholders1 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = -1
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        revenue_plug = formatting_plug(revenue1, revenue_delta1)
        expense_plug = formatting_plug(expenses1, expense_delta1)
        profit_plug = formatting_plug(profits1, profit_delta1)
        points = shareholder_delta1 + customer_delta1 + employee_delta1
        dashboard_1 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue1} €{revenue_delta1}{revenue_plug}|   {shareholders1}\
  {shareholder_delta1}    \n\
    Expenses:  €{expenses1} €{expense_delta1}{expense_plug}|   {customers1}\
  {customer_delta1}    \n\
    Profits:   €{profits1} €{profit_delta1}{profit_plug}|   {employees1}\
  {employee_delta1}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_1_answer_1, 0.0015)
        typewriter(dashboard_1, 0.0003)
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
        shareholders1 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        revenue_plug = formatting_plug(revenue1, revenue_delta1)
        expense_plug = formatting_plug(expenses1, expense_delta1)
        profit_plug = formatting_plug(profits1, profit_delta1)
        points = shareholder_delta1 + customer_delta1 + employee_delta1
        dashboard_1 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue1} €{revenue_delta1}{revenue_plug}|   {shareholders1}\
  {shareholder_delta1}    \n\
    Expenses:  €{expenses1} €{expense_delta1}{expense_plug}|   {customers1}\
  {customer_delta1}    \n\
    Profits:   €{profits1} €{profit_delta1}{profit_plug}|   {employees1}\
  {employee_delta1}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
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
        shareholders1 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        revenue_plug = formatting_plug(revenue1, revenue_delta1)
        expense_plug = formatting_plug(expenses1, expense_delta1)
        profit_plug = formatting_plug(profits1, profit_delta1)
        points = shareholder_delta1 + customer_delta1 + employee_delta1
        dashboard_1 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue1} €{revenue_delta1}{revenue_plug}|   {shareholders1}\
  {shareholder_delta1}    \n\
    Expenses:  €{expenses1} €{expense_delta1}{expense_plug}|   {customers1}\
  {customer_delta1}    \n\
    Profits:   €{profits1} €{profit_delta1}{profit_plug}|   {employees1}\
  {employee_delta1}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        print(scenario_1_answer_3)
        print(dashboard_1)
        input("\nPress Enter To Proceed to Next Scenario\n")

    return revenue1, revenue_delta1, expenses1, expense_delta1, profits1,\
        profit_delta1, shareholders1, shareholder_delta1, customers1,\
        customer_delta1, employees1, employee_delta1, dashboard_1


def question_2(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1):

    clear()
    print(dashboard_1)
    scenario_2 = "\n    Scenario 2: You must decide at what level the marketing budget \n\
    should be set for the coming year:\n\
    \n    A. Increase Marketing Expenditure \n\
    B. Maintain Marketing Expenditure \n\
    C. Decrease Marketing Expenditure \n"
    print(scenario_2)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_2_answer_1 = "\nYou have chosen Option A\n \n    - Increasing the Marketing Budget by ~5% has resulted in an increase in projected\n\
    units sold, with increasing customer interest\n\
    - Yearly Revenue projection increases run ahead of equivalent expenditure increase projections\n\
    - Profit projections have increased as a result\n"
    scenario_2_answer_2 = "\nYou have chosen Option B\n \n    - Retaining current marketing expenditure levels has resulted in flat\n\
    projected unit sales\n\
    - Yearly Revenue projections remain unchanged as a result\n\
    - With expenditure forecasts unchanged, Profit projections remained static\n"
    scenario_2_answer_3 = "\nYou have chosen Option C\n \n    - Decreasing the Marketing Budget by ~5% has resulted in a decrease in projected\n\
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

        dashboard_2 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_2 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_2 = f"\n        ------------------------------------------------------------\n\
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
    scenario_3 = "\n    Scenario 3: You must Choose the new material supplier rate \n\
    for the coming year:\n\
    \n    A. Premium rate - Increase Expenditure \n\
    B. Maintain Rate - Maintain Expenditure \n\
    C. Low Cost Rate - Decrease Expenditure \n"
    print(scenario_3)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_3_answer_1 = "\nYou have chosen Option A\n \n    - Increasing the Material Supplier rate by ~5% has resulted in an increase in material\n\
    quality, without increasing units sold\n\
    - Yearly Revenue projections are unchanged, whilst expense projections have slightly increased\n\
    - Profit projections have slightly decreased for the year as a result\n"
    scenario_3_answer_2 = "\nYou have chosen Option B\n \n    - Retaining current material supply rates has resulted in flat projected\n\
    unit costs and unit sales\n\
    - Yearly Revenue projections remain unchanged as a result\n\
    - With expenditure forecasts unchanged, Profit projections remained static\n"
    scenario_3_answer_3 = "\nYou have chosen Option C\n \n    - Decreasing the material supply rate by ~5% has resulted in a decrease in\n\
      projected unit costs\n\
        - Yearly Revenue projections are unchanged, however cost projections have\n\
      decreased\n\
    \n- Profit projections for the year have improved as a result\n"

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

        dashboard_3 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_3 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_3 = f"\n        ------------------------------------------------------------\n\
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
    scenario_4 = "\n    Scenario 4: You must now help set the employee payroll budget \n\
    for the coming year:\n\
    \n    A. Increase Payroll Budget (Increasing Expenditure) \n\
    B. Maintain Payroll Budget - (Maintaining Expenditure) \n\
    C. Reduce Payroll Budget - (Decreasing Expenditure) \n"
    print(scenario_4)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_4_answer_1 = "\nYou have chosen Option A\n \n    - Increasing the payroll budget has resulted in an increase in yearly\n\
    expenditure projections, without increasing units sold\n\
    - Yearly Revenue projections are unchanged, whilst expense projections have\n\
      slightly increased\n\
    - Profit projections have slightly decreased for the year as a result\n"
    scenario_4_answer_2 = "\nYou have chosen Option B\n \n    - Retaining current employee payroll budget has resulted in flat projected\n\
    unit costs\n\
    - Yearly Revenue projections remain unchanged\n\
    - With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_4_answer_3 = "\nYou have chosen Option C\n \n    - Decreasing the employee payroll budget has resulted in a decrease in\n\
        projected unit costs\n\
    - Yearly Revenue projections are unchanged, however cost projections have\n\
        decreased\
    - Profit projections for the year have improved as a result - however -\n\
        employees are not happy!\n"

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

        dashboard_4 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_4 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_4 = f"\n        ------------------------------------------------------------\n\
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
    scenario_5 = "\n    Scenario 5: You must now choose a 'Workplace Improvement Strategy'\n\
        expenditure level for the coming year:\n\
    \n    A. Increase (Increasing Expenditure) \n\
    B. Maintain - (Maintaining Expenditure) \n\
    C. Reduce - (Decreasing Expenditure) \n"
    print(scenario_5)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_5_answer_1 = "\nYou have chosen Option A\n \n    - Increasing the Workplace Improvement budget has resulted in an increase\n\
        in yearly expenditure projections, without increasing units sold\n\
    - Yearly Revenue projections are unchanged, whilst expense projections have\n\
        slightly increased\
    - Profit projections have slightly decreased for the year as a result\n"
    scenario_5_answer_2 = "\nYou have chosen Option B\n \n    - Retaining the current Workplace Improvement budget has resulted in flat projected\n\
    unit costs\n\
    - Yearly Revenue projections remain unchanged\n\
    - With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_5_answer_3 = "\nYou have chosen Option C\n \n    - Decreasing the Workplace Improvement budget has resulted in a decrease in projected\n\
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

        dashboard_5 = f"\n        ------------------------------------------------------------\n\
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

        dashboard_5 = f"\n        ------------------------------------------------------------\n\
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
        shareholder_delta5 = shareholder_delta4 + 1
        shareholders5 = "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 - 1
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5)
        expense_plug = formatting_plug(expenses5, expense_delta5)
        profit_plug = formatting_plug(profits5, profit_delta5)

        dashboard_5 = f"\n        ------------------------------------------------------------\n\
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


def run_textadv():
    """
    Main function containing questions for game execution
    """
    revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1 = question_1(revenue, revenue_delta, expenses, expense_delta, profits, profit_delta, shareholders, shareholder_delta, customers, customer_delta, employees, employee_delta, dashboard_0)
    revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2 = question_2(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1)
    revenue3, revenue_delta3, expenses3, expense_delta3, profits3, profit_delta3, shareholders3, shareholder_delta3, customers3, customer_delta3, employees3, employee_delta3, dashboard_3 = question_3(revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2)
    revenue4, revenue_delta4, expenses4, expense_delta4, profits4, profit_delta4, shareholders4, shareholder_delta4, customers4, customer_delta4, employees4, employee_delta4, dashboard_4 = question_4(revenue3, revenue_delta3, expenses3, expense_delta3, profits3, profit_delta3, shareholders3, shareholder_delta3, customers3, customer_delta3, employees3, employee_delta3, dashboard_3)
    revenue5, revenue_delta5, expenses5, expense_delta5, profits5, profit_delta5, shareholders5, shareholder_delta5, customers5, customer_delta5, employees5, employee_delta5, dashboard_5 = question_5(revenue4, revenue_delta4, expenses4, expense_delta4, profits4, profit_delta4, shareholders4, shareholder_delta4, customers4, customer_delta4, employees4, employee_delta4, dashboard_4)
    return shareholder_delta5, customer_delta5, employee_delta5


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
            shareholder_delta5, customer_delta5, employee_delta5 = run_textadv()


def initialise_variables():
    # Initialise key variables
    # Answer bank & Word variables
    # word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]
    word_list = open('words.txt').read().split()
    for words in word_list:
        if len(words) < 3:
            word_list.remove(words)
    answer = choice(word_list)
    answer_hidden = ["Guess The Word: "]
    answer_hidden.extend(["_ "] * len(answer))
    # Guess variables
    guesses_used = 0
    incorrect_guesses = 0
    previous_guesses = ["Previous Guesses: "]
    # Gallows variables
    gallows_stage = 0
    guesses_remaining = 8 - gallows_stage
    return word_list, answer, answer_hidden, guesses_remaining, guesses_used, incorrect_guesses, previous_guesses, gallows_stage


def clear():
        """
        Clears the terminal for formatting purposes
        """
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


def welcome_screen():
        """
        Displays welcome screen to user upon loading
        the application. Allows proceeding to play
        the game upon pressing "Enter"
        """
        clear()
        print("--------------------------------------------")
        print("|                                          |")
        print("|                                          |")
        print("|       W  E  L  C  O  M  E                |")
        print("|                                          |")
        print("|          T O                             |")
        print("|                                          |")
        print("|             P  Y  T  H  O  N             |")
        print("|                                          |")
        print("|                 H  A  N  G  M  A  N      |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|         [PRESS ENTER TO BEGIN]           |")
        print("|                                          |")
        print("--------------------------------------------")
        input()
        clear()


def draw_gallows(gallows_stage):
    """
    Build up the hangman "gallows" element by
    element based on number of incorrect guesses
    """
    if gallows_stage == 0:
        print("   _________")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 1:
        print("   _________")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 2:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 3:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 4:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 5:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |       |")
        print("   |      /")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 6:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 7:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |      /|")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 8:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |      /|\\")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")


def main_game_screen(guesses_used, guesses_remaining, incorrect_guesses, answer_hidden):
    print("".join(answer_hidden))
    print(f"Guesses Used So Far: {guesses_used}")
    print(f"Guesses Remaining: {guesses_remaining}")
    print("".join(previous_guesses) + "\n")
    if guesses_remaining == 1:
        print(f"Final attempt!\nOne last chance to guess the word!\n")
    elif guesses_remaining == 3 or guesses_remaining == 2:
        print(f"Hurry!\nYou only have {guesses_remaining} lives left...\nTry guessing the word!\n")


def validate_guess(previous_guesses, guesses_remaining):
    while True:
        if guesses_remaining <= 3:
            guess_type = input("Press 'W' to guess a word, or 'L' to guess a letter: ").lower()
            if guess_type == "w":
                user_guess = input("\nPlease guess a word: ").lower()
                if len(user_guess) > 1:
                    if user_guess.isalpha():
                        if not ((user_guess + ", ") in previous_guesses):
                            if len(user_guess) == len(answer):
                                return user_guess
                            print(f"Sorry, {user_guess} is {len(user_guess)} characters long, but the answer is {len(answer)} characters long, please try again")
                            continue
                        print(f"\nSorry, You have already guessed the word '{user_guess}', please try again \n")
                        continue
                    print(f"\nSorry, Your guess must be a word, '{user_guess}' is not a word, please try again\n")
                    continue
                print(f"Sorry, The Word must not be a single character, '{user_guess}' is not valid, please try again\n")
            elif guess_type == "l":
                user_guess = input("\nPlease guess a letter: ").lower()
                if len(user_guess) == 1:
                    if user_guess.isalpha():
                        if not ((user_guess + ", ") in previous_guesses):
                            return user_guess
                        print(f"\nSorry, You have already guessed the letter '{user_guess}', please try again \n")
                        continue
                    print(f"\nSorry, Your guess must be a letter, '{user_guess}' is not a letter, please try again\n")
                    continue
                print(f"\nSorry, Your guess must be a single character only, '{user_guess}' is not valid, please try again\n")
            else:
                print(f"Sorry, '{guess_type}' is not a valid input, please try again")
        else:
            user_guess = input("\nPlease guess a letter: ").lower()
            if len(user_guess) == 1:
                if user_guess.isalpha():
                    if not ((user_guess + ", ") in previous_guesses):
                        return user_guess
                    print(f"\nSorry, You have already guessed the letter '{user_guess}', please try again \n")
                    continue
                print(f"\nSorry, Your guess must be a letter, '{user_guess}' is not a letter, please try again\n")
                continue
            print(f"\nSorry, Your Guess must be a single character only, '{user_guess}' is not valid, please try again\n")


def reveal_letter_in_answer(user_guess, answer, answer_hidden):

    if user_guess == answer:
        answer_hidden = ["Guess The Word: ", answer]
    else:
        for index, value in enumerate(answer, start=1):
            if user_guess == value:
                answer_hidden[index] = user_guess

    return answer_hidden


def answer_check(user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining):

    previous_guesses.append(user_guess + ", ")
    guesses_used += 1

    if user_guess == answer:
        answer_hidden = reveal_letter_in_answer(user_guess, answer, answer_hidden)
        print(f"\nCorrect! Great guess - '{user_guess}' was the answer!")
        sleep(0.75)
    elif user_guess in answer:
        answer_hidden = reveal_letter_in_answer(user_guess, answer, answer_hidden)
        print(f"\nCorrect! '{user_guess}' is in the answer")
        sleep(0.75)
    elif len(user_guess) > 1:
        print(f"\nSorry! The word '{user_guess}' is not the answer")
        sleep(0.75)
        gallows_stage += 1
        incorrect_guesses += 1
        guesses_remaining = 8 - gallows_stage
    else:
        print(f"\nSorry! '{user_guess}' is not in the answer")
        sleep(0.75)
        gallows_stage += 1
        incorrect_guesses += 1
        guesses_remaining = 8 - gallows_stage

    return user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining


def play_game(previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining):
    while "_ " in answer_hidden:
        if gallows_stage == 8:
            clear()
            draw_gallows(gallows_stage)
            answer_hidden = ["Guess The Word: ", answer]
            main_game_screen(guesses_used, guesses_remaining, incorrect_guesses, answer_hidden)
            print(f"Sorry You Lost - the answer was '{answer}'\n")
            break
        else:
            clear()
            draw_gallows(gallows_stage)
            main_game_screen(guesses_used, guesses_remaining, incorrect_guesses, answer_hidden)
            user_guess = validate_guess(previous_guesses, guesses_remaining)
            user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining = answer_check(user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining)
            clear()
        draw_gallows(gallows_stage)
        main_game_screen(guesses_used, guesses_remaining, incorrect_guesses, answer_hidden)

        if not ("_ " in answer_hidden):
            clear()
            draw_gallows(gallows_stage)
            main_game_screen(guesses_used, guesses_remaining, incorrect_guesses, answer_hidden)
            print(f"Congratulations You Won - the answer was '{answer}'\n")
            sleep(0.75)

while True:
    print("--------------------------------------------")
    print("|                                          |")
    print("|           *** MAIN MENU ***              |")
    print("|                                          |")
    print("|      PLEASE SELECT A GAME TO PLAY:       |")
    print("|                                          |")
    print("|    A. HANGMAN                            |")
    print("|                                          |")
    print("|    B. ACCOUNTING ADVENTURES              |")
    print("|                                          |")
    print("|    C. EXIT APPLICATION                   |")
    print("|                                          |")
    print("|                                          |")
    print("|            [PLEASE SELECT]               |")
    print("|                                          |")
    print("--------------------------------------------")
    game = input("Select option A, B or C: ").lower()
    if game == "a":
        word_list, answer, answer_hidden, guesses_remaining, guesses_used, incorrect_guesses, previous_guesses, gallows_stage = initialise_variables()
        welcome_screen()
        play_game(
            previous_guesses, gallows_stage, incorrect_guesses,
            guesses_used, answer, answer_hidden, guesses_remaining)
        while True:
            stop_go = input(
                "Please press 'y' to play again, or press 'e' to exit: \
").lower()
            if stop_go == "e":
                print("\nThank you for playing Python Hangman - Goodbye!")
                sleep(0.5)
                clear()
                break
            elif stop_go == "y":
                word_list, answer, answer_hidden, guesses_remaining,\
                    guesses_used, incorrect_guesses, previous_guesses,\
                    gallows_stage = initialise_variables()
                play_game(
                    previous_guesses, gallows_stage, incorrect_guesses,
                    guesses_used, answer, answer_hidden, guesses_remaining)
            else:
                print("\nPlease enter a valid choice - press 'e' to exit or \
press 'y' to play again: ")
    elif game == "b":
        clear()
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

        dashboard_0 = f"\n        ------------------------------------------------------------\n\
        Financial Projections:         |     Stakeholder Sentiment :  \n\
        ------------------------------------------------------------\n\
        Revenue:   €{revenue} {revenue_delta}      |      {shareholders}\
            {shareholder_delta}    \
    Expenses:  €{expenses} {expense_delta}       |      {customers}\
        {customer_delta}    \
        Profits:   €{profits} {profit_delta}       |      {employees}\
            {employee_delta}    \
    ------------------------------------------------------------\n"

        intro = f"- The Year is 2021...\
        \n- FictionalCorp have hired you as their new CEO\
        \n- You have been tasked with improving their performance on 3x fronts\
        \n\n1. Shareholder Sentiment\
        \n2. Customer Confidence\
        \n3. Employee Engagement\n\
        \n- You will receive one point for each improvement in stakeholder\
        \nstatus\
        \n- You will lose one point for each decline in stakeholder status\
        \n- Navigate the following series of business decisions, and their\
        \nrespective stakeholder impacts\
        \n- Your performance will be displayed on a dashboard in the format\
        \nbelow: \n"

        main_menu()
        typewriter(intro, 0.0001)
        typewriter(dashboard_0, 0.001)
        input("\n[Press Enter To Begin]")
        shareholder_delta5, customer_delta5, employee_delta5 = run_textadv()
        finish_game()
    elif game == "c":
        print("Goodbye")
        break
    else:
        clear()
        print("Please enter a valid input - A, B or C")


# import keyboard
# def clear():
#     if name == 'nt':
#         _ = system('cls')
#     else:
#         _ = system('clear')

# game_mode_status = "PENDING"
# board_size = "PENDING"
# team_selection = "PENDING"
# play_status = "LOCKED"

# def begin_game():
#     global board_size
#     if board_size == "DEFAULT":
#         display_board_normal()
#     elif board_size == " LARGE ":
#         display_board_large()
#     else: 
#         display_board_xlarge()

# def display_board_normal():
#     print("                                      ")
#     print("--------------------------------------------")
#     print(f"Game mode:{game_mode_status}, Board Size: {board_size}")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|           A  B  C  D  E  F  G  H         |")
#     print("|                                          |")
#     print("|      0    O  -  &  -  O  -  0  -         |")
#     print("|      1    -  O  -  O  -  @  -  O         |")
#     print("|      2    O  -  O  -  O  -  O  -         |")
#     print("|      3    -  -  -  -  -  -  -  -         |")
#     print("|      4    -  -  -  -  -  -  -  -         |")
#     print("|      5    X  -  X  -  X  -  X  -         |")
#     print("|      6    -  X  -  X  -  X  -  X         |")
#     print("|      7    #  -  X  -  X  -  X  -         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     print("To Be Continued...")

# def e_start_game():
#     global play_status
#     if play_status != "LOCKED":
#         print("--------------------------------------------")
#         print("|                                          |")
#         print("|***************BEGIN GAME*****************|")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|           LET'S PLAY CHECKERS !          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|        [PRESS ENTER TO CONTINUE]         |")
#         print("--------------------------------------------")
#         input("")
#         clear()
#         begin_game()
#     else:
#         print("--------------------------------------------")
#         print("|                                          |")
#         print("|******** GAME LOCKED UNTIL SETUP *********|")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|           PLEASE COMPLETE GAME           |")
#         print("|              SETUP OPTIONS               |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|        [PRESS ENTER TO CONTINUE]         |")
#         print("--------------------------------------------")
#         input("")
#         clear()
#         setup_screen()

# def d_view_rules():
#     print("--------------------------------------------")
#     print("|****************GAME RULES****************|")
#     print("|                                          |")
#     print("| 1. Objective of the game is to capture   |")
#     print("|    all of the opposition's pieces        |")
#     print("|                                          |")
#     print("| 2. Pieces can normally only move one     |")
#     print("|    square - diagonally and forwards      |")
#     print("|                                          |")
#     print("| 3. An opposition piece is captured       |")
#     print("|    by jumping diagonally over it         |")
#     print("|                                          |")
#     print("| 4. The capture of an opposition piece    |")
#     print("|    is a compulsory move if possible      |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("--------------------------------------------")
#     setup = input("")
#     clear()        
#     setup_screen()

# def c_side_selection():
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|***********PLEASE CHOOSE A SIDE***********|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|             A. NOUGHTS [ O ]             |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|             B. CROSSES [ X ]             |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|             [PLEASE SELECT]              |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A or B: ")
#     if setup.upper() == "A":
#         clear()
#         side_selected_A()    
#     elif setup.upper() == "B":            
#         clear()        
#         side_selected_B()
#     else:
#         print("Please make a valid choice")

# def side_selected_A():
#     global team_selection 
#     team_selection = "NOUGHTS"
#     print("                                      ")
#     print("--------------------------------------------")
#     print("        You have chosen Team Noughts        ")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|          TEAM NOUGHTS SELECTED           |")
#     print("|                                          |")
#     print("|                  [ O ]                   |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
    
#     setup_screen()

# def side_selected_B():
#     global team_selection 
#     team_selection = "CROSSES"
#     print("                                      ")
#     print("--------------------------------------------")
#     print("        You have chosen Team Crosses        ")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|          TEAM CROSSES SELECTED           |")
#     print("|                                          |")
#     print("|                  [ X ]                   |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def select_board_normal():
#     global board_size 
#     board_size = "DEFAULT"
#     print("                                      ")
#     print("--------------------------------------------")
#     print("You have chosen Board Size: Standard (8 x 8)")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|           A  B  C  D  E  F  G  H         |")
#     print("|                                          |")
#     print("|      0    O  -  &  -  O  -  0  -         |")
#     print("|      1    -  O  -  O  -  @  -  O         |")
#     print("|      2    O  -  O  -  O  -  O  -         |")
#     print("|      3    -  -  -  -  -  -  -  -         |")
#     print("|      4    -  -  -  -  -  -  -  -         |")
#     print("|      5    X  -  X  -  X  -  X  -         |")
#     print("|      6    -  X  -  X  -  X  -  X         |")
#     print("|      7    #  -  X  -  X  -  X  -         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def select_board_large():
#     global board_size 
#     board_size = " LARGE "
#     print("                                      ")
#     print("-------------------------------------------")
#     print("You have chosen Board Size: Large (9 x 9)  ")
#     print("-------------------------------------------")
#     print("|                                          |")
#     print("|           A  B  C  D  E  F  G  H  I      |")
#     print("|                                          |")
#     print("|      0    O  -  O  -  O  -  O  -  O      |")
#     print("|      1    -  O  -  O  -  O  -  O  -      |")
#     print("|      2    O  -  O  -  O  -  O  -  O      |")
#     print("|      3    -  -  -  -  -  -  -  -  -      |")
#     print("|      4    -  -  -  -  -  -  -  -  -      |")
#     print("|      5    -  -  -  -  -  -  -  -  -      |")
#     print("|      6    -  X  -  X  -  X  -  X  -      |")
#     print("|      7    X  -  X  -  X  -  X  -  X      |")
#     print("|      8    -  X  -  X  -  X  -  X  -      |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def select_board_extralarge():
#     global board_size 
#     board_size = "X-LARGE"
#     print("                                         ")
#     print("-------------------------------------------------")
#     print("You have chosen Board Size: Extra-Large (10 x 10)")
#     print("-------------------------------------------------")
#     print("|                                               |")
#     print("|                                               |")
#     print("|           A  B  C  D  E  F  G  H  I  J        |")
#     print("|                                               |")
#     print("|      0    O  -  O  -  O  -  O  -  O  -        |")
#     print("|      1    -  O  -  O  -  O  -  O  -  O        |")
#     print("|      2    O  -  O  -  O  -  O  -  O  -        |")
#     print("|      3    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      4    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      5    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      6    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      7    X  -  X  -  X  -  X  -  X  -        |")
#     print("|      8    -  X  -  X  -  X  -  X  -  X        |")
#     print("|      9    X  -  X  -  X  -  X  -  X  -        |")
#     print("|                                               |")
#     print("|                                               |")
#     print("|        [PRESS ENTER TO CONTINUE]              |")
#     print("|_______________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def b_select_board_size():

#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT BOARD SIZE*************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|    A. STANDARD                           |")
#     print("|                                          |")
#     print("|    B. LARGE                              |")
#     print("|                                          |")
#     print("|    C. EXTRA-LARGE                        |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|            [PLEASE SELECT]               |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A, B or C: ")
#     if setup.upper() == "A":
#         clear()
#         select_board_normal()
#     elif setup.upper() == "B":            
#         clear()        
#         select_board_large()
#     elif setup.upper() == "C":            
#         clear()        
#         select_board_extralarge()        
#     else:
#         print("Please make a valid choice")

# def a_select_game_mode():

#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT GAME MODE**************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|    A. Player1    vs.    Computer         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|    B. Player1    vs.    Player2          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|            [PLEASE SELECT]               |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A or B: ")
#     if setup.upper() == "A":
#         clear()
#         game_mode_A()    
#     elif setup.upper() == "B":            
#         clear()        
#         game_mode_B()
#     else:
#         print("Please make a valid choice")

# def game_mode_A():
#     global game_mode_status 
#     game_mode_status = "P vs. C"
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT GAME MODE**************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|      YOU HAVE SELECTED GAME MODE: A      |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        PLAYER1    vs.   COMPUTER         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     input("")
#     clear()
#     setup_screen()

# def game_mode_B():
#     global game_mode_status 
#     game_mode_status = "P vs. P"
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT GAME MODE**************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|      YOU HAVE SELECTED GAME MODE: B      |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        PLAYER1    vs.   PLAYER2          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     input("")
#     clear()
#     setup_screen()

# def welcome_screen():
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|    W  E  L  C  O  M  E                   |")
#     print("|                                          |")
#     print("|       T O                                |")
#     print("|                                          |")
#     print("|          P  Y  T  H  O  N                |")
#     print("|                                          |")
#     print("|              C  H  E  C  K  E  R  S !    |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|         [PRESS ENTER TO BEGIN]           |")
#     print("|                                          |")
#     print("|                                          |")
#     print("--------------------------------------------")    

# welcome_screen()
# input("")
# clear()

# def setup_screen():
#     global play_status
#     global game_mode_status 
#     global board_size 
#     global team_selection 
#     if game_mode_status and board_size and team_selection != "PENDING":
#         play_status = "READY!"
#     else: 
#         play_status = "LOCKED"
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************GAME SETUP MENU:**************|")
#     print("|                                          |")
#     print(f"|    A. GAME MODE            [{game_mode_status}]     |")
#     print("|                                          |")
#     print(f"|    B. BOARD SIZE           [{board_size}]     |")
#     print("|                                          |")
#     print(f"|    C. SIDE SELECTION       [{team_selection}]     |")
#     print("|                                          |")
#     print("|    D. VIEW RULES           [OPTIONAL]    |")
#     print("|                                          |")
#     print(f"|    E. PLAY CHECKERS!       [{play_status}]      |")
#     print("|                                          |")
#     print("|         [PLEASE COMPLETE SETUP]          |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A to E: ")

#     if setup.upper() == "A":
#         clear()
#         a_select_game_mode()
#     elif setup.upper() == "B":
#         clear()
#         b_select_board_size()
#     elif setup.upper() == "C":
#         clear()
#         c_side_selection()
#     elif setup.upper() == "D":
#         clear()
#         d_view_rules()
#     elif setup.upper() == "E":
#         clear()
#         e_start_game()
#     else:
#         print("Please make a valid choice")

# setup_screen()

# This Section workings for setting up game
# print("                                      \n--------------------------------------------")
# print("You have chosen Board Size: Standard (8 x 8)")
# print("--------------------------------------------")
# print("|                                          |")
# print("|           A  B  C  D  E  F  G  H         |")
# print("|                                          |")
# print("|      0    O  -  &  -  O  -  0  -         |")
# print("|      1    -  O  -  O  -  @  -  O         |")
# print("|      2    O  -  O  -  O  -  O  -         |")
# print("|      3    -  -  -  -  -  -  -  -         |")
# print("|      4    -  -  -  -  -  -  -  -         |")
# print("|      5    X  -  X  -  X  -  X  -         |")
# print("|      6    -  X  -  X  -  X  -  X         |")
# print("|      7    #  -  X  -  X  -  X  -         |")
# print("|                                          |")
# print("|                                          |")
# print("|        [PRESS ENTER TO CONTINUE]         |")
# print("|__________________________________________|")
# input("")

# coordinates = []
# for x in range(10):
#     coordinates.append(x)
# print(f"coordinates={coordinates}")

# numbers=[]
# numbers = [x for x in range(10)]
# print(f"numbers={numbers}")

# board = []

# def make_row_1(display_lines):
#     row = ["|"]
#     row.extend([" "] * 4)
#     row.extend(["_"] * 8)
#     row.extend([" "] * 6)
#     row.extend(["|"])
#     display_lines.append(row)
#     return display_lines

# def create_board(display_lines):
#     make_row_1(display_lines)
#     return display_lines

# create_board(board)

# def print_board(display_lines):
#     print(display_lines)
#     for row in display_lines:
#         print("".join(row))

# print_board(board)

