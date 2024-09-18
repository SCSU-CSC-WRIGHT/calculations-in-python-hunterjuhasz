#user prompts
principal=float(input("Enter the principal amount:"))
rate_of_interest=float(input("Enter the rate of interest:"))
time_period=float(input("Enter the time period (in years:)"))
#calculations
simple_interest= (principal*rate_of_interest*time_period)/100


#print the calculations

print("The simple interest is:", simple_interest)