from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_number = driver.find_element(By.ID, value="mwDw")
print(article_number.text)

search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

driver.quit()