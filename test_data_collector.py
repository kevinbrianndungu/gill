import json
from utils.data_collector import collect_all_data

if __name__ == "__main__":
    # Collect all data
    data = collect_all_data()

    # Print the data in a readable JSON format
    print(json.dumps(data, indent=4))
