from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def fetch_competitor_data():
    options = Options()
    options.add_argument('--headless')  # Silent mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://naivas.online/")
    time.sleep(5)  # Wait for JS to load

    try:
        store_name = "Naivas Supermarket Nakuru Super Centre"

        # Update these selectors as needed
        address = driver.find_element(By.CSS_SELECTOR, "footer div[class*='address']").text
        promo_banner = driver.find_element(By.CSS_SELECTOR, "div[class*='promo'], div[class*='banner']").text

        return {
            "store_name": store_name,
            "address": address,
            "promotion": promo_banner,
            "source": "competitor_website"
        }

    except Exception as e:
        print(f"Scraping error: {e}")
        return {
            "store_name": store_name,
            "address": None,
            "promotion": None,
            "source": "competitor_website"
        }
    finally:
        driver.quit()

