age = input("What is your age?")
age_int = int(age)

years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
month_remaining = years_remaining * 12

message = f"You have {month_remaining} month,{weeks_remaining}weeks and {days_remaining}days"
print(message)
