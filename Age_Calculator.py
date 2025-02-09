from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust for negative months or days
    if days < 0:
        months -= 1
        days += 30  # Approximate month length

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Input date of birth
birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

# Calculate and display age
years, months, days = calculate_age(birth_date)
print(f"Your age is {years} years, {months} months, and {days} days.")

    