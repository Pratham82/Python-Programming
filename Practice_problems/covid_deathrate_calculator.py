# Program to find Covid DeathRate

# Requirements:
# 1. Values must be returned by a function.
# 2. Take user input, total cases and no. of deaths

# deathrate_calculator

total_cases = int(input('Enter the of total cases:'))
total_deaths = int(input('Enter the of total deaths:'))


def deathrate_calculator(total_cases, deaths):
    deathrate = deaths / total_cases * 100
    return f"DeathRate calulated from the given values: {round(deathrate,2)}%"


print(deathrate_calculator(700000, 350000))
print(deathrate_calculator(total_cases, total_deaths))
