#Capstone Project1 - Investment & Bond Calculator - Cian - 13/10/2026 - version 1.0

# Key new terms for this task, adding to my "py-ble"
# N.B. glossary

# ELSE IF (ELSE IF in pseudo but elif in PY)= Check something else, but only if the IF above it was false
# ELSE = Do this if none of the checks above were true
# END IF (no py term needed, just indent)= That's the end of the checking
# IMPORT = Bring in extra tools in this casee math so I can use them
# LOWERCASE = Turn text into small letters, so "Bond", "BOND" and "bond" all count as the same
# TO THE POWER OF = **

# 1) Choose the calculator problem:

#         START
#         IMPORT math
#         OUTPUT menu (investment = interest you'll earn, bond = home loan repayment)
#         INPUT calculation_choice
#         SET calculation_choice = calculation_choice in LOWERCASE (Because capitals shouldn't matter)

#         IF calculation_choice = "investment"
#             do problem 2
#         ELSE IF calculation_choice = "bond"
#             do problem 3
#         ELSE
#             OUTPUT error message (not a valid choice)
#         END IF
#         STOP

# ***

# 2) Investment calculator problem (run if the choice was investment):

#         START
#         INPUT deposit_amount
#         INPUT interest_rate 
#         INPUT years_investing
#         INPUT interest ("simple" or "compound")
#         SET interest = interest in LOWERCASE
#         SET rate_as_decimal = interest_rate / 100 (Because the formula needs 0.08, not 8)

#         IF interest = "simple"
#             SET total_amount = deposit_amount x (1 + rate_as_decimal x years_investing)
#             OUTPUT total_amount
#         ELSE IF interest = "compound"
#             SET total_amount = deposit_amount x (1 + rate_as_decimal) TO THE POWER OF years_investing
#             OUTPUT total_amount
#         ELSE
#             OUTPUT error message (needs to be simple or compound)
#         END IF
#         STOP

# ***

# 3) Bond calculator problem (run if the choice was bond):
#         START
#         INPUT house_value
#         INPUT annual_interest_rate (just the number, e.g. 7)
#         INPUT months_to_repay
#         SET monthly_rate = annual_interest_rate / 100 / 12 (Because a bond is paid monthly, so the yearly rate gets split into 12)
#         SET monthly_repayment = (monthly_rate x house_value) / (1 - (1 + monthly_rate) TO THE POWER OF minus months_to_repay)
#         OUTPUT monthly_repayment
#         STOP

# finance_calculators.py
# Two calculators: investment (simple or compound interest) and bond (monthly home loan repayment)

import math

# Show the menu
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")
print()

# .lower() so that "Bond", "BOND" and "bond" all count as the same choice
calculation_choice = input('Enter either "investment" or "bond" from the menu above to proceed: ').lower()
print()

if calculation_choice == "investment":
    deposit_amount = float(input("Amount of money you are depositing: "))
    interest_rate = float(input("Interest rate (just the number, e.g. 8 for 8%): "))
    years_investing = int(input("Number of years you plan on investing: "))
    interest = input('Type "simple" or "compound" interest: ').lower()
    print()

    # Turn the percentage into a decimal, e.g. 8 becomes 0.08
    rate_as_decimal = interest_rate / 100

    if interest == "simple":
        total_amount = deposit_amount * (1 + rate_as_decimal * years_investing)
        print(f"Total amount after {years_investing} years (simple interest): {total_amount:.2f}")

    elif interest == "compound":
        total_amount = deposit_amount * math.pow((1 + rate_as_decimal), years_investing)
        print(f"Total amount after {years_investing} years (compound interest): {total_amount:.2f}")

    else:
        print('Error: interest must be either "simple" or "compound".')

elif calculation_choice == "bond":
    house_value = float(input("Present value of the house: "))
    annual_interest_rate = float(input("Interest rate (just the number, e.g. 7 for 7%): "))
    months_to_repay = int(input("Number of months you plan to take to repay the bond: "))
    print()

    # The bond is repaid monthly, so the yearly rate is split into 12
    monthly_rate = (annual_interest_rate / 100) / 12

    monthly_repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months_to_repay))
    print(f"You will need to repay {monthly_repayment:.2f} each month.")

else:
    print('Error: please enter either "investment" or "bond".')
    