# Description: This program calculates the insurance policy for the customer.
# Author: Adewale Gbadamosi
# Date: March 16, 2024

# importing libraries
import datetime
import sys
import time
import random
import FormatValues as fv

# Open the defaults file and read the values into variables
f = open('Def.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREMIUM_RATE = float(f.readline())
ADDITIONAL_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_RATE = float(f.readline())
GLASS_COVERAGE_RATE = float(f.readline())
LOANER_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

while True: 
    # Function to calculate insurance premium
    def calculatePremium(numOfCar, extraLiability, glassCoverage, optionalLoaner):
        global basicPremium
        global totalExtraCost

        extraLiabilityCost = 0
        glassCoverageCost = 0
        optionalLoanerCost = 0

        basicPremium = BASIC_PREMIUM_RATE + (numOfCar - 1) * BASIC_PREMIUM_RATE * (1 - ADDITIONAL_CAR_DISCOUNT)
        if extraLiability == "Y":
            extraLiabilityCost = numOfCar * EXTRA_LIABILITY_RATE
        if glassCoverage == "Y":
            glassCoverageCost = numOfCar * GLASS_COVERAGE_RATE
        if optionalLoaner == "Y":
            optionalLoanerCost = numOfCar * LOANER_CAR_RATE
        
        totalExtraCost = extraLiabilityCost + glassCoverageCost + optionalLoanerCost
        totalPremium = basicPremium + totalExtraCost
        return totalPremium
    
    # Function to calculate total cost
    def calculateTotalCost(premium):
        global hst
        hst = premium * HST_RATE
        totalCost = premium + hst
        return totalCost
    
    # Function to calculate monthly payment
    def calculateMonthlyPayment(totalCost, paymentOption, downPayment=0):
        if paymentOption == "F":
            return totalCost
        elif paymentOption == "D":
            remainingBalance = totalCost - downPayment
            monthlyPayment = (remainingBalance + PROCESSING_FEE) / 8
            return monthlyPayment
        elif paymentOption == "M":
            monthlyPayment = (totalCost + PROCESSING_FEE) / 8
            return monthlyPayment
        
    # Function to get first day of next month
    def getFirstDayNextMonth():
        today = datetime.datetime.now()
        if today.month < 12:
            nextMonth = today.month + 1 
        else:
            nextMonth = 1

        if today.month == 12:
            nextYear = today.year + 1  
        else:
            nextYear = today.year

        return fv.FDateS(datetime.datetime(nextYear, nextMonth, 1))
    
    # Get current date
    currentDate = fv.FDateS(datetime.datetime.now())

   # Gathering customer information and validations 
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
    while True:
        cusFirstName = input("\nEnter the customer first name:                      ").strip().title()
        if cusFirstName == "":
            print("Invalid Entry: Customer first name cannot be blank.")
        elif set(cusFirstName).issubset(allowed_char) == False:
            print("Invalid Entry - Customer first name contains invalid character.")
        else:
            break

    while True:
        cusLastName = input("Enter the customer last name:                       ").strip().title()
        if cusLastName == "":
            print("Invalid Entry: Customer last name cannot be blank.")
        elif set(cusLastName).issubset(allowed_char) == False:
            print("Invalid Entry - Customer last name contains invalid character.")
        else:
            break

    while True:
        cusAddress = input("Enter the customer address:                         ").strip().title()
        if cusAddress == "":
            print("Invalid Entry: Customer address cannot be blank.")
        else:
            break
    
    while True:
        cusCity = input("Enter the customer's city of residence:             ").strip().title()
        if cusCity == "":
            print("Invalid Entry: Customer's city of residence cannot be blank.")
        elif set(cusCity).issubset(allowed_char) == False:
            print("Invalid Entry - Customer's city of residence contains invalid character.")
        else:
            break

    provinceList = ["AB", "BC", "MB", "NB", "NS", "NL", "NT", "NU", "ON", "PE", "SK", "QC", "YT" ]
    while True:
        cusProvince = input("Enter the customer's province of residence (XX):    ").strip().upper()
        if cusProvince == "":
            print("Invalid Entry: Customer's province of residence cannot be blank.")
        elif cusProvince not in provinceList:
            print("Invalid Entry - Invalid province, please enter of one of the provinces listed: AB, BC, MB, NB, NS, NL, NT, NU, ON, PE, SK, QC, YT.")
        elif len(cusProvince) != 2:
            print("Invalid Entry: Customer's province of residence must be two character.")
        else:
            break
    
    while True:
        postalCode = input("Enter customer postal code (X9X9X9):                ").strip().upper()
        if postalCode == "":
            print("Invalid Entry: Customer's postal code cannot be blank.")
        elif len(postalCode) != 6:
            print("Invalid Entry: Customer's postal must be six characters.")
        else:
            break

    while True:
        phoneNum = input("Enter phone number (9999999999):                    ").strip()
        if phoneNum == "":
            print("Invald Entry - Phone number cannot be blank.")
        elif phoneNum.isdigit() == False:
            print("Invalid Entry - phone number must be digit number.")
        elif len(phoneNum) != 10:
            print("Invalid Entry - phone number must 10 digit number.")
        else:
            break

    while True:
        try:
            numOfCar = int(input("Enter the number of cars for insurance:            "))
        except:
            print("Invalid Entry - number of car is not valid entry.")
        else:
            break

    while True:
        extraLiability = input("Extra liability (Up to $1,000,000): Enter Y for Yes and N for No: ").strip().upper()
        if extraLiability == "":
            print("Invalid Entry - extra liability can not be blank.")
        elif len(extraLiability) != 1:
            print("Invalid Entry - extra liabilty entry must be one letter (Y or N).")
        elif extraLiability != "Y" and extraLiability != "N":
            print("Invalid Entry - extra liabilty must be Y or N.")
        else:
            break

    while True:
        glassCoverage = input("Optional glass coverage: Enter Y for Yes and N for No: ").strip().upper()
        if glassCoverage == "":
            print("Invalid Entry - Optional glass coverage can not be blank.")
        elif len(glassCoverage) != 1:
            print("Invalid Entry - Optional glass coverage entry must be one letter (Y or N).")
        elif glassCoverage != "Y" and  glassCoverage != "N":
            print("Invalid Entry - Optional glass coverage must be Y or N.")
        else:
           break
        
    while True:
        optionalLoaner = input("Optionalloaner: Enter Y for Yes and N for No: ").strip().upper()
        if optionalLoaner == "":
            print("Invalid Entry - Optional glass coverage can not be blank.")
        elif len(optionalLoaner) != 1:
            print("Invalid Entry - Optional glass coverage entry must be one letter (Y or N).")
        elif optionalLoaner != "Y" and  optionalLoaner != "N":
            print("Invalid Entry - Optional glass coverage must be Y or N.")
        else:
           break
    
    paymentOptionList = ["F", "M", "D"]
    while True:
        paymentOption = input("Enter the customer's payment option (F for full, M for monthly payment and D for down payment): ").strip().upper()
        if paymentOption == "":
            print("Invalid Entry: Customer's payment option cannot be blank.")
        elif paymentOption not in paymentOptionList:
            print("Invalid Entry - Invalid payment option, please enter F, M or D.")
        elif len(paymentOption) != 1:
            print("Invalid Entry: Customer's payment option must be F, M or D for full, monthly or down payment respectively.")
        else:
            if paymentOption == "D":
                try:
                    downPayment = float(input("Enter the down playment:                 $"))
                except:
                    print("Invalid Entry - down payment must be numeric")
                else:
                    break
            break
    
    # Input claims and validation
    while True:
        try:
            numClaims = int(input("Number of previous Claims:                  ")) 
        except:
            print("Invalid Entry - number of previous claim is not valid number.")
        else:
            break
    
    claims = []
    for i in range(numClaims):
        while True:
            claimNumber = input(f"Enter Claim {i + 1} Number:                       ")  
            if claimNumber == "":
                print("Invald Entry - claim nmber cannot be blank.")
            elif claimNumber.isdigit() == False:
                print("Invalid Entry - claim number must be digit number.")
            elif len(claimNumber) < 4 or len(claimNumber) > 8:
                print("Invalid Entry - claim number must be between 4 and 8 digit number.")
            else:
                break
        
        while True:
            try:
                claimDate = input(f"Enter Claim {i + 1} Date (YYYY-MM-DD):            ")
                claimDatePT = datetime.datetime.strptime(claimDate, "%Y-%m-%d")  
            except:
                print("Invalid Entry - previous claim date entry is not valid date.")
            else:
                break
        
        while True:
            try:
                claimAmount = float(input(f"Enter Claim {i + 1} Amount:                       $"))  
            except:
                print("Invalid Entry - previous claim amount is not valid amount.")
            else:
                break
        claims.append((claimNumber, claimDate, f"{fv.FDollar2(claimAmount):>10s}"))


    # Calculate insurance premium and total cost
    premium = calculatePremium(numOfCar, extraLiability, glassCoverage, optionalLoaner)

    totalCost = calculateTotalCost(premium)

    if paymentOption == "D":
        monthlyPayment = calculateMonthlyPayment(totalCost, paymentOption, downPayment)
    else:
        monthlyPayment = calculateMonthlyPayment(totalCost, paymentOption)

    cityProvicePostal = cusCity + " " + cusProvince + " " + postalCode
    
    # Display receipt
    print(f"\n")
    print(f"                         One Stop Insurance Company")
    print(f"")
    print(f"Policy No: {POLICY_NUM}                         Invoice Number:     {str(POLICY_NUM)[-3:]}-{numOfCar}-{random.randint(1,8999)+1000}")  # Generating invoice number
    print(f"Insurance Coverage Receipt              Invoice Date:       {currentDate}")
    print(f"                                        First Payment Date: {getFirstDayNextMonth()}")
    print(f"")
    print(f"                                         Extra Liability: {extraLiability}")
    print(f"                                         Glass Coverage:  {glassCoverage}")
    print(f"Sold to:                                 Loaner:          {optionalLoaner}")
    print(f"                                         ----------------------------")
    print(f"     {cusFirstName[0]}. {cusLastName:<26s}       Number of car:            {numOfCar:>2d}")
    print(f"     {cusAddress:<30s}      Basic Premium:     {fv.FDollar2(basicPremium):>9s}")
    print(f"     {cityProvicePostal:<30s}      Total Extra Cost:  {fv.FDollar2(totalExtraCost):>9s}             ")
    print(f"                                         ----------------------------")
    print(f"                                         SubTotal:          {fv.FDollar2(premium):>9s}")
    print(f"                                         HST:               {fv.FDollar2(hst):>9s}")
    print(f"                                         ----------------------------")
    print(f"                                         Total policy cost: {fv.FDollar2(totalCost):>9s}")
    # Only print processing fee if payment method is Monthly or Down Payment
    if paymentOption == "M" or paymentOption == "D":
        print(f"                                         Processing fee:    {fv.FDollar2(PROCESSING_FEE):>9s}")
    print(f"")
    # Display Down payment only when the payment method is D
    if paymentOption == "D":
        print(f"                                         Down Payment:      {fv.FDollar2(downPayment):>9s}")
        print(f"")
    # Display options for payment method. Display full payment when the payment method is F, otherwise display monthly payment
    if paymentOption == "F":
        print(f"                                         ----------------------------")   
        print(f"                                         Full Payment:      {fv.FDollar2(totalCost):>9s}")
        print(f"                                         ----------------------------")
    else:
        print(f"                                         ----------------------------")   
        print(f"                                         Monthly Payment:   {fv.FDollar2(monthlyPayment):>9s}")
        print(f"                                         ----------------------------")
    print(f"")
    print("-----------------------------------------")
    print("Previous Claims:")
    print("Claim #        Claim Date         Amount")
    print("-----------------------------------------")
    for claim in claims:
        print(f"{claim[0]:<15}{claim[1]:<15}{claim[2]}")
    print("-----------------------------------------")


    # Store the policy data into a file called Policy.dat
    for _ in range(5):  # Change to control no. of 'blinks'
        print('Saving policy data ...', end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)

    print()
    print("Claim data successfully saved ...", end='\r')
    time.sleep(1)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns

    f = open("Policy.dat", "a")
    f.write("{}, ".format(POLICY_NUM))
    f.write("{}, ".format(cusFirstName))
    f.write("{}, ".format(cusLastName)) 
    f.write("{}, ".format(cusAddress))
    f.write("{}, ".format(cusCity))
    f.write("{}, ".format(cusProvince))
    f.write("{}, ".format(phoneNum))
    f.write("{}, ".format(postalCode))
    f.write("{}, ".format(str(numOfCar)))
    f.write("{}, ".format(extraLiability))
    f.write("{}, ".format(glassCoverage))
    f.write("{}, ".format(optionalLoaner))
    f.write("{}, ".format(str(numClaims)))
    f.write("{}, ".format(str(currentDate)))
    f.write("{}, ".format(str(getFirstDayNextMonth())))
    f.write("{}, ".format(str(paymentOption)))
    f.write("{}\n".format(str(totalCost)))
    f.close()


    POLICY_NUM += 1  # Increase the next policy number

    f = open('Def.dat', 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREMIUM_RATE)))
    f.write("{}\n".format(str(ADDITIONAL_CAR_DISCOUNT)))
    f.write("{}\n".format(str(EXTRA_LIABILITY_RATE)))
    f.write("{}\n".format(str(GLASS_COVERAGE_RATE)))
    f.write("{}\n".format(str(LOANER_CAR_RATE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROCESSING_FEE)))
    f.close()

    # Ask if the user wants to add another customer
    while True:
        anotherCustomer = input("\nDo you want to enter information for another customer? (Y/N): ").upper()
        if anotherCustomer == "":
            print("Inalid Entry - another customer can not be blank.")
        elif len(anotherCustomer) != 1:
            print("Invalid Entry - enter either Y or N if want o proceed to another customer")
        elif anotherCustomer != "Y" and anotherCustomer != "N":
            print("Invalid Entry - Must enter either Y or N, please try again.")
        else:
            break
    
    if anotherCustomer == "N":
        print(f"\nPolicy data has been saved. Next policy number: {POLICY_NUM}")
        break 

print("\nProgram ended.")
print("Thanks for using the insurance coverage program!")
            
            
    
