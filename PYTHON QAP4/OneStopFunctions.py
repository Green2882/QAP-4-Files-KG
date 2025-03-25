import datetime as DT

def get_extra_costs(ext_liab, glass_cov, loaner_car, num_cars):
   # Function that will calculate the extra costs of insurance premiums

   if ext_liab == "Y":
       ext_liab_cost = 130.00 * num_cars
   else:
       ext_liab_cost = 0.00

   if glass_cov == "Y":
       glass_cov_cost = 86.00 * num_cars
   else:
       glass_cov_cost = 0.00

   if loaner_car == "Y":
       loaner_car_cost = 58.00 * num_cars
   else:
       loaner_car_cost = 0.00

   extra_costs = ext_liab_cost + glass_cov_cost + loaner_car_cost
   
   return extra_costs


def get_monthly_pay(pay_off_type, final_insur_cost, PROCESS_FEE_RATE, down_pay):
    # Function that will determine customers monthly payment

    if pay_off_type == "Full":
       monthly_pay = 0.00
    elif pay_off_type == "Monthly":
       monthly_pay = (final_insur_cost + PROCESS_FEE_RATE) / 8
    else:
       monthly_pay = (final_insur_cost - down_pay + PROCESS_FEE_RATE) / 8

    return monthly_pay

def get_pay_due(inv_date):
        # Function to determine payment date based off
        # 20 days after invoice or 1st of next month, whichever is later

        inv_20_days = inv_date + DT.timedelta(days = 20)
    
        pur_year = inv_date.year
        pur_month = inv_date.month
        pur_day = inv_date.day

        pay_year = pur_year
        pay_month = pur_month + 1
        if pay_month == 13:
            pay_month -= 12
            pay_year += 1
        pay_day = 1
        pay_first_date = DT.datetime(pay_year, pay_month, pay_day)
        if inv_20_days > pay_first_date:
            pay_date = inv_20_days
        else:
            pay_date = pay_first_date

        return pay_date

