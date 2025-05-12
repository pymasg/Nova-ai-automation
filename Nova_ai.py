'''
Programmer: Ahsan Raza khan
Date: 22.1.2025
Description: This code will automate the login form page of nova ai.   
Caution: Use it for only legal purpose and the owner is not responsible for anything.  
'''
# --- import the nesscessary  modules ----
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# --- chosing MS Edge for automation ---
web = webdriver.Edge()

# --- Making window maximize ---
web.maximize_window()

# --- open web ---
web.get("https://chat.novaapp.ai/login")

# --- locating input tag in which email is to be written ---
try:
    wait = WebDriverWait(web, 10)
    email_entry = wait.until(EC.presence_of_all_elements_located(
        (By.NAME, 'email')))
    email_entry[0].send_keys('ahsanpymaster@gmail.com')
except Exception as e:
    print(f"{e}")

# --- locating password input field ---
try:
    password_entry = wait.until(EC.presence_of_all_elements_located(
        (By.NAME, "password")))

    password_entry[0].send_keys('PyAhsanRk1122')
    password_entry[0].submit()
    sleep(10)
except Exception as e:
    print(f"{e}")

# --- Save screenshor of webpage ---
web.save_screenshot("image.png")

# --- Stop program execution ---
sleep(10)

web.quit()
