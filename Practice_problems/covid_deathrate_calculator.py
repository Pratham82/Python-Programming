# Program to find Covid DeathRate
"""Program to calculate covid deathrate"""
# Requirements:
# 1. Values must be returned by a function.
# 2. Take user input, total cases and no. of deaths

# Taking input
total_cases_input = int(input('Enter the total cases:'))
total_deaths_input = int(input('Enter the total deaths:'))


def deathrate_calculator(total_cases, deaths):
    """Deathrate calculator"""
    deathrate = deaths / total_cases * 100
    return f"DeathRate calulated from the given values: {round(deathrate,2)}%"


print(deathrate_calculator(700000, 350000))
print(deathrate_calculator(total_cases_input, total_deaths_input))
