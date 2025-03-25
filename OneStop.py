# Description: Program for One Stop Insurance to enter and calculate insurance policies
# Author: Kevin Green
# Date(s): March 15, 2025 - March 21, 2025


# Define required libraries.
import FormatValues as FV
import datetime as DT
import OneStopFunctions as OSF
import time
import sys


# Define program constants.
POLICY_NUM = 1944

BASIC_PREM_RATE = 869.00
ADDT_CAR_DISC = .25           # Discount off additional cars being insured
EXT_LIABILITY_RATE = 130.00   # Cost of extra liability (up to $1000)
GLASS_COV_RATE = 86.00        # Cost for glass coverage       
LOANER_COV_RATE = 58.00       # Cost to have a loaner available if needed

HST_RATE = .15
PROCESS_FEE_RATE = 39.99      # Processing fee for monthly payments

CUR_DATE = DT.datetime.now()


# Main program starts here.
while True:
    
    # Gather user inputs.
    print()
    first_name = input("Enter the customers first name:                            ").title()
    last_name = input("Enter the customers last name:                             ").title()
    phone_num = input("Enter the customers phone number (##########):             ")

    print()
    address = input("Enter the customers street address:                        ")
    city = input("Enter the customers city:                                  ").title()
    
    prov_lst = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
    while True:
     prov = input("Enter the customers province (XX):                         ").upper()
     if prov not in prov_lst:
        print()
        print("   Error - not a valid province")
        print()
     else:
        break   
     
    postal = input("Enter the customers postal code (X#X#X#):                  ").upper()
     
    print()
    num_cars = input("Enter the number of cars being insured:                    ")
    num_cars = int(num_cars)
    ext_liab = input("Enter if the customer wants extra liability (Y/N)          ").upper()
    glass_cov = input("Enter if the customer wants glass coverage (Y/N):          ").upper()
    loaner_car = input("Enter if the customer wants loaner coverage (Y/N):         ").upper()

    pay_off_type_lst = ["Full", "Monthly", "Down Pay"]
    while True:
       pay_off_type = input("Enter how the customer will pay (Full, Monthly, Down Pay): ").title()
       if pay_off_type not in pay_off_type_lst:
          print()
          print("   Error - not a valid payment method")
          print()
       else:
          break
       
    down_pay = 0.00
    if pay_off_type == "Down Pay":
       down_pay = input("Enter the down payment amount:                             ")
       down_pay = int(down_pay)

    claim_num_lst = ["1285", "1499", "1722"]
    claim_date_lst = ["2020-03-26", "2022-04-01", "2023-10-22"]
    claim_amount_lst = [1065.00, 1220.00, 1350.00]
       
    # Perform required calculations.
    if num_cars == 1:
       insur_prem = BASIC_PREM_RATE
    else:
       insur_prem = (num_cars - 1) * (BASIC_PREM_RATE - (BASIC_PREM_RATE * ADDT_CAR_DISC)) + BASIC_PREM_RATE

    extra_costs = OSF.get_extra_costs(ext_liab, glass_cov, loaner_car, num_cars)
    tot_insur_prem = insur_prem + extra_costs
    hst = tot_insur_prem * HST_RATE

    final_insur_cost = tot_insur_prem + hst

    monthly_pay = OSF.get_monthly_pay(pay_off_type, final_insur_cost, PROCESS_FEE_RATE, down_pay)
    
    inv_date = CUR_DATE

    if pay_off_type == "Monthly" or pay_off_type == "Down Pay":
        pay_date = OSF.get_pay_due(inv_date)
        pay_date = FV.FDateS(pay_date)
        
    else:
       pay_date = "Paid in full, No monthly payments"


    # Create needed display values
    name_dsp = first_name[0] + ". " + last_name
    phone_num_dsp =FV.FPhone14(phone_num)
    inv_date = FV.FDateS(inv_date)

    if ext_liab == "Y":
       ext_liab_dsp = "Yes"
    else:
       ext_liab_dsp = "No"

    if glass_cov == "Y":
       glass_cov_dsp = "Yes"
    else:
       glass_cov_dsp = "No"

    if loaner_car == "Y":
       loaner_car_dsp = "Yes"
    else:
       loaner_car_dsp = "No"

    if pay_off_type == "Full":
       pay_off_type_dsp = "Paying in full"
    elif pay_off_type == "Monthly":
       pay_off_type_dsp = "Monthly"
    else:
       pay_off_type_dsp = "Monthly with down payment"

    # Display results
    print()
    print()
    print(f"                         One Stop Insurance Company")
    print(f"                          Customer Claims Receipt")
    print("--------------------------------------------------------------------------------")

    print()
    print(f" Customer Information:                                   Date Issued: {inv_date}")
    
    print()
    print(f"   Name and address:  {name_dsp:<20s}")
    print(f"                      {address:<30s}")
    print(f"                      {city:<15s}, {prov:<2s}, {postal:<6s}")

    print()
    print(f"   Phone #:           {phone_num_dsp}")

    print()
    print(f" Claim Info:")

    print()
    print(f"   Claim #:                           {POLICY_NUM:<4d}")
    print(f"   Number of cars being insured:     {num_cars:>2d}")
    print(f"   Extra liability:                   {ext_liab_dsp:<3s}")
    print(f"   Glass coverage:                    {glass_cov_dsp:<3s}")
    print(f"   Loaner car:                        {loaner_car_dsp:<3s}")

    print()
    print(f"   How will customer pay off claim:   {pay_off_type_dsp:<25s}")

    print()
    print("--------------------------------------------------------------------------------")

    print()
    print(f" Charges:")

    print()
    print(f"   Insurance premiums:                                                 {FV.FDollar2(insur_prem):>9s}")
    print(f"   Extra charges:                                                      {FV.FDollar2(extra_costs):>9s}")
    print(f"                                                                       ---------")
    print(f"   HST:                                                                {FV.FDollar2(hst):>9s}")
    print(f"   Total insurance cost:                                              {FV.FDollar2(final_insur_cost):>10s}")
    print(f"                                                                       ---------")
    if pay_off_type == "Down Pay":
       print(f"   Down payment:                                                       {FV.FDollar2(down_pay):>9s}")
       print(f"   Processing fee:                                                        {FV.FDollar2(PROCESS_FEE_RATE):>6s}")
       print(f"   Monthly payments:                                                   {FV.FDollar2(monthly_pay):>9s}")
    elif pay_off_type == "Monthly":
       print(f"   Processing Fee:                                                        {FV.FDollar2(PROCESS_FEE_RATE):>6s}")
       print(f"   Monthly payments:                                                   {FV.FDollar2(monthly_pay):>9s}")
    elif pay_off_type == "Full":
       print(f"   Monthly payments:                                                   {FV.FDollar2(monthly_pay):>9s}")
    print(f"                                                                       ---------")
    print(f"   First payment date:                         {pay_date:>33s}")

    print("--------------------------------------------------------------------------------")
    print()
    print(f" Customers previous claims:")

    print()
    print(f"            Claim #         Claim Date                 Amount")
    print(f"            -------------------------------------------------")
    for i in range(len(claim_num_lst)):
       print(f"             {claim_num_lst[i]:<4s}           {claim_date_lst[i]:<10s}              {FV.FDollar2(claim_amount_lst[i]):>9s}")
         
    print()
    
    # Write the values to a data file for storage.
    f = open("Policies.dat", "a")

    f.write(f"{FV.FNumber0(POLICY_NUM)}, ")
    f.write(f"{first_name}, ")
    f.write(f"{last_name}, ")
    f.write(f"{phone_num}, ")
    f.write(f"{address}, ")
    f.write(f"{city}, ")
    f.write(f"{prov}, ")
    f.write(f"{postal}, ")
    f.write(f"{FV.FNumber0(num_cars)}, ")
    f.write(f"{ext_liab}, ")
    f.write(f"{glass_cov}, ")
    f.write(f"{loaner_car}, ")
    f.write(f"{pay_off_type}, ")
    f.write(f"{FV.FNumber2(down_pay)}, ")
    f.write(f"{FV.FNumber2(final_insur_cost)}\n")

    f.close()

    # Display message to inform user data is saved
    message = "Saving claim number " + str(POLICY_NUM) + "....."
    for _ in range(6):
        print(message, end="\r")
        time.sleep(.3)
        sys.stdout.write("\033[2K\r")
        time.sleep(.3)
   
    print()
    POLICY_NUM += 1

    print()
    Continue = input("Would you like to process another claim (Y / N): ").upper()
    if Continue == "N":
       break
    print()


# Any housekeeping duties at the end of the program.
print()
print(f"     Thank you for using One Stop Insurance claims program - Have a great day!")
print()