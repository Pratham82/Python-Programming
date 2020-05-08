import webbrowser
from selenium import webdriver

# basic: opening webpage using web driver
webbrowser.open("https://github.com/Pratham82/Complete-Python-3-Bootcamp")

# Using selenium for automation
browser = webdriver.Chrome()

browser.get("https://www.github.com/Pratham82")
