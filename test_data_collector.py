import json
from utils.data_collector import collect_all_data

def validate_data(data):
    issues = []

    competitor = data.get("competitor_data", {})
    internal = data.get("internal_data", {})

    if not competitor.get("store_name"):
        issues.append("❌ Missing store_name")

    if not competitor.get("address"):
        issues.append("❌ Missing address")

    if not competitor.get("promotion"):
        issues.append("❌ Missing promotion")

    if "source" not in competitor or not competitor.get("source"):
        issues.append("❌ Missing source info")

    if "current_price" not in internal:
        issues.append("❌ Missing current_price")

    if "inventory" not in internal:
        issues.append("❌ Missing inventory")

    if "loyalty_percentage" not in internal:
        issues.append("❌ Missing loyalty_percentage")

    if "delivery_time" not in internal:
        issues.append("❌ Missing delivery_time")

    return issues

if __name__ == "__main__":
    print("🧠 Running Gill Data Collector Test...\n")

    try:
        print("⚙️ Collecting data...")
        data = collect_all_data()

        print("\n📦 Raw Output:\n")
        print(json.dumps(data, indent=4))

        print("\n🔍 Validation Report:\n")
        issues = validate_data(data)

        if issues:
            for issue in issues:
                print(issue)
        else:
            print("✅ All fields populated successfully.")

    except Exception as e:
        print("❌ An unexpected error occurred:")
        print(str(e))

