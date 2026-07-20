from src.data_loader import load_battery_data

FILE_PATH = "data/raw/battery_discharge.csv"


def main():
    battery_data = load_battery_data(FILE_PATH)

    print("Battery data loaded successfully!\n")
    print(battery_data.head())


if __name__ == "__main__":
    main()