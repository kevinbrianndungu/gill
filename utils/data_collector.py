from .competitor_scraper import fetch_competitor_data
from .internal_mock import fetch_internal_data

def collect_all_data():
    competitor_data = fetch_competitor_data()
    internal_data = fetch_internal_data()

    return {
        "competitor_data": competitor_data,
        "internal_data": internal_data
    }

