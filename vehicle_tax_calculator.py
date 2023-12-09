from datetime import datetime

renew_date = input("Enter the renew from date (YYYY/MM/DD): ")
today_date = input("Enter today's date (YYYY/MM/DD): ")
engine_cc_str = input("Enter the CC of your vehicle: ")

# Convert engine_cc to an integer, handling potential errors
try:
    engine_cc = int(engine_cc_str)
except ValueError:
    print("Error: Engine CC should be a numeric value.")
    engine_cc = 0  # Default value for error case

date_format = "%Y/%m/%d"
date1 = datetime.strptime(renew_date, date_format)
date2 = datetime.strptime(today_date, date_format)
difference_in_days = (date2 - date1).days

if difference_in_days > 455:
    if 0 < engine_cc <= 125:
        tax = 3000
        renewal_charge = 300
        fine_tax = tax * 0.20
        service_charge = 399
        renewal_fine = renewal_charge
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 125 < engine_cc <= 150:
        tax = 5000
        renewal_charge = 300
        fine_tax = tax * 0.20
        service_charge = 399
        renewal_fine = renewal_charge
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 151 <= engine_cc <= 225:
        tax = 6500
        renewal_charge = 300
        fine_tax = tax * 0.20
        service_charge = 399
        renewal_fine = renewal_charge
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 226 <= engine_cc <= 400:
        tax = 11000
        renewal_charge = 300
        fine_tax = tax * 0.20
        service_charge = 399
        renewal_fine = renewal_charge
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 401 <= engine_cc <= 650:
        tax = 20000
        renewal_charge = 300
        fine_tax = tax * 0.20
        service_charge = 399
        renewal_fine = renewal_charge
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif engine_cc > 650:
        tax = 30000
        renewal_charge = 300
        fine_tax = tax * 0.20
        service_charge = 399
        renewal_fine = renewal_charge
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    else:
        print("Invalid engine CC value")
else:  # if data isn't cross over 365.
    if 0 < engine_cc <= 125:
        tax = 3000
        renewal_charge = 300
        fine_tax = 0
        service_charge = 399
        renewal_fine = 0
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 125 < engine_cc <= 150:
        tax = 5000
        renewal_charge = 300
        fine_tax = 0
        service_charge = 399
        renewal_fine = 0
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 151 <= engine_cc <= 225:
        tax = 6500
        renewal_charge = 300
        fine_tax = 0
        service_charge = 399
        renewal_fine = 0
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 226 <= engine_cc <= 400:
        tax = 11000
        renewal_charge = 300
        fine_tax = 0
        service_charge = 399
        renewal_fine = 0
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif 401 <= engine_cc <= 650:
        tax = 20000
        renewal_charge = 300
        fine_tax = 0
        service_charge = 399
        renewal_fine = 0
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine
    elif engine_cc > 650:
        tax = 30000
        renewal_charge = 300
        fine_tax = 0
        service_charge = 399
        renewal_fine = 0
        total_amount = tax + renewal_charge + fine_tax + service_charge + renewal_fine

# Print the amounts only if they are defined
if (
    "tax" in locals()
    and "renewal_charge" in locals()
    and "fine_tax" in locals()
    and "service_charge" in locals()
):
    print(
        f"You need to pay:- \n"
        f"Unpaid Tax Rs {tax} \n"
        f"Unpaid Tax Penalty Rs {fine_tax} \n"
        f"Renewal Charge Rs {renewal_charge} \n"
        f"Renewal Fine Rs {renewal_fine} \n"
        f"MeroSawaari Service Charge Rs {service_charge} \n"
        f"Total Amount is Rs {total_amount} \n"
    )
