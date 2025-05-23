# utils/analytics.py

def calculate_total_sales(transactions):
    """Sum up all sales from daily transactions."""
    return sum(t["amount"] for t in transactions)

def calculate_average_basket_size(transactions):
    """Average amount per transaction."""
    if not transactions:
        return 0
    return calculate_total_sales(transactions) / len(transactions)

def calculate_peak_hours(transactions):
    """Returns the hour(s) with most transactions."""
    from collections import Counter
    from datetime import datetime

    hours = [datetime.fromisoformat(t["timestamp"]).hour for t in transactions]
    count = Counter(hours)
    max_count = max(count.values(), default=0)
    return [hour for hour, c in count.items() if c == max_count]

def calculate_loyalty_score(customer_data):
    """Basic loyalty scoring based on return frequency or volume."""
    scores = {customer: len(purchases) for customer, purchases in customer_data.items()}
    return scores

def generate_summary_metrics(transactions, customer_data=None):
    return {
        "total_sales": calculate_total_sales(transactions),
        "avg_basket_size": calculate_average_basket_size(transactions),
        "peak_hours": calculate_peak_hours(transactions),
        "loyalty_scores": calculate_loyalty_score(customer_data or {})
    }

