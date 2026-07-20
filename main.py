from src.data_loader import load_battery_data
from src.soc_estimator import estimate_soc

FILE_PATH = "data/raw/battery_discharge.csv"


def main():
    battery_data = load_battery_data(FILE_PATH)

    battery_data["SoC(%)"] = battery_data["Voltage(V)"].apply(
        estimate_soc
    )

    print(battery_data.head())


if __name__ == "__main__":
    main()