
'''
def investment_end(principal, annual_rate, compounded, contributions, time_years):
    rate = annual_rate/100
    principle_interest = principal*((1+(rate/compounded))**(compounded*time_years))
    future_val = contributions*(((1+(rate/compounded))**(compounded*time_years)-1)/(rate/compounded))
    total_compounded = principle_interest+future_val
    print(round(total_compounded,4))


principal_ = int(input("Initial amount: "))
annual_rate_ = int(input("Annual Rate of Return : "))
compounded_ = int(input("Times compounded yearly/monthly: "))
contributions_ = int(input("Additional Contributions: "))
time_years_ = int(input("Number of years later: "))

investment_end(principal_,annual_rate_,compounded_,contributions_,time_years_)
#investment(1400,7,12,100,20)


def investment_beg(principal, annual_rate, compounded, contributions, time_years):
    rate = annual_rate/100
    principle_interest = principal*((1+(rate/compounded))**(compounded*time_years))
    future_val = contributions*(((1+(rate/compounded))**(compounded*time_years)-1)/(rate/compounded))
    future_val_end = (future_val)*(1+(rate/compounded))
    total_compounded = principle_interest+future_val_end
    print(round(total_compounded,4))

principal_ = int(input("Initial amount: "))
annual_rate_ = int(input("Annual Rate of Return : "))
compounded_ = int(input("Times compounded yearly/monthly: "))
contributions_ = int(input("Additional Contributions: "))
time_years_ = int(input("Number of years later: "))
investment_beg(principal_, annual_rate_, compounded_, contributions_, time_years_)


def investment_diff(principal, annual_rate, compounded, contributions, periodic_cont, time_years):
    rate = annual_rate/100
    periodic = periodic_cont/12
    principal_interest = principal*((1+(rate/compounded))**(compounded*time_years))
    future_val = contributions*(((1+(rate/compounded))**(compounded*time_years)-1)/(rate/compounded))
    future_val_cont_end = future_val*periodic
    total_compounded = future_val_cont_end+principal_interest
    print(round(total_compounded,4))
principal_ = int(input("Initial amount: "))
annual_rate_ = int(input("Annual Rate of Return : "))
compounded_ = int(input("Times compounded yearly/monthly: "))
contributions_ = int(input("Additional Contributions: "))
periodic_cont_ = int(input("Periodic Contributions (every.... months): "))
time_years_ = int(input("Number of years later: "))
investment_diff(principal_, annual_rate_, compounded_, contributions_, periodic_cont_, time_years_)
