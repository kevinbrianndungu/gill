import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_competitor():
    """
    Scrapes live competitor data from their website.
    Example: Extracts store name, address, and any visible promotions.
    """
    url = "https://naivas.info/locations/naivas-supercentre-nakuru/"  # Competitor's URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        session = requests.Session()
        session.headers.update(headers)
        response = session.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, "html.parser")

        # Example: Extract store name
        store_name_element = soup.find("h1", class_="entry-title")  # Adjust based on HTML structure
        store_name = store_name_element.text.strip() if store_name_element else None

        # Example: Extract store address
        address_element = soup.find("div", class_="address")  # Adjust based on HTML structure
        address = address_element.text.strip() if address_element else None

        # Example: Extract promotions (if available)
        promotion_element = soup.find("div", class_="promotion-banner")
        promotion = promotion_element.text.strip() if promotion_element else None

        return {
            "store_name": store_name,
            "address": address,
            "promotion": promotion,
            "source": "competitor_website",
        }
    except Exception as e:
        print(f"Error scraping competitor data: {e}")
        return {"error": str(e)}

def fetch_internal_data():
    """
    Fetches internal data from a local JSON file.
    Example: Current prices, inventory, loyalty metrics, etc.
    """
    try:
        # Path to the internal data file
        file_path = os.path.join(os.path.dirname(__file__), "../internal_data.json")

        # Read the JSON file
        with open(file_path, "r") as f:
            data = json.load(f)

        # Extract relevant fields
        return {
            "current_price": data.get("current_price"),
            "inventory": data.get("inventory"),
            "loyalty_percentage": data.get("loyalty_percentage"),
            "delivery_time": data.get("delivery_time"),
        }
    except Exception as e:
        print(f"Error fetching internal data: {e}")
        return {"error": str(e)}

def collect_all_data():
    """
    Collects both competitor and internal data into a single dictionary.
    """
    competitor_data = scrape_competitor()
    internal_data = fetch_internal_data()

    return {
        "competitor_data": competitor_data,
        "internal_data": internal_data,
    }
