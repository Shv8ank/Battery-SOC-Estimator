from pathlib import Path

import pandas as pd


def load_battery_data(file_path: str) -> pd.DataFrame:
    """
    Load and validate battery discharge data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Validated battery data.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(path)

    required_columns = ["Time(s)", "Voltage(V)"]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.isnull().values.any():
        raise ValueError("Dataset contains missing values.")

    return df