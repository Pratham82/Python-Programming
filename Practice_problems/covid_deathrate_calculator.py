import requests
import json

# Program to find Covid DeathRate
"""Program to calculate covid deathrate"""
# Requirements:
# 1. Values must be returned by a function.
# 2. Take user input, total cases and no. of deaths


def get_summary():
    """Fetching Realtime values"""
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    result = json.loads(response.text)
    total_cases_fetched = result["Global"]["TotalConfirmed"]
    total_deaths_fetched = result["Global"]["TotalDeaths"]
    summary = {
        "total_cases": total_cases_fetched,
        "total_deaths": total_deaths_fetched
    }
    return summary


def deathrate_calculator(total_cases, deaths):
    """Deathrate calculator"""
    deathrate = deaths / total_cases * 100
    return f"DeathRate calulated from the given values: {round(deathrate,2)}%"


total_cases = get_summary()["total_cases"]
total_deaths = get_summary()["total_deaths"]

print(deathrate_calculator(total_cases, total_deaths))
