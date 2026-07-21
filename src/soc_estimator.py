import numpy as np
import pandas as pd


def estimate_soc(
    voltage: float,
    profile: pd.DataFrame
) -> float:
    """
    Estimate battery State of Charge (SoC)
    using a voltage profile.
    """

    voltage_points = profile["Voltage(V)"].to_numpy()
    soc_points = profile["SoC(%)"].to_numpy()

    soc = np.interp(
        voltage,
        voltage_points,
        soc_points
    )

    return round(float(soc), 2)