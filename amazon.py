from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
searchBar = driver.find_element(By.ID, "twotabsearchtextbox")
searchBar.click()

searchBar.send_keys("Sony PS5")
searchButton = driver.find_element(By.ID, "nav-search-submit-button")
searchButton.click()


product = driver.find_element(By.LINK_TEXT, "Sony PlayStation5 Gaming Console (Slim)")
product.click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])

addToCart = driver.find_element(By.ID, "add-to-cart-button")
addToCart.click()
time.sleep(10)

goToCart = driver.find_element(By.LINK_TEXT, "Go to Cart")
goToCart.click()

proceedToBuy = driver.find_element(By.NAME, "proceedToRetailCheckout")
proceedToBuy.click()


time.sleep(8)
email = driver.find_element(By.ID, "ap_email_login")
email.send_keys("jothirsailesh005@gmail.com")

time.sleep(15)
continue_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div/div/span/form/span/span/input")
continue_button.click()


time.sleep(8)
password = driver.find_element(By.ID, "ap_password")
password.send_keys("#Jothir55Sailesh55")


time.sleep(15)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(100)

