
"""Program to find Covid19 death rate and cases in India"""
import json
import requests


def get_summary():
    """Fetching Realtime values"""
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    result = json.loads(response.text)
    total_cases_fetched = result["Countries"][76]["TotalConfirmed"]
    total_deaths_fetched = result["Countries"][76]["TotalDeaths"]
    toal_recovered_fetched = result["Countries"][76]["TotalRecovered"]
    summary = {
        "total_cases": total_cases_fetched,
        "total_deaths": total_deaths_fetched,
        "total_recovered": toal_recovered_fetched
    }
    return summary


def deathrate_calculator(total_cases, deaths):
    """Deathrate calculator"""
    deathrate = deaths / total_cases * 100
    return f"""Total Confirmed cases: {get_summary()["total_cases"]}
        \nTotal Recovered: {get_summary()["total_recovered"]}
        \nTotal Deaths: {get_summary()["total_deaths"]}
        \nDeathRate calulated from the given values: {round(deathrate,2)}%"""


total_cases = get_summary()["total_cases"]
total_deaths = get_summary()["total_deaths"]

print(deathrate_calculator(total_cases, total_deaths))
