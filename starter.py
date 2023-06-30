from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#Initializes the chrome webdriver into a variable
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#opens the URL path that is specified
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
browser.implicitly_wait(10)
#Maximizes the window
browser.maximize_window()
#Finds the HTML element for the first name bar using the ID
first_name = browser.find_element(By.XPATH, "//*[@id=\"input-firstname\"]")
#Sends FirstName in the first name bar
first_name.send_keys("Random Name")
#Finds the HTML elements for last_name, telephone no, email, password and filled them in the same way

#checks the subscribe to newsletter box and clicks
subscribe = browser.find_element(By.XPATH, "//label[@for='input-newsletter-yes']")
subscribe.click()

#Checks the terms and conditions box and clicks 
tc = browser.find_element(By.XPATH, "//label[@for='input-agree']")
tc.click()
#Finds the continue button and clicks
cont = browser.find_element(By.XPATH, "//*[@id=\"content\"]/form/div/div/input")
cont.click()

#Checks what the browser title is after the user has been logged in
page_title = browser.find_element(By.XPATH, "//*[@id=\"content\"]/h1")

assert page_title.text == "Congratulations! Your new account has been successfully created!"
#Asserts for successful login 