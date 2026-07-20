import numpy as np


# Voltage-to-SoC lookup table
VOLTAGE_POINTS = np.array([
    3.20,
    3.40,
    3.60,
    3.80,
    4.00,
    4.20
])

SOC_POINTS = np.array([
    0,
    20,
    40,
    60,
    80,
    100
])


def estimate_soc(voltage: float) -> float:
    """
    Estimate battery State of Charge (SoC)
    from voltage using linear interpolation.
    """

    soc = np.interp(
        voltage,
        VOLTAGE_POINTS,
        SOC_POINTS
    )

    return round(float(soc), 2)