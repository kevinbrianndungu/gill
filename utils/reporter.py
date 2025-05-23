# utils/reporter.py

def format_sales_report(metrics):
    report = (
        f"📊 Today's Sales Summary:\n"
        f"- Total Revenue: ${metrics['total_sales']:.2f}\n"
        f"- Average Basket Size: ${metrics['avg_basket_size']:.2f}\n"
        f"- Peak Shopping Hour(s): {', '.join(str(h) + ':00' for h in metrics['peak_hours'])}\n"
    )
    
    if metrics.get("loyalty_scores"):
        top_customers = sorted(metrics["loyalty_scores"].items(), key=lambda x: x[1], reverse=True)[:3]
        loyalty_report = "\n👑 Top Loyal Customers:\n" + "\n".join(f"{cust} - {score} visits" for cust, score in top_customers)
        report += loyalty_report
    
    return report

def keiali_response(metrics):
    return (
        f"Today's total revenue is ${metrics['total_sales']:.2f}. "
        f"The average customer spent ${metrics['avg_basket_size']:.2f}. "
        f"Peak activity was around {', '.join(str(h) + ':00' for h in metrics['peak_hours'])}. "
        f"Need anything else, Keiv?"
    )

