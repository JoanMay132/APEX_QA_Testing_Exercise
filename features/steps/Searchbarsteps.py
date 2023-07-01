from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('I launch the browser')
def launch_browser(context):
    # Code to open the browser
    context.driver = webdriver.Chrome()

@when('I open the Liverpool homepage')
def open_liverpool_homepage(context):
    # Code to open the Liverpool homepage
    context.driver.get("https://www.liverpool.com.mx/tienda/home")

@when('I click the search bar')
def click_search_bar(context):
    # Code to click on the search bar
    context.driver.find_element(By.ID, "mainSearchbar").click()

@when('I type "{search_term}" in the search bar')
def enter_search_term(context, search_term):
    if search_term == "NO_SPACE":
        search_term = ""
        # Code to enter the search term in the search bar
        context.driver.find_element(By.ID, "mainSearchbar").send_keys(search_term)
        time.sleep(3)
    elif search_term == "TRIPLE_SPACE":
        search_term = "   "
        # Code to enter the search term in the search bar
        context.driver.find_element(By.ID, "mainSearchbar").send_keys(search_term)
        time.sleep(3)
    else:
        
        context.driver.find_element(By.ID, "mainSearchbar").send_keys(search_term)
        time.sleep(3)

@when('I click on the search button')
def click_search_button(context):
    # Code to press enter key on the keyboard
    context.driver.find_element(By.XPATH, "//header/div[4]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/i[1]").click()
    time.sleep(3)

@then('I should see "{expected_results}"')
def verify_search_results(context, expected_results):
    if expected_results == "list of articles related to toys" or expected_results == "list of articles related to Samsung Galaxy S21 5G" or expected_results == "list of articles related to the Electronics category":
        try:
            # Get the element containing the number of results
            result_element = context.driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/aside[1]/div[1]/div[1]/h1[1]/span[1]")
            # Get the text of the element
            result_text = result_element.text
            # Extract the number of results from the text string
            num_results = int(''.join(filter(str.isdigit, result_text)))
            # Verify if the number of results is greater than zero
            assert num_results > 0 # If condtions is True, the test passes
        except:
            assert False, "The element containing the number of results was not found"

    elif expected_results == "message indicating no articles found":
        # Verify that a message indicating no articles found is displayed
        try:
            context.driver.find_element(By.XPATH, "//h1[contains(text(),'Lo sentimos...')]")
        except:
            assert False, "The message indicating no articles found was not displayed"

    elif expected_results == "same page" or expected_results == "current page":
        try:
            # Verify that the same page is displayed
            current_url = context.driver.current_url
            assert current_url == "https://www.liverpool.com.mx/tienda/home"
        except:
            assert False, "The page did not remain on the same homepage"


@then('I close the browser')
def closeBrowser(context):
   context.driver.close()  # Close the browser
    
