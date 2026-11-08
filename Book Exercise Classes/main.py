import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = os.getenv("EMAIL") or ""
ACCOUNT_PASSWORD = os.getenv("PASSWORD") or ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 7)

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    get_login = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    get_login.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.send_keys(ACCOUNT_PASSWORD)

    login_button = driver.find_element(By.ID, "submit-button")
    login_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "logout-button")))

retry(login, description="login")

classes_booked = 0
waitlist_joined = 0
already_booked = 0
total_tues_thurs = 0
detailed_list = []

def process_day(day_prefix):
    global classes_booked, waitlist_joined, already_booked, total_tues_thurs

    day_grp = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[id^='day-group-'][id*='{day_prefix}']")))
    day_title = day_grp.find_element(By.CSS_SELECTOR, "[id^='day-title-']").text
    class_cards = day_grp.find_elements(By.CSS_SELECTOR, "[id^='class-card-']")

    for card in class_cards:
        card_text = card.text

        if "6:00 PM" in card_text:
            total_tues_thurs += 1
            class_name = card.find_element(By.TAG_NAME, "h3").text

            button = card.find_element(By.CSS_SELECTOR, "[class^='ClassCard_bookButton__DMM1I ClassCard_']")
            button_text = button.text

            if button_text == "Booked":
                already_booked += 1
                detailed_list.append(f"✓ Already booked: {class_name} on {day_title}")
            elif button_text == "Waitlisted":
                already_booked += 1
                detailed_list.append(f"✓ Already on waitlist: {class_name} on {day_title}")
            elif button_text == "Join Waitlist":
                def click_waitlist():
                    driver.execute_script("arguments[0].click();", button)

                    WebDriverWait(driver, 3).until(
                        lambda d: "Waitlisted" in button.text or "Leave Waitlist" in button.text)

                retry(click_waitlist, retries=7, description=f"join waitlist for {class_name}")
                waitlist_joined += 1
                detailed_list.append(f"✓ Joined waitlist: {class_name} on {day_title}")
            elif button_text == "Book Class":
                def click_book():
                    driver.execute_script("arguments[0].click();", button)

                    WebDriverWait(driver, 3).until(
                        lambda d: "Booked" in button.text or "Cancel Booking" in button.text
                    )

                retry(click_book, retries=7, description=f"book class {class_name}")
                classes_booked += 1
                detailed_list.append(f"✓ Booked: {class_name} on {day_title}")


def get_my_bookings():
    my_bookings_link = wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link")))
    driver.execute_script("arguments[0].click();", my_bookings_link)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    h3_elements = driver.find_elements(By.TAG_NAME, "h3")

    found_output = []
    for h3 in h3_elements:
        text = h3.text.strip()
        if text:
            found_output.append(text)

    if not found_output:
        raise NoSuchElementException("No bookings found.")
    return found_output


def verification():
    global total_tues_thurs, detailed_list
    for idx, item in enumerate(detailed_list, 1):
        print(f"{idx}. {item}")

    print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_tues_thurs} ---")
    print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

    found_count = 0
    verified_output = []

    try:
        verified_items = retry(get_my_bookings, retries=7, description="fetch my bookings page")
        for text in verified_items:
            found_count += 1
            verified_output.append(f"  ✓ Verified: {text}")

        for v in verified_output:
            print(v)

    except Exception:
        print("  ❌ NoSuchElementException: Bookings container or items not found.")
        found_count = 0

    print(f"\n--- VERIFICATION RESULT ---")
    expected = total_tues_thurs
    print(f"Expected: {expected} bookings")
    print(f"Found: {found_count} bookings")

    if found_count == expected:
        print("✅ SUCCESS: All bookings verified!")
    else:
        diff = expected - found_count
        print(f"❌ MISMATCH: Missing {diff} bookings")

process_day("tue")
process_day("thu")
verification()

