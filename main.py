from src.data_loader import load_battery_data
from src.soc_estimator import estimate_soc
from src.exporter import export_soc_data
from src.visualization import (
    plot_voltage_vs_time,
    plot_soc_vs_time,
)

FILE_PATH = "data/raw/battery_discharge.csv"


def main():
    # Load battery discharge data
    battery_data = load_battery_data(FILE_PATH)

    # Estimate State of Charge (SoC)
    battery_data["SoC(%)"] = battery_data["Voltage(V)"].apply(
        estimate_soc
    )

    # Display first few rows
    print("\nBattery Data with Estimated SoC:\n")
    print(battery_data.head())

    # Generate and save plots
    plot_voltage_vs_time(battery_data)
    plot_soc_vs_time(battery_data)

    print("\nPlots saved successfully!")
    print("Location: outputs/plots/")

    export_soc_data(battery_data)

if __name__ == "__main__":
    main()