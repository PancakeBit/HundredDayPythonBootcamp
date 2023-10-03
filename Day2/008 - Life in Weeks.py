age = input("What is your current age?: ")

age = int(age)

days = (90-age) * 365
weeks = (90-age) * 52
months = (90-age) * 12

print(f"You have {days} days, or {weeks} weeks, or {months} months left if you live up to 90 years old")
