from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
clean_time = []
for time in times:
    clean_time.append(time.text)

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
clean_date = []
for date in dates:
    clean_date.append(date.text)

numbers = [0, 1, 2, 3, 4]
event = {number: {clean_time[number]:clean_date[number]} for number in numbers}
print(event)

driver.quit()