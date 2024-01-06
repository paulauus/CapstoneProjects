import math
# Create a program that allows the user to access two different finance calculators:
# an investment calculator and a home loan repayment calculator.

# Output definitions of 'investment' and 'bond' for information.
print("This program will allow you to access two different finance calculators for investments and bonds.\n")
print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond         - to calculate the amount you'll have to pay on a home loan\n")

# The user must choose which calculation they want to proceed with.
selection = input("Enter either 'investment' or 'bond' from the options above to proceed: ")
selection_lower = selection.lower()

# Keep asking the user for input until they enter one of the two options.
while selection_lower != "investment" and selection_lower != "bond":
    selection = input("You have not made a valid selection.\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
    selection_lower = selection.lower()
if selection_lower == "investment" or selection_lower == "bond":
    print(f"You have selected '{selection_lower}'.\n")

# If the user inputs 'investment', proceed to asking for input on investment details.
if selection_lower == "investment":
    print("Please enter your investment details below:")
    deposit_P = input("How much money are you depositing? ")
    rate_r = input("What is your interest rate? ")
    years_t = input("How many years are you investing? ")
    interest = input("Do you want 'simple' or 'compound' interest? ")
    interest_lower = interest.lower()

    # If the user chooses simple interest, proceed with the following formula:
    # A = P * ( 1 + r * t )
    if interest_lower == "simple":
        simple_interest_A = float(deposit_P) * (1 + (float(rate_r)/100) * float(years_t))
        print(f"\nAfter {years_t} years you will get back {round(simple_interest_A, 2)}.\n")

    # If the user chooses compound interest, proceed with the following formula:
    # A = P * m a t h . p o w ( ( 1 + r ) , t )
    elif interest_lower == "compound":
        compound_interest_A = float(deposit_P) * math.pow(1 + (float(rate_r)/100), float(years_t))
        print(f"\nAfter {years_t} years you will get back {round(compound_interest_A, 2)}.\n")

    # If the user does not type 'simple' or 'compound', display an error message.
    else:
        print("Invalid selection. Please start again.")

# If the user inputs 'bond', proceed to asking for input on property details.
elif selection_lower == "bond":
    print("Please enter your home loan details below:")
    house_value_P = input("What is the value of your property? ")
    house_value_number = float(house_value_P)
    annual_interest_i = input("What is the annual interest rate? ")
    monthly_interest_i = float(annual_interest_i)/100
    monthly_interest_number = float(monthly_interest_i)/12
    months_n = input("How many months is the repayment period? ")
    months_number = float(months_n)
    
    # Input values above have been converted to floats to make the bond repayment formula readable:
    # repayment = ( i * P ) / ( 1 - ( 1 + i ) * * ( - n ) )
    monthly_repayment = (monthly_interest_number * house_value_number) / (1 - ( (1 + monthly_interest_number) ** (-months_number) ))
    print (f"\nYou will have to repay {round(monthly_repayment, 2)} each month.\n")