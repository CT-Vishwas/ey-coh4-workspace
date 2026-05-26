principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest in percentage: ")) / 100
num_years = int(input("Input number of Years: "))

# plan_kind = input("Select the Type of Plan\n1.Lumpsum\n2.SIP\n")

# if plan_kind == "1":
#     lumpsum_value = principal * (1 + (rate_of_interest)) ** num_years
#     print(f"The lumpsum invested value is: {lumpsum_value:.2f}")
# elif plan_kind == "2":
#     total_months = num_years * 12
#     monthly_amount = principal / total_months
#     print(f"Monthly Amount: {monthly_amount:.2f}")
#     monthly_interest_rate = rate_of_interest / 12

#     sip_value = monthly_amount * ((((1+monthly_interest_rate)**total_months)-1)/monthly_interest_rate)*(1+monthly_interest_rate)
#     print(f"The SIP invested value is: {sip_value:.2f}")
# else:
#     print("INVALID Plan")



lumpsum_value = principal * (1 + (rate_of_interest)) ** num_years
print(f"The lumpsum invested value is: {lumpsum_value:.2f}")
total_months = num_years * 12
monthly_amount = principal / total_months
print(f"Monthly Amount: {monthly_amount:.2f}")
monthly_interest_rate = rate_of_interest / 12

sip_value = monthly_amount * ((((1+monthly_interest_rate)**total_months)-1)/monthly_interest_rate)*(1+monthly_interest_rate)
print(f"The SIP invested value is: {sip_value:.2f}")

if lumpsum_value > sip_value:
    print("Lumpsum investing is beneficial")
else:
    print("SIP is beneficial")