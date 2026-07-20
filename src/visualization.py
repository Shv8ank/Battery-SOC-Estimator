from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = Path("outputs/plots")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_voltage_vs_time(data: pd.DataFrame) -> None:
    """
    Plot battery voltage against time.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        data["Time(s)"],
        data["Voltage(V)"],
        linewidth=2,
        label="Voltage"
    )

    plt.title("Battery Voltage vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "voltage_vs_time.png")

    plt.close()


def plot_soc_vs_time(data: pd.DataFrame) -> None:
    """
    Plot estimated SoC against time.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        data["Time(s)"],
        data["SoC(%)"],
        linewidth=2,
        label="Estimated SoC"
    )

    plt.title("Estimated State of Charge vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("State of Charge (%)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "soc_vs_time.png")

    plt.close()