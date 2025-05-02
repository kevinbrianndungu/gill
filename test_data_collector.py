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

    if not internal.get("current_price"):
        issues.append("❌ Missing current_price")

    if not internal.get("inventory"):
        issues.append("❌ Missing inventory")

    return issues

if __name__ == "__main__":
    # Collect data
    data = collect_all_data()

    # Print raw output
    print("📦 Raw Output:\n")
    print(json.dumps(data, indent=4))

    # Run validations
    print("\n🔍 Validation Report:\n")
    issues = validate_data(data)

    if issues:
        for issue in issues:
            print(issue)
    else:
        print("✅ All fields populated.")

