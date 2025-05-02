from utils.data_collector import collect_all_data

if __name__ == "__main__":
    data = collect_all_data()
    print(json.dumps(data, indent=4))
