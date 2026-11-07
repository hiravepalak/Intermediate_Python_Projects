from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Palak")

surname = driver.find_element(By.NAME, value="lName")
surname.send_keys("Hirave")

email = driver.find_element(By.NAME, value="email")
email.send_keys("example@email.com")

click_button = driver.find_element(By.XPATH, value='//*[@id="signup-form"]/button')
click_button.click()

driver.quit()