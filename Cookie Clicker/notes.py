from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Pass bot detection - now automatically added
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Little-Black-Classics-Box-Penguin/dp/0141398876/ref=sr_1_1?crid=2JR3P0X5AGX9Y&dib=eyJ2IjoiMSJ9.iUxZV52ojXsS1HD8YG_-qeYdpAI2mOEaE42xN-HFNgE-HnxRIWlfR8OMTebq72yFY30gAQFUH8vHFT9pr6XNg3Z8OlLjOL6848MkXHU6PvW9wpF-oaWjLow2HTZC7t2MY62w5ZNy5GGtGH0wnxFWyS1rOpVeqrJ9HUYxlgYDlXm-4kYLvK_JJ04qlhoFQNSJy_kMj51kBz55sCulLyLvu5FhiBZDGfbuykNvjGF0d4HL0YUg5vno2vn_YQz6jNcm2c6qjz34W4rRpkVczOZaQEoY5VAcZkEy6r9vUkETlDk.aOZ0SE5oxVcDHjsjwJQKv6CMfRT1jQ2HevT0LTbxP58&dib_tag=se&dplnkSrc=appbanner&keywords=penguin+classics&qid=1794033191&sprefix=Penguin+%2Caps%2C311&sr=8-1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text

# driver.close() (closes single tab)
driver.quit() #quits entire browser
