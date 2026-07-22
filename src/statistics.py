import pandas as pd


def generate_summary(
    battery_data: pd.DataFrame,
    battery_profile: str
) -> dict:
    """
    Generate battery statistics.
    """

    summary = {
        "Battery Profile": battery_profile,
        "Initial Voltage": battery_data["Voltage(V)"].iloc[0],
        "Final Voltage": battery_data["Voltage(V)"].iloc[-1],
        "Average Voltage": battery_data["Voltage(V)"].mean(),
        "Initial SoC": battery_data["SoC(%)"].iloc[0],
        "Final SoC": battery_data["SoC(%)"].iloc[-1],
        "Average SoC": battery_data["SoC(%)"].mean(),
        "Samples": len(battery_data),
        "Duration": battery_data["Time(s)"].iloc[-1],
    }

    return summary


def print_summary(summary: dict) -> None:
    """
    Print battery analysis summary.
    """

    print("\n" + "=" * 35)
    print(" Battery Analysis Summary")
    print("=" * 35)

    for key, value in summary.items():
        if isinstance(value, float):
            print(f"{key:<20}: {value:.2f}")
        else:
            print(f"{key:<20}: {value}")