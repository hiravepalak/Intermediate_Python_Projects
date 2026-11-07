from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://ozh.github.io/cookieclicker/")

lang = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
lang.click()

sleep(1)
try:
    driver.execute_script("""
        var banner = document.querySelector('.cc_banner');
        if (banner) { banner.remove(); }
    """)
except Exception:
    pass

def check_upgrades():
    cookie_no = driver.find_element(By.ID, "cookies")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    clean_price = []
    for price in prices:
        clean_price.append(price.text)
    print(clean_price)

item_ids = [f"product{i}" for i in range(18)]

wait_time = 20
timeout = time() + wait_time
five_min = time() + 60 * 10

while True:
    cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {str(best_item.get_attribute('id'))}")

        except ValueError:
            print("Couldn't find cookie count or items")

        timeout = time() + wait_time

    if time() > five_min:
        cookies_element = driver.find_element(by=By.ID, value="cookies")
        print(f"Final result: {cookies_element.text}")