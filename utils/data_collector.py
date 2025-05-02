import requests
from bs4 import BeautifulSoup
import json

def scrape_competitor():
    """
    Scrapes live competitor data from their website.
    Example: Extracts product prices, promotions, and delivery info.
    """
    url = "https://competitor.com/pricing"  # Replace with the actual URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, "html.parser")

        # Example: Extract price
        price_element = soup.find("span", class_="price")  # Adjust based on HTML structure
        price = float(price_element.text.strip().replace("$", "")) if price_element else None

        # Example: Extract promotions (e.g., banners)
        promotion_element = soup.find("div", class_="promotion-banner")
        promotion = promotion_element.text.strip() if promotion_element else None

        return {
            "price": price,
            "promotion": promotion,
            "source": "competitor_website",
        }
    except Exception as e:
        print(f"Error scraping competitor data: {e}")
        return {"error": str(e)}

def fetch_internal_data():
    """
    Fetches internal data from your database or API.
    Example: Current prices, inventory, loyalty metrics, etc.
    """
    # Simulated internal API endpoint
    internal_api_url = "https://api.yourcompany.com/internal-data"  # Replace with your actual API
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace with your API key

    try:
        response = requests.get(internal_api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Example: Extract relevant fields
        return {
            "current_price": data.get("price"),
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
