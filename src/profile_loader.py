from pathlib import Path

import pandas as pd


def load_battery_profile(profile_path: str) -> pd.DataFrame:
    """
    Load a battery voltage-to-SoC profile.
    """

    path = Path(profile_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Profile not found: {profile_path}"
        )

    profile = pd.read_csv(path)

    required_columns = [
        "Voltage(V)",
        "SoC(%)"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in profile.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if profile.isnull().values.any():
        raise ValueError(
            "Profile contains missing values."
        )

    return profile