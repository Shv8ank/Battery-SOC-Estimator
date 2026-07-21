from src.data_loader import load_battery_data
from src.profile_loader import load_battery_profile
from src.soc_estimator import estimate_soc
from src.visualization import (
    plot_voltage_vs_time,
    plot_soc_vs_time,
)
from src.exporter import export_soc_data

FILE_PATH = "data/raw/battery_discharge.csv"
PROFILE_PATH = "data/profiles/lithium_ion.csv"


def main():
    # Load battery discharge data
    battery_data = load_battery_data(FILE_PATH)

    # Load battery profile
    profile = load_battery_profile(PROFILE_PATH)

    # Estimate SoC
    battery_data["SoC(%)"] = battery_data["Voltage(V)"].apply(
        lambda voltage: estimate_soc(voltage, profile)
    )

    # Display results
    print("\nBattery data loaded successfully!\n")
    print(battery_data.head())

    # Generate plots
    plot_voltage_vs_time(battery_data)
    plot_soc_vs_time(battery_data)

    # Export processed data
    export_soc_data(battery_data)


if __name__ == "__main__":
    main()