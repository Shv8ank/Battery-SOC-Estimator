from pathlib import Path

import pandas as pd

OUTPUT_DIR = Path("outputs/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def export_soc_data(data: pd.DataFrame) -> None:
    """
    Export battery data with estimated SoC.
    """

    output_file = OUTPUT_DIR / "battery_soc_results.csv"

    data.to_csv(output_file, index=False)

    print(f"Results exported to: {output_file}")