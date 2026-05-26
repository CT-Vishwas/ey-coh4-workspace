principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest in percentage (p.a): ")) / 100
num_years = int(input("Input number of Years: "))

monthly_sip_amount = principal / (num_years * 12 )
monthly_rate_decimal = rate_of_interest / 12

# Lumpsum Growth
print("\n------LUMPSUM INVESTMENT GROWTH -------\n")
print(f"Starting Principal: {principal}")
print(f"{'Year':<6}{'Opening Balance':<18}{'Interest Earned':<18}{'Closing Balance':<18}")
print('-'*60)

lumpsum_balance = principal
for year in range(1, num_years + 1):
    opening_balance = lumpsum_balance
    interest = opening_balance * rate_of_interest
    closing = opening_balance + interest

    print(f"{year:<6}Rs.{opening_balance:<17.2f}Rs.{interest:<17.2f}Rs.{closing:<17.2f}")
    lumpsum_balance = closing


# sip Growth
print("\n------SIP INVESTMENT GROWTH -------\n")
print(f"Monthly Contribution: {monthly_sip_amount}")
print(f"{'Year':<6}{'Total Invested':<18}{'Interest Earned':<18}{'Future Value':<18}")
print('-'*60)

sip_balance = 0
total_sip_invested = 0

for year in range(1, num_years + 1):
    yearly_interest_earned = 0

    for month in range(1,13):
        sip_balance += monthly_sip_amount
        total_sip_invested += monthly_sip_amount

        # Calculate monthly interest (compounded monthly)
        monthly_interest = sip_balance * monthly_rate_decimal
        sip_balance += monthly_interest

        yearly_interest_earned += monthly_interest
        
    print(f"{year:<6}Rs{total_sip_invested:<17.2f}Rs.{yearly_interest_earned:<17.2f}Rs.{sip_balance:<17.2f}")
