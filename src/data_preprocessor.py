import numpy as np
import pandas as pd


def read_raw_data(file_path: str) -> pd.DataFrame:
    with open(file_path, "r") as f:
        # skip the first 2 rows since those are metadata
        df = pd.read_csv(f, skiprows=[0, 1])

    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # remove the last 3 rows since those are also metadata
    df = df.iloc[:-3, :]

    # rename columns without chinese characters
    df = df.rename(
        columns={
            "年/Year": "year",
            "月/Month": "month",
            "日/Day": "day",
            "數值/Value": "value",
            "數據完整性/data Completeness": "data_completeness",
        }
    )

    # format DatetimeIndex using year, month, day column
    df["timestamp"] = df.apply(
        lambda x: f"{x['year']}-{str(int(x['month'])).zfill(2)}-{str(int(x['day'])).zfill(2)}",
        axis=1,
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["timestamp"] = pd.DatetimeIndex(df["timestamp"]).tz_localize("Asia/Hong_Kong")

    # "***" represents missing data
    df = df.replace({"***": np.nan})

    # select only data_completeness is C
    df = df[df["data_completeness"] == "C"]

    # drop unused columns
    df = df.drop(columns=["year", "month", "day", "data_completeness"])
    df = df.dropna()

    return df
