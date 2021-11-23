# Initial import of required external libraries & functions
# Used at varying points by both games - Hangman & FictCorp Adventures
from os import system, name
from random import choice
from time import sleep
import sys


# Credits: As per readme credits section - the clear terminal function
# is taken from the methods used by geeksforgeeks.org - see full details
# and links in credits section of readme - used extensively throughout
# both applications


def clear():
    """
    Clears the terminal for formatting purposes - used extensively
    throughout both applications
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Credits: As per readme credits section - the class for adding colored
# text is taken from the stack overflow article - see full details
# and links in credits section of readme


class bcolors:
    """
    Class to enable adding colors to text throughout the application
    Credits:sourced from stack overflow article - please see full
    details in the credits section of README.md
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


# Note: ***FictCorp Adventures Section of Code Begins Here***


def emoji_assignment(delta):
    """
    Assigns emoji to dashboard categories based on stakeholder sentiment score
    Accepts a numeric delta as input parameter and returns the emoji for use
    in the stakeholder dashboard displays
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
    print("|                F I C T C O R P                                 |")
    print("|                                                                |")
    print("|                      A D V E N T U R E S                       |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                   SHAREHOLDERS:  😀                             |")
    print("|                                                                |")
    print("|                      CUSTOMERS:  😀                             |")
    print("|                                                                |")
    print("|                      EMPLOYEES:  😀                             |")
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


# Credits: Typewriter function was sourced from the article below and adapted
# for project needs - see credits section of readme for further detail:
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
    """
    First question of the game - requires 13x parameters and returns 13x values
    Displays the question & financial/stakeholder dashboard and asks the user
    to choose an answer.

    Based on the answer, the function will display one of three possible
    outcomes, each of which the function will reflect across the financial
    & stakeholder dashboard displays, along with the total cumulative points
    scored

    The function will then return the closing values for each variable to be
    passed on for use as arguments in the subsequent question
    """
    clear()
    # Print opening dashboard, use typewriter effect to enhance UX
    typewriter(dashboard_0, 0.003)
    # Text outlining scenario details for the user stored as string variable:
    scenario_1 = "\n    Scenario 1: You must decide at what level the selling price for \n\
    FictonalCorp's leading product should be set for the coming year:\n\
    \n    A. Increase Current Selling Price\n\
    B. Maintain Current Selling Price \n\
    C. Reduce Current Selling Price\n"
    typewriter(scenario_1, 0.01)
    # Request input from the user - choice between A, B or C
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        # Input validation to ensure no invalid data entered into program
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    # Answers A, B & C stored in strings in 3x variables below:
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
    # Code dealing with Decision Path "A"
    if input1 == "A":
        # Revenue decreases by €50,000
        revenue_delta1 = -50000
        # Updated revenue stored in variable revenue1
        revenue1 = revenue + revenue_delta1
        # No impact to costs in this scenario therefore expense delta = 0
        expense_delta1 = 0
        # Error Handling/Input validation for initial round of expense delta
        # calculations
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses
        # Calculate updated profit delta
        profit_delta1 = revenue_delta1 - expense_delta1
        # Calculate scenario's closing profit
        profits1 = revenue1 - expenses1
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta1 = -1
        # Updated Shareholder section of dashboard
        shareholders1 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta1)
        # Impact to customer sentiment of decision path chosen
        customer_delta1 = -1
        # Updated Customer section of dashboard
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        # Impact to employee sentiment of decision path chosen
        employee_delta1 = 0
        # Updated Employee section of dashboard
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue1, revenue_delta1)
        expense_plug = formatting_plug(expenses1, expense_delta1)
        profit_plug = formatting_plug(profits1, profit_delta1)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta1 + customer_delta1 + employee_delta1
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
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
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_1_answer_1, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_1, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "B":
        # No impact to revenue therefore revenue delta = 0
        revenue_delta1 = 0
        # Updated revenue stored in variable revenue1
        revenue1 = revenue + revenue_delta1
        # No impact to costs in this scenario therefore expense delta = 0
        expense_delta1 = 0
        # Error Handling/Input validation for initial round of expense delta
        # calculations
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses
        # Calculate updated profit delta
        profit_delta1 = revenue_delta1 - expense_delta1
        # Calculate scenario's closing profit
        profits1 = revenue1 - expenses1
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta1 = 0
        # Updated Shareholder section of dashboard
        shareholders1 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta1)
        # Impact to customer sentiment of decision path chosen
        customer_delta1 = 0
        # Updated Customer section of dashboard
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        # Impact to employee sentiment of decision path chosen
        employee_delta1 = 0
        # Updated Employee section of dashboard
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue1, revenue_delta1)
        expense_plug = formatting_plug(expenses1, expense_delta1)
        profit_plug = formatting_plug(profits1, profit_delta1)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta1 + customer_delta1 + employee_delta1
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
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
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_1_answer_2, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_1, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        # Revenue increases by €50,000
        revenue_delta1 = 50000
        # Updated revenue stored in variable revenue1
        revenue1 = revenue + revenue_delta1
        # No impact to costs in this scenario therefore expense delta = 0
        expense_delta1 = 0
        # Error Handling/Input validation for initial round of expense delta
        # calculations
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses
        # Calculate updated profit delta
        profit_delta1 = revenue_delta1 - expense_delta1
        # Calculate scenario's closing profit
        profits1 = revenue1 - expenses1
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta1 = 1
        # Updated Shareholder section of dashboard
        shareholders1 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta1)
        # Impact to customer sentiment of decision path chosen
        customer_delta1 = 0
        # Updated Customer section of dashboard
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        # Impact to employee sentiment of decision path chosen
        employee_delta1 = 0
        # Updated Employee section of dashboard
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue1, revenue_delta1)
        expense_plug = formatting_plug(expenses1, expense_delta1)
        profit_plug = formatting_plug(profits1, profit_delta1)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta1 + customer_delta1 + employee_delta1
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
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
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_1_answer_3, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_1, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario\n")
    # Pass on key values (depending on user's chosen decision path) for use as
    # opening balances/figures/dashboards & scores in the next scenario
    return revenue1, revenue_delta1, expenses1, expense_delta1, profits1,\
        profit_delta1, shareholders1, shareholder_delta1, customers1,\
        customer_delta1, employees1, employee_delta1, dashboard_1


def question_2(
    revenue1, revenue_delta1, expenses1, expense_delta1,
        profits1, profit_delta1, shareholders1, shareholder_delta1,
        customers1, customer_delta1, employees1, employee_delta1, dashboard_1):
    """
    Second question game - requires 13x parameters and returns 13x values
    Displays the question & financial/stakeholder dashboard and asks the user
    to choose an answer.

    Based on the answer, the function will display one of three possible
    outcomes, each of which the function will reflect across the financial
    & stakeholder dashboard displays, along with the total cumulative points
    scored

    The function will then return the closing values for each variable to be
    passed on for use as arguments in the subsequent question
    """
    clear()
    # Print opening dashboard, use typewriter effect to enhance UX
    typewriter(dashboard_1, 0.003)
    # Text outlining scenario details for the user stored as string variable:
    scenario_2 = "\n    Scenario 2: You must decide at what level the marketing \n\
    budget should be set for the coming year:\n\
    \n    A. Increase Marketing Expenditure \n\
    B. Maintain Marketing Expenditure \n\
    C. Decrease Marketing Expenditure \n"
    typewriter(scenario_2, 0.01)
    # Request input from the user - choice between A, B or C
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        # Input validation to ensure no invalid data entered into program
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    # Answers A, B & C stored in strings in 3x variables below:
    scenario_2_answer_1 = "\nYou have chosen Option A\
    \n \n\
    - Increasing the Marketing Budget by ~5% has resulted in an increase in \n\
    projected units sold, with increasing customer interest\n\
    - Yearly Revenue projected increases run ahead of equivalent expenditure\n\
    increase projections\n\
    - Profit projections have increased as a result\n"
    scenario_2_answer_2 = "\nYou have chosen Option B\
    \n \n\
    - Retaining current marketing expenditure levels has resulted in flat\n\
    projected unit sales\n\
    - Yearly Revenue projections remain unchanged as a result\n\
    - With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_2_answer_3 = "\nYou have chosen Option C\
    \n \n\
    - Decreasing the Marketing Budget has resulted in decreased projected\n\
    units sold, with customers choosing competitor alternatives\n\
    - Yearly Revenue projection decreases outstrip expenditure reduction\n\
    projections\n\
    - Profit projections have decreased as a result\n"
    # Code dealing with Decision Path "A"
    if input1 == "A":
        # Revenue increases by €100,000
        revenue_delta2 = 100000
        # Updated revenue stored in variable revenue2
        revenue2 = revenue1 + revenue_delta2
        # Costs impacts driving expensedelta2 of €50,000
        expense_delta2 = 50000
        # Calculate updated expenses2
        expenses2 = expenses1 + expense_delta2
        # Calculate updated profit delta
        profit_delta2 = revenue_delta2 - expense_delta2
        # Calculate scenario's closing profit
        profits2 = revenue2 - expenses2
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta2 = shareholder_delta1 + 1
        # Updated Shareholder section of dashboard
        shareholders2 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta2)
        # Impact to customer sentiment of decision path chosen
        customer_delta2 = customer_delta1 + 1
        # Updated Customer section of dashboard
        customers2 = "Customers:         " + emoji_assignment(customer_delta2)
        # Impact to employee sentiment of decision path chosen
        employee_delta2 = 0
        # Updated Employee section of dashboard
        employees2 = "Employees:         " + emoji_assignment(employee_delta2)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue2, revenue_delta2)
        expense_plug = formatting_plug(expenses2, expense_delta2)
        profit_plug = formatting_plug(profits2, profit_delta2)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta2 + customer_delta2 + employee_delta2
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
        dashboard_2 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue2} €{revenue_delta2}{revenue_plug}|   {shareholders2}\
  {shareholder_delta2}    \n\
    Expenses:  €{expenses2} €{expense_delta2}{expense_plug}|   {customers2}\
  {customer_delta2}    \n\
    Profits:   €{profits2} €{profit_delta2}{profit_plug}|   {employees2}\
  {employee_delta2}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_2_answer_1, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_2, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "B":
        # No impact to revenue therefore revenue delta = 0
        revenue_delta2 = 0
        # Updated revenue stored in variable revenue2
        revenue2 = revenue1 + revenue_delta2
        # No impact to costs in this scenario therefore expense delta = 0
        expense_delta2 = 0
        # Calculate updated expenses2
        expenses2 = expenses1 + expense_delta2
        # Calculate updated profit delta
        profit_delta2 = revenue_delta2 - expense_delta2
        # Calculate scenario's closing profit
        profits2 = revenue2 - expenses2
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta2 = shareholder_delta1 + 0
        # Updated Shareholder section of dashboard
        shareholders2 = shareholders1
        # Impact to customer sentiment of decision path chosen
        customer_delta2 = customer_delta1 + 0
        # Updated Customer section of dashboard
        customers2 = customers1
        # Impact to employee sentiment of decision path chosen
        employee_delta2 = 0
        # Updated Employee section of dashboard
        employees2 = employees1
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue2, revenue_delta2)
        expense_plug = formatting_plug(expenses2, expense_delta2)
        profit_plug = formatting_plug(profits2, profit_delta2)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta2 + customer_delta2 + employee_delta2
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
        dashboard_2 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue2} €{revenue_delta2}{revenue_plug}|   {shareholders2}\
  {shareholder_delta2}    \n\
    Expenses:  €{expenses2} €{expense_delta2}{expense_plug}|   {customers2}\
  {customer_delta2}    \n\
    Profits:   €{profits2} €{profit_delta2}{profit_plug}|   {employees2}\
  {employee_delta2}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_2_answer_2, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_2, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        # Revenue decreases by €50,000
        revenue_delta2 = -50000
        # Updated revenue stored in variable revenue2
        revenue2 = revenue1 + revenue_delta2
        # Costs impact in this scenario is negative €50,000
        expense_delta2 = -50000
        # Calculate updated expenses2
        expenses2 = expenses1 + expense_delta2
        # Calculate updated profit delta
        profit_delta2 = revenue_delta2 - expense_delta2
        # Calculate scenario's closing profit
        profits2 = revenue2 - expenses2
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta2 = shareholder_delta1 - 1
        # Updated Shareholder section of dashboard
        shareholders2 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta2)
        # Impact to customer sentiment of decision path chosen
        customer_delta2 = customer_delta1 - 1
        # Updated Customer section of dashboard
        customers2 = "Customers:         " + emoji_assignment(customer_delta2)
        # Impact to employee sentiment of decision path chosen
        employee_delta2 = 0
        # Updated Employee section of dashboard
        employees2 = "Employees:         " + emoji_assignment(employee_delta2)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue2, revenue_delta2)
        expense_plug = formatting_plug(expenses2, expense_delta2)
        profit_plug = formatting_plug(profits2, profit_delta2)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta2 + customer_delta2 + employee_delta2
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
        dashboard_2 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue2} €{revenue_delta2}{revenue_plug}|   {shareholders2}\
  {shareholder_delta2}    \n\
    Expenses:  €{expenses2} €{expense_delta2}{expense_plug}|   {customers2}\
  {customer_delta2}    \n\
    Profits:   €{profits2} €{profit_delta2}{profit_plug}|   {employees2}\
  {employee_delta2}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_2_answer_3, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_2, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")
    # Pass on key values (depending on user's chosen decision path) for use as
    # opening balances/figures/dashboards & scores in the next scenario
    return revenue2, revenue_delta2, expenses2, expense_delta2, profits2,\
        profit_delta2, shareholders2, shareholder_delta2, customers2,\
        customer_delta2, employees2, employee_delta2, dashboard_2


def question_3(
    revenue2, revenue_delta2, expenses2, expense_delta2,
        profits2, profit_delta2, shareholders2, shareholder_delta2,
        customers2, customer_delta2, employees2, employee_delta2, dashboard_2):
    """
    Third question of the game - requires 13x parameters and returns 13x values
    Displays the question & financial/stakeholder dashboard and asks the user
    to choose an answer.

    Based on the answer, the function will display one of three possible
    outcomes, each of which the function will reflect across the financial
    & stakeholder dashboard displays, along with the total cumulative points
    scored

    The function will then return the closing values for each variable to be
    passed on for use as arguments in the subsequent question
    """
    clear()
    # Print opening dashboard, use typewriter effect to enhance UX
    typewriter(dashboard_2, 0.003)
    # Text outlining scenario details for the user stored as string variable:
    scenario_3 = "\n    Scenario 3: You must Choose the new material supplier rate \n\
    for the coming year:\n\
    \n    A. Premium rate - Increase Expenditure \n\
    B. Maintain Rate - Maintain Expenditure \n\
    C. Low Cost Rate - Decrease Expenditure \n"
    typewriter(scenario_3, 0.01)
    # Request input from the user - choice between A, B or C
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        # Input validation to ensure no invalid data entered into program
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    # Answers A, B & C stored in strings in 3x variables below:
    scenario_3_answer_1 = "\nYou have chosen Option A\
    \n \n\
    - Increasing the Material Supplier rate by ~5% has resulted in increased\n\
    material quality and cost, without increasing units sold\n\
    - Yearly Revenue projections are unchanged, whilst expense projections\n\
    have slightly increased\n\
    - Profit projections have slightly decreased for the year as a result\n"
    scenario_3_answer_2 = "\nYou have chosen Option B\
    \n \n\
    - Retaining current material supply rates has resulted in flat projected\n\
    unit costs and unit sales\n\
    - Yearly Revenue projections remain unchanged as a result\n\
    - With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_3_answer_3 = "\nYou have chosen Option C\
    \n \n\
    - Decreasing the material supply rate has resulted in a decrease in\n\
    projected unit costs\n\
    - Yearly Revenue projections are unchanged, however cost projections \n\
    have decreased\n\
    - Profit projections for the year have improved as a result\n"
    # Code dealing with Decision Path "A"
    if input1 == "A":
        # No change to revenue
        revenue_delta3 = 0
        # Updated revenue stored in variable revenue2
        revenue3 = revenue2 + revenue_delta2
        # Costs impacts driving expensedelta3 of €50,000
        expense_delta3 = 50000
        # Calculate updated expenses3
        expenses3 = expenses2 + expense_delta3
        # Calculate updated profit delta
        profit_delta3 = revenue_delta3 - expense_delta3
        # Calculate scenario's closing profit
        profits3 = revenue3 - expenses3
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta3 = shareholder_delta2 + 0
        # Updated Shareholder section of dashboard
        shareholders3 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta3)
            # Impact to customer sentiment of decision path chosen
        customer_delta3 = customer_delta2 + 1
        # Updated Customer section of dashboard
        customers3 = "Customers:         " + emoji_assignment(customer_delta3)
        # Impact to employee sentiment of decision path chosen
        employee_delta3 = employee_delta2 + 1
        # Updated Employee section of dashboard
        employees3 = "Employees:         " + emoji_assignment(employee_delta3)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue3, revenue_delta3)
        expense_plug = formatting_plug(expenses3, expense_delta3)
        profit_plug = formatting_plug(profits3, profit_delta3)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta3 + customer_delta3 + employee_delta3
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
        dashboard_3 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue3} €{revenue_delta3}{revenue_plug}|   {shareholders3}\
  {shareholder_delta3}    \n\
    Expenses:  €{expenses3} €{expense_delta3}{expense_plug}|   {customers3}\
  {customer_delta3}    \n\
    Profits:   €{profits3} €{profit_delta3}{profit_plug}|   {employees3}\
  {employee_delta3}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_3_answer_1, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_3, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "B":
        # No impact to revenue therefore revenue delta = 0
        revenue_delta3 = 0
        # Updated revenue stored in variable revenue2
        revenue3 = revenue2 + revenue_delta2
        # No impact to costs in this scenario therefore expense delta = 0
        expense_delta3 = 0
        # Calculate updated expenses2
        expenses3 = expenses2 + expense_delta3
        # Calculate updated profit delta
        profit_delta3 = revenue_delta3 - expense_delta3
        # Calculate scenario's closing profit
        profits3 = revenue3 - expenses3
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta3 = shareholder_delta2 + 0
        # Updated Shareholder section of dashboard
        shareholders3 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta3)
        # Impact to customer sentiment of decision path chosen
        customer_delta3 = customer_delta2 + 0
        # Updated Customer section of dashboard
        customers3 = "Customers:         " + emoji_assignment(customer_delta3)
        # Impact to employee sentiment of decision path chosen
        employee_delta3 = employee_delta2 + 0
        # Updated Employee section of dashboard
        employees3 = "Employees:         " + emoji_assignment(employee_delta3)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue3, revenue_delta3)
        expense_plug = formatting_plug(expenses3, expense_delta3)
        profit_plug = formatting_plug(profits3, profit_delta3)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta3 + customer_delta3 + employee_delta3
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
        dashboard_3 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue3} €{revenue_delta3}{revenue_plug}|   {shareholders3}\
  {shareholder_delta3}    \n\
    Expenses:  €{expenses3} €{expense_delta3}{expense_plug}|   {customers3}\
  {customer_delta3}    \n\
    Profits:   €{profits3} €{profit_delta3}{profit_plug}|   {employees3}\
  {employee_delta3}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_3_answer_2, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_3, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        # No change to revenue
        revenue_delta3 = 0
        # Updated revenue stored in variable revenue2
        revenue3 = revenue2 + revenue_delta2
        # Costs impact in this scenario is negative €50,000
        expense_delta3 = -50000
        # Calculate updated expenses2
        expenses3 = expenses2 + expense_delta3
        # Calculate updated profit delta
        profit_delta3 = revenue_delta3 - expense_delta3
        # Calculate scenario's closing profit
        profits3 = revenue3 - expenses3
        # Impact to shareholder sentiment of decision path chosen
        shareholder_delta3 = shareholder_delta2 + 1
        # Updated Shareholder section of dashboard
        shareholders3 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta3)
        # Impact to customer sentiment of decision path chosen
        customer_delta3 = customer_delta2 + -1
        # Updated Customer section of dashboard
        customers3 = "Customers:         " + emoji_assignment(customer_delta3)
        # Impact to employee sentiment of decision path chosen
        employee_delta3 = employee_delta2 + 0
        # Updated Employee section of dashboard
        employees3 = "Employees:         " + emoji_assignment(employee_delta3)
        # Plugs to visually align the revenue, expenses & profits in
        # dashboard displays for terminal width ensuring consistency
        # of formatting
        revenue_plug = formatting_plug(revenue3, revenue_delta3)
        expense_plug = formatting_plug(expenses3, expense_delta3)
        profit_plug = formatting_plug(profits3, profit_delta3)
        # Points calculation to be displayed in scenario's closing dashboard
        # And to be carried forward as opening points for subsequent scenario
        points = shareholder_delta3 + customer_delta3 + employee_delta3
        # Updated dashboard/closing dashboard for current scenario
        # Reflects the impact of user's chosen decision on financials &
        # stakeholder sentiment - stored in variable below
        dashboard_3 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue3} €{revenue_delta3}{revenue_plug}|   {shareholders3}\
  {shareholder_delta3}    \n\
    Expenses:  €{expenses3} €{expense_delta3}{expense_plug}|   {customers3}\
  {customer_delta3}    \n\
    Profits:   €{profits3} €{profit_delta3}{profit_plug}|   {employees3}\
  {employee_delta3}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        # Clear display for formatting purposes
        clear()
        # Display to the user the explanation of the impacts of their chosen
        # decision path using typewriter method to enhance UX
        typewriter(scenario_3_answer_3, 0.01)
        # Also display updated/closing dashboard with scenario results
        typewriter(dashboard_3, 0.003)
        # Request user to press the enter key to proceed to next scenario when
        # ready
        input("\nPress Enter To Proceed to Next Scenario")
    # Pass on key values (depending on user's chosen decision path) for use as
    # opening balances/figures/dashboards & scores in the next scenario
    return revenue3, revenue_delta3, expenses3, expense_delta3, profits3,\
        profit_delta3, shareholders3, shareholder_delta3, customers3,\
        customer_delta3, employees3, employee_delta3, dashboard_3


def question_4(
    revenue3, revenue_delta3, expenses3, expense_delta3, profits3,
        profit_delta3, shareholders3, shareholder_delta3, customers3,
        customer_delta3, employees3, employee_delta3, dashboard_3):
    """
    Fourth question of game - requires 13x parameters and returns 13x values
    Displays the question & financial/stakeholder dashboard and asks the user
    to choose an answer.

    Based on the answer, the function will display one of three possible
    outcomes, each of which the function will reflect across the financial
    & stakeholder dashboard displays, along with the total cumulative points
    scored

    The function will then return the closing values for each variable to be
    passed on for use as arguments in the subsequent question
    """
    clear()
    typewriter(dashboard_3, 0.003)
    scenario_4 = "\n    Scenario 4: You must now help set the employee payroll budget \n\
    for the coming year:\n\
    \n    A. Increase Payroll Budget (Increasing Expenditure) \n\
    B. Maintain Payroll Budget - (Maintaining Expenditure) \n\
    C. Reduce Payroll Budget - (Decreasing Expenditure) \n"
    typewriter(scenario_4, 0.01)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_4_answer_1 = "\nYou have chosen Option A\
    \n \n\
    - Increasing the payroll budget has resulted in an increase in yearly\n\
    expenditure projections, without increasing units sold\n\
    - Yearly Revenue projections are unchanged, whilst expense projections\n\
    have slightly increased\n\
    - Profit projections have slightly decreased for the year as a result\n"
    scenario_4_answer_2 = "\nYou have chosen Option B\
    \n \n\
    - Retaining current employee payroll budget has resulted in flat\n\
    projected unit costs\n\
    - Yearly Revenue projections remain unchanged\n\
    - With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_4_answer_3 = "\nYou have chosen Option C\
    \n \n\
    - Decreasing the employee payroll budget has resulted in a decrease in\n\
    projected unit costs\n\
    - Yearly Revenue projections are unchanged, however cost projections \n\
    have decreased\n\
    - Profit projections for the year have improved as a result - however -\n\
    your employees are not happy!\n"

    if input1 == "A":
        revenue_delta4 = 0
        revenue4 = revenue3 + revenue_delta4
        expense_delta4 = 50000
        expenses4 = expenses3 + expense_delta4
        profit_delta4 = revenue_delta4 - expense_delta4
        profits4 = revenue4 - expenses4
        shareholder_delta4 = shareholder_delta3 - 1
        shareholders4 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta4)
        customer_delta4 = customer_delta3 + 0
        customers4 = "Customers:         " + emoji_assignment(customer_delta4)
        employee_delta4 = employee_delta3 + 2
        employees4 = "Employees:         " + emoji_assignment(employee_delta4)
        revenue_plug = formatting_plug(revenue4, revenue_delta4)
        expense_plug = formatting_plug(expenses4, expense_delta4)
        profit_plug = formatting_plug(profits4, profit_delta4)
        points = shareholder_delta4 + customer_delta4 + employee_delta4
        dashboard_4 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue4} €{revenue_delta4}{revenue_plug}|   {shareholders4}\
  {shareholder_delta4}    \n\
    Expenses:  €{expenses4} €{expense_delta4}{expense_plug}|   {customers4}\
  {customer_delta4}    \n\
    Profits:   €{profits4} €{profit_delta4}{profit_plug}|   {employees4}\
  {employee_delta4}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_4_answer_1, 0.01)
        typewriter(dashboard_4, 0.003)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "B":
        revenue_delta4 = 0
        revenue4 = revenue3 + revenue_delta4
        expense_delta4 = 0
        expenses4 = expenses3 + expense_delta4
        profit_delta4 = revenue_delta4 - expense_delta4
        profits4 = revenue4 - expenses4
        shareholder_delta4 = shareholder_delta3 + 0
        shareholders4 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta4)
        customer_delta4 = customer_delta3 + 0
        customers4 = "Customers:         " + emoji_assignment(customer_delta4)
        employee_delta4 = employee_delta3 + 0
        employees4 = "Employees:         " + emoji_assignment(employee_delta4)
        revenue_plug = formatting_plug(revenue4, revenue_delta4)
        expense_plug = formatting_plug(expenses4, expense_delta4)
        profit_plug = formatting_plug(profits4, profit_delta4)
        points = shareholder_delta4 + customer_delta4 + employee_delta4
        dashboard_4 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue4} €{revenue_delta4}{revenue_plug}|   {shareholders4}\
  {shareholder_delta4}    \n\
    Expenses:  €{expenses4} €{expense_delta4}{expense_plug}|   {customers4}\
  {customer_delta4}    \n\
    Profits:   €{profits4} €{profit_delta4}{profit_plug}|   {employees4}\
  {employee_delta4}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_4_answer_2, 0.01)
        typewriter(dashboard_4, 0.003)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta4 = 0
        revenue4 = revenue3 + revenue_delta4
        expense_delta4 = -50000
        expenses4 = expenses3 + expense_delta4
        profit_delta4 = revenue_delta4 - expense_delta4
        profits4 = revenue4 - expenses4
        shareholder_delta4 = shareholder_delta3 + 1
        shareholders4 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta4)
        customer_delta4 = customer_delta3 + 0
        customers4 = "Customers:         " + emoji_assignment(customer_delta4)
        employee_delta4 = employee_delta3 - 2
        employees4 = "Employees:         " + emoji_assignment(employee_delta4)
        revenue_plug = formatting_plug(revenue4, revenue_delta4)
        expense_plug = formatting_plug(expenses4, expense_delta4)
        profit_plug = formatting_plug(profits4, profit_delta4)
        points = shareholder_delta4 + customer_delta4 + employee_delta4
        dashboard_4 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue4} €{revenue_delta4}{revenue_plug}|   {shareholders4}\
  {shareholder_delta4}    \n\
    Expenses:  €{expenses4} €{expense_delta4}{expense_plug}|   {customers4}\
  {customer_delta4}    \n\
    Profits:   €{profits4} €{profit_delta4}{profit_plug}|   {employees4}\
  {employee_delta4}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_4_answer_3, 0.01)
        typewriter(dashboard_4, 0.003)
        input("\nPress Enter To Proceed to Next Scenario")

    return revenue4, revenue_delta4, expenses4, expense_delta4, profits4,\
        profit_delta4, shareholders4, shareholder_delta4, customers4,\
        customer_delta4, employees4, employee_delta4, dashboard_4


def question_5(
    revenue4, revenue_delta4, expenses4, expense_delta4, profits4,
        profit_delta4, shareholders4, shareholder_delta4, customers4,
        customer_delta4, employees4, employee_delta4, dashboard_4):
    """
    Final question of the game - requires 13x parameters and returns 13x values
    Displays the question & financial/stakeholder dashboard and asks the user
    to choose an answer.

    Based on the answer, the function will display one of three possible
    outcomes, each of which the function will reflect across the financial
    & stakeholder dashboard displays, along with the total cumulative points
    scored

    The function will then return the closing values for each variable and will
    also display to the user their final score
    """
    clear()
    typewriter(dashboard_4, 0.003)
    scenario_5 = "\n    Scenario 5: You must now choose a 'Workplace Improvement Strategy'\n\
    expenditure level for the coming year:\n\
    \n    A. Increase (Increasing Expenditure) \n\
    B. Maintain - (Maintaining Expenditure) \n\
    C. Reduce - (Decreasing Expenditure) \n"
    typewriter(scenario_5, 0.01)
    while True:
        input1 = input("\n    Please select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_5_answer_1 = "\nYou have chosen Option A\
    \n \n\
    - Increasing the Workplace Improvement budget results in an increase\n\
    in yearly expenditure projections, without increasing units sold\n\
    - Yearly Revenue projections are unchanged, whilst expense projections\n\
    have slightly increased\n\
    - Profit projections have slightly decreased for the year as a result\n"
    scenario_5_answer_2 = "\nYou have chosen Option B\
    \n \n\
    - Retaining the current Workplace Improvement budget has resulted in\n\
    flat projected unit costs\n\
    - Yearly Revenue projections remain unchanged\n\
    - With expenditure forecasts unchanged, Profit projections remain static\n"
    scenario_5_answer_3 = "\nYou have chosen Option C\
    \n \n\
    - Decreasing the Workplace Improvement budget has resulted in a decrease\n\
    in projected unit costs\n\
    - Yearly Revenue projections are unchanged, however cost projections\n\
    have decreased\n\
    - Profit projections for the year have improved as a result, however -\n\
    employees are not happy!\n"

    if input1 == "A":
        revenue_delta5 = 0
        revenue5 = revenue4 + revenue_delta5
        expense_delta5 = 50000
        expenses5 = expenses4 + expense_delta5
        profit_delta5 = revenue_delta5 - expense_delta5
        profits5 = revenue5 - expenses5
        shareholder_delta5 = shareholder_delta4 - 1
        shareholders5 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 + 2
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5)
        expense_plug = formatting_plug(expenses5, expense_delta5)
        profit_plug = formatting_plug(profits5, profit_delta5)
        points = shareholder_delta5 + customer_delta5 + employee_delta5
        dashboard_5 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue5} €{revenue_delta5}{revenue_plug}|   {shareholders5}\
  {shareholder_delta5}    \n\
    Expenses:  €{expenses5} €{expense_delta5}{expense_plug}|   {customers5}\
  {customer_delta5}    \n\
    Profits:   €{profits5} €{profit_delta5}{profit_plug}|   {employees5}\
  {employee_delta5}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_5_answer_1, 0.01)
        typewriter(dashboard_5, 0.003)
        final = \
            final_score(shareholder_delta5, customer_delta5, employee_delta5)
        print(f"\nThis completes the final scenario - you have scored {final}")
        sleep(0.5)

    elif input1 == "B":
        revenue_delta5 = 0
        revenue5 = revenue + revenue_delta5
        expense_delta5 = 0
        expenses5 = expenses4 + expense_delta5
        profit_delta5 = revenue_delta5 - expense_delta5
        profits5 = revenue5 - expenses5
        shareholder_delta5 = shareholder_delta4 + 0
        shareholders5 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 + 0
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5)
        expense_plug = formatting_plug(expenses5, expense_delta5)
        profit_plug = formatting_plug(profits5, profit_delta5)
        points = shareholder_delta5 + customer_delta5 + employee_delta5
        dashboard_5 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue5} €{revenue_delta5}{revenue_plug}|   {shareholders5}\
  {shareholder_delta5}    \n\
    Expenses:  €{expenses5} €{expense_delta5}{expense_plug}|   {customers5}\
  {customer_delta5}    \n\
    Profits:   €{profits5} €{profit_delta5}{profit_plug}|   {employees5}\
  {employee_delta5}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_5_answer_2, 0.01)
        typewriter(dashboard_5, 0.003)
        final = \
            final_score(shareholder_delta5, customer_delta5, employee_delta5)
        print(f"\nThis completes the final scenario - you have scored {final}")
        sleep(0.5)

    elif input1 == "C":
        revenue_delta5 = 0
        revenue5 = revenue4 + revenue_delta5
        expense_delta5 = -50000
        expenses5 = expenses4 + expense_delta5
        profit_delta5 = revenue_delta5 - expense_delta5
        profits5 = revenue5 - expenses5
        shareholder_delta5 = shareholder_delta4 + 1
        shareholders5 = \
            "Shareholders:      " + emoji_assignment(shareholder_delta5)
        customer_delta5 = customer_delta4 + 0
        customers5 = "Customers:         " + emoji_assignment(customer_delta5)
        employee_delta5 = employee_delta4 - 2
        employees5 = "Employees:         " + emoji_assignment(employee_delta5)
        revenue_plug = formatting_plug(revenue5, revenue_delta5)
        expense_plug = formatting_plug(expenses5, expense_delta5)
        profit_plug = formatting_plug(profits5, profit_delta5)
        points = shareholder_delta5 + customer_delta5 + employee_delta5
        dashboard_5 = f"\n    ------------------------------------------------------------\n\
    Financial Projections:      |    Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:   €{revenue5} €{revenue_delta5}{revenue_plug}|   {shareholders5}\
  {shareholder_delta5}    \n\
    Expenses:  €{expenses5} €{expense_delta5}{expense_plug}|   {customers5}\
  {customer_delta5}    \n\
    Profits:   €{profits5} €{profit_delta5}{profit_plug}|   {employees5}\
  {employee_delta5}    \n\
    ------------------------------------------------------------\n\
                                            Total Points: {points}\n"
        clear()
        typewriter(scenario_5_answer_3, 0.01)
        typewriter(dashboard_5, 0.003)
        final = \
            final_score(shareholder_delta5, customer_delta5, employee_delta5)
        print(f"\nThis completes the final scenario - you have scored {final}")
        sleep(0.5)

    return revenue5, revenue_delta5, expenses5, expense_delta5, profits5,\
        profit_delta5, shareholders5, shareholder_delta5, customers5,\
        customer_delta5, employees5, employee_delta5, dashboard_5


def run_textadv():
    """
    Main function containing questions for game execution
    Sequenced to ensure the correct parameters and handed over from
    each question function to the next, and returns the final
    status for each of the 3x key stakeholders
    """
    revenue1, revenue_delta1, expenses1, expense_delta1, profits1,\
        profit_delta1, shareholders1, shareholder_delta1, customers1,\
        customer_delta1, employees1, employee_delta1, dashboard_1\
        = question_1(
            revenue, revenue_delta, expenses, expense_delta,
            profits, profit_delta, shareholders, shareholder_delta,
            customers, customer_delta, employees, employee_delta, dashboard_0)
    revenue2, revenue_delta2, expenses2, expense_delta2, profits2,\
        profit_delta2, shareholders2, shareholder_delta2, customers2,\
        customer_delta2, employees2, employee_delta2, dashboard_2\
        = question_2(
            revenue1, revenue_delta1, expenses1, expense_delta1,
            profits1, profit_delta1, shareholders1, shareholder_delta1,
            customers1, customer_delta1, employees1, employee_delta1,
            dashboard_1)
    revenue3, revenue_delta3, expenses3, expense_delta3, profits3,\
        profit_delta3, shareholders3, shareholder_delta3, customers3,\
        customer_delta3, employees3, employee_delta3, dashboard_3\
        = question_3(
            revenue2, revenue_delta2, expenses2, expense_delta2,
            profits2, profit_delta2, shareholders2, shareholder_delta2,
            customers2, customer_delta2, employees2, employee_delta2,
            dashboard_2)
    revenue4, revenue_delta4, expenses4, expense_delta4, profits4,\
        profit_delta4, shareholders4, shareholder_delta4, customers4,\
        customer_delta4, employees4, employee_delta4, dashboard_4\
        = question_4(
            revenue3, revenue_delta3, expenses3, expense_delta3,
            profits3, profit_delta3, shareholders3, shareholder_delta3,
            customers3, customer_delta3, employees3, employee_delta3,
            dashboard_3)
    revenue5, revenue_delta5, expenses5, expense_delta5, profits5,\
        profit_delta5, shareholders5, shareholder_delta5, customers5,\
        customer_delta5, employees5, employee_delta5, dashboard_5\
        = question_5(
            revenue4, revenue_delta4, expenses4, expense_delta4,
            profits4, profit_delta4, shareholders4, shareholder_delta4,
            customers4, customer_delta4, employees4, employee_delta4,
            dashboard_4)
    return shareholder_delta5, customer_delta5, employee_delta5


def finish_game():
    """
    Closing game loop triggered post-completion of final question
    Allows the user to either play again, or exit back to the main menu
    """
    loop = True
    while loop:
        print("\nPlease Press E to exit...")
        print("\nOr alternatively - if you wish to try to improve your score,")
        choice = input(f"\nPress any key followed by enter to play again:")
        if choice.upper() == "E":
            print("Goodbye")
            sleep(0.5)
            clear()
            loop = False
        else:
            shareholder_delta5, customer_delta5, employee_delta5 = \
                run_textadv()


# Note: ***Hangman Section of Code Begins here***


def initialise_variables():
    """
    Initialises key variables for use when looping back to re-play the game
    Does not take in any parameters
    Returns 8x key values required to enable core game mechanics
    """
    # Answer bank & Word variables
    # Credits: word_list sourced from Github repository below:
    # https://github.com/Xethron/Hangman/blob/master/words.txt
    # And the method for removing words less than three letters in length
    # was sourced from (https://stackoverflow.com/questions/10150725/
    # beginner-issue-python-how-do-i-remove-words-from-a-list-under
    # -a-certain-leng) article on Stack Overflow
    # Please see readme credits for more detail if required
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
    return word_list, answer, answer_hidden, guesses_remaining, guesses_used,\
        incorrect_guesses, previous_guesses, gallows_stage


def welcome_screen():
    """
    Displays welcome screen to user upon loading
    the application. Allows proceeding to play
    the game upon pressing "Enter"
    """
    clear()
    print("------------------------------------------------------")
    print("|                                                    |")
    print("|                P  Y  T  H  O  N                    |")
    print("|                                                    |")
    print("|                   H  A  N  G  M  A  N              |")
    print("|                    _________                       |")
    print("|                    |       |                       |")
    print("|                    |       O                       |")
    print("|                    |      /|\                      |")
    print("|                    |       |                       |")
    print("|                    |      / \                      |")
    print("|                    |                               |")
    print("|                    |                               |")
    print("|                 ___|___________                    |")
    print("|                 XXXXXXXXXXXXXXX                    |")
    print("|                                                    |")
    print("|               [PRESS ENTER TO BEGIN]               |")
    print("|                                                    |")
    print("------------------------------------------------------")
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


def main_game_screen(
    guesses_used, guesses_remaining, incorrect_guesses, answer_hidden
        ):
        """
        - Builds/Draws the main game screen/board for the user to play on
        - Function will stop after drawing the initial 4x game elements
        if the answer has been guessed, or will add a warning based on the
        number of guesses remaining if the answer is still unguessed
        - Requires 4x parameters to be passed in
        - Does not return any value because it is used for display purposes
        """
        print("".join(answer_hidden))
        print(f"Guesses Used So Far: {guesses_used}")
        print(f"Guesses Remaining: {guesses_remaining}")
        print("".join(previous_guesses) + "\n")
        if not ("_ " in answer_hidden):
            return
        elif guesses_remaining == 1:
            print(f"{bcolors.FAIL}Final attempt!\
            \nOne last chance to guess the word!{bcolors.ENDC}\n")
        elif guesses_remaining == 3 or guesses_remaining == 2:
            print(f"{bcolors.WARNING}Hurry!\
            \nYou only have {guesses_remaining} lives left...{bcolors.ENDC}")
            print(bcolors.WARNING + "Try guessing the word!\n" + bcolors.ENDC)


def validate_guess(previous_guesses, guesses_remaining):
    """
    - Validates the user's guess for data integrity purposes
    in downstream calculations & functions
    - Will allow the user the option to guess the full word
    if guesses remaining is three or less
    - Will ensure any word/letter guesses are not duplicates,
    non-alpha, or of incorrect length
    """
    while True:
        if guesses_remaining <= 3:
            guess_type = input(
                "Press 'W' to guess a word, or 'L' to guess a letter: ")
            guess_type = guess_type.lower()
            if guess_type == "w":
                user_guess = input("\nPlease guess a word: ").lower()
                if len(user_guess) > 1:
                    if user_guess.isalpha():
                        if not ((user_guess + ", ") in previous_guesses):
                            if len(user_guess) == len(answer):
                                return user_guess
                            print(f"Sorry, {user_guess} is {len(user_guess)} \
characters long, but the answer is {len(answer)} characters long, please try\
again")
                            continue
                        print(f"\nSorry, You have already guessed the word \
'{user_guess}', please try again \n")
                        continue
                    print(f"\nSorry, Your guess must be a word, '{user_guess}' \
is not a word, please try again\n")
                    continue
                print(f"Sorry, The Word must not be a single character, \
'{user_guess}' is not valid, please try\n again\n")
            elif guess_type == "l":
                user_guess = input("\nPlease guess a letter: ").lower()
                if len(user_guess) == 1:
                    if user_guess.isalpha():
                        if not ((user_guess + ", ") in previous_guesses):
                            return user_guess
                        print(f"\nSorry, You have already guessed the letter \
'{user_guess}', please try again \n")
                        continue
                    print(f"\nSorry, Your guess must be a letter, \
'{user_guess}' is not a letter, please try again\n")
                    continue
                print(f"\nSorry, Your guess must be a single character \
only, '{user_guess}' is not valid, please try again\n")
            else:
                print(f"Sorry, '{guess_type}' is not a valid input, please \
try again")
        else:
            user_guess = input("\nPlease guess a letter: ").lower()
            if len(user_guess) == 1:
                if user_guess.isalpha():
                    if not ((user_guess + ", ") in previous_guesses):
                        return user_guess
                    print(f"\nSorry, You have already guessed the letter \
'{user_guess}', please try again \n")
                    continue
                print(f"\nSorry, Your guess must be a letter, \
'{user_guess}' is not a letter, please try again\n")
                continue
            print(f"\nSorry, Your Guess must be a single character only, \
'{user_guess}' is not valid, please try again\n")


def reveal_letter_in_answer(user_guess, answer, answer_hidden):
    """
    - Replaces the blanks/underscores representing the unguessed letters of
    the answer with the correct guesses from the user
    - It requires 3x parameters as inputs, and returns the status of the
    answer in terms of guessed/unguessed letters
    """
    if user_guess == answer:
        answer_hidden = ["Guess The Word: ", answer]
    else:
        for index, value in enumerate(answer, start=1):
            if user_guess == value:
                answer_hidden[index] = user_guess

    return answer_hidden

# Credits: the "Sleep" function used throughout my answer_check
# function was sourced from the article below:
# https://www.programiz.com/python-programming/time/sleep
# Please see credits section of readme for further detail


def answer_check(
    user_guess, previous_guesses, gallows_stage, incorrect_guesses,
        guesses_used, answer, answer_hidden, guesses_remaining):
    """
    - checks whether the user's guess is correct (either is a letter
    in the answer, or is a word that matches the answer) or incorrect
    and notifies the user accordingly
    - It requires 8x key parameters as inputs, and returns 8x values
    for use as variables in downstream functions
    """
    previous_guesses.append(user_guess + ", ")
    guesses_used += 1

    if user_guess == answer:
        answer_hidden = \
            reveal_letter_in_answer(user_guess, answer, answer_hidden)
        print(f"\nCorrect! Great guess - '{user_guess}' was the answer!")
        sleep(0.75)
    elif user_guess in answer:
        answer_hidden = \
            reveal_letter_in_answer(user_guess, answer, answer_hidden)
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

    return user_guess, previous_guesses, gallows_stage, incorrect_guesses,\
        guesses_used, answer, answer_hidden, guesses_remaining


def play_game(
    previous_guesses, gallows_stage, incorrect_guesses, guesses_used,
        answer, answer_hidden, guesses_remaining):
    """
    - Main game function: this will display to the user either a "game
    lost" notification if the gallows is fully built resulting from
    8x incorrect guesses, or alternatively a game won notification if
    the "answer_hidden" variable no longer contains any unguessed letters
    - if the game has been neither won, nor lost, the game will still be
    in progress, and in this case the function will run the main game
    mechanics for the player
    - The function requires 7x key parameters as inputs and does not
    return any values
    """
    while "_ " in answer_hidden:
        if gallows_stage == 8:
            clear()
            draw_gallows(gallows_stage)
            answer_hidden = ["Guess The Word: ", answer]
            main_game_screen(
                guesses_used, guesses_remaining, incorrect_guesses,
                answer_hidden)
            print(f"Sorry You Lost - the answer was '{answer}'\n")
            break
        else:
            clear()
            draw_gallows(gallows_stage)
            main_game_screen(
                guesses_used, guesses_remaining, incorrect_guesses,
                answer_hidden)
            user_guess = validate_guess(previous_guesses, guesses_remaining)
            user_guess, previous_guesses, gallows_stage, incorrect_guesses,\
                guesses_used, answer, answer_hidden, guesses_remaining\
                = answer_check(
                    user_guess, previous_guesses, gallows_stage,
                    incorrect_guesses, guesses_used, answer, answer_hidden,
                    guesses_remaining)
            clear()
        draw_gallows(gallows_stage)
        main_game_screen(
            guesses_used, guesses_remaining, incorrect_guesses,
            answer_hidden)

        if not ("_ " in answer_hidden):
            clear()
            draw_gallows(gallows_stage)
            main_game_screen(
                guesses_used, guesses_remaining, incorrect_guesses,
                answer_hidden)
            print(f"Congratulations You Won - the answer was '{answer}'\n")
            sleep(0.75)


# Main application loop - this will display the opening welcome screen
# and progress into the "select game" screen allowing the user to choose
# which game to play, or to exit the application

print("--------------------------------------------")
print("|                                          |")
print(bcolors.WARNING + "|    W  E  L  C  O  M  E                   |" +
      bcolors.ENDC)
print("|                                          |")
print("|       T O                                |")
print("|                                          |")
print(bcolors.FAIL + "|          P  Y  T  H  O  N                |" +
      bcolors.ENDC)
print("|                                          |")
print("|              G A M E S                   |")
print("|                                          |")
print(bcolors.OKBLUE + "|                 P A C K A G E            |" +
      bcolors.ENDC)
print("|                                          |")
print("|                                          |")
print(bcolors.BOLD + "|         [PRESS ENTER TO BEGIN]           |" +
      bcolors.ENDC)
print("|                                          |")
print("--------------------------------------------")
input()

while True:
    clear()
    print("--------------------------------------------")
    print("|                                          |")
    print("|           *** MAIN MENU ***              |")
    print("|                                          |")
    print("|      PLEASE SELECT A GAME TO PLAY:       |")
    print("|                                          |")
    print("|    A. HANGMAN                            |")
    print("|                                          |")
    print("|    B. FICT-CORP ADVENTURES               |")
    print("|                                          |")
    print("|    C. EXIT APPLICATION                   |")
    print("|                                          |")
    print("|                                          |")
    print("|            [PLEASE SELECT]               |")
    print("|                                          |")
    print("--------------------------------------------")
    game = input("Select option A, B or C: ").lower()
    # Option "A" selection will trigger the Hangman game to load
    # The code below intialises the key variables and runs the game
    if game == "a":
        word_list, answer, answer_hidden, guesses_remaining,\
                    guesses_used, incorrect_guesses, previous_guesses,\
                    gallows_stage = initialise_variables()
        welcome_screen()
        play_game(
            previous_guesses, gallows_stage, incorrect_guesses,
            guesses_used, answer, answer_hidden, guesses_remaining)
        # Game ending sequence - this will give the user the option
        # to either play again, or to exit back to the main menu
        # With input validation to ensure invalid input is handled
        # elegantly as part of defensive design principles
        while True:
            stop_go = input(
                "Please press 'y' to play again, or press 'e' to exit: "
                ).lower()
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
                print(f"\n'{stop_go}' is an invalid choice\n")
    # Option "B" selection will trigger the FictCorp Adventures game
    # The code below intialises the key variables and runs the game
    elif game == "b":
        # Clear terminal for formatting purposes
        clear()
        # Set intial revenue value & store in variable "revenue"
        revenue = 1000000
        # Set initial revenue delta as an empty string for display purposes
        revenue_delta = "     "
        # Set intial Expenses value & store in variable "expenses"
        expenses = 700000
        # Set initial expenses delta as an empty string for display purposes
        expense_delta = "     "
        # Set initial profit as revenue less expenses & store in variable:
        profits = revenue - expenses
        # Initial profits delta set to blank string for display purposes
        profit_delta = "     "
        # Initial values for each stakeholder & their sentiment level below:
        shareholders = "Shareholders:      😐"
        shareholder_delta = "  "
        customers = "Customers:         😐"
        customer_delta = "  "
        employees = "Employees:         😐"
        employee_delta = "  "
        # Initial/Opening dashboard created & stored in variable "dashboard_0"
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
        # Introductory text & instructions/game objectives
        # Stored in variable below
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
        \nbelow: "
        # Display the FictCorp Adventures opening screen
        main_menu()
        # Use the typewriter effect to present to the user the opening texts
        typewriter(intro, 0.01)
        # Use typewriter effect to display opening dashboard
        typewriter(dashboard_0, 0.003)
        # Request the user to press enter to begin when they are ready
        input("\n[Press Enter To Begin]")
        # Run the game function for the user
        shareholder_delta5, customer_delta5, employee_delta5 = run_textadv()
        # Run the finish_game function to end the game for the user
        finish_game()
    # Option C will trigger the closure of the application & exit for the user
    elif game == "c":
        print("Goodbye")
        break
    # Input validation to ensure invalid data entry is dealt with elegantly as
    # part of defensive design principles
    else:
        print(bcolors.FAIL + "Please enter a valid input - A, B or C" +
              bcolors.ENDC)
        sleep(1)
        clear()
