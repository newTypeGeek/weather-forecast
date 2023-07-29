import loguru
import numpy as np
import pandas as pd


def read_raw_data(file_path: str) -> pd.DataFrame:
    with open(file_path, "r") as f:
        # skip the first 2 rows since those are metadata
        df = pd.read_csv(f, skiprows=[0, 1])

    loguru.logger.success(
        "Successfully read raw data from csv file_path={file_path}", file_path=file_path
    )
    return df


def write_df_to_csv(df: pd.DataFrame, file_path: str) -> None:
    with open(file_path, "w") as f:
        df.to_csv(f, index=False)
    loguru.logger.success(
        "Successfully write dataframe to csv file_path={file_path}", file_path=file_path
    )


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
    df["date"] = df.apply(
        lambda x: f"{x['year']}-{str(int(x['month'])).zfill(2)}-{str(int(x['day'])).zfill(2)}",
        axis=1,
    )
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # we do not add timezone because HKT is chaanged from +07:36 to +08:00 in 1904
    # making it diffcult to parse DatetimeIndex

    # "***" represents missing data
    df = df.replace({"***": np.nan})

    # select only data_completeness is C
    df = df[df["data_completeness"] == "C"]

    # drop unused columns
    df = df.drop(columns=["year", "month", "day", "data_completeness"])
    df = df.dropna()

    # ensure timestamp is evenly spaced daily (since the raw data is supposed to be daily separated)
    df = df.set_index("date")
    df = df.resample("1D").first().reset_index()

    return df
