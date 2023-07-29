import pandas as pd


from pytorch_forecasting.data.timeseries import TimeSeriesDataSet


def df_from_csv(file_path: str) -> pd.DataFrame:
    with open(file_path, "r") as f:
        df = pd.read_csv(f)
    df["date"] = pd.DatetimeIndex(df["date"])
    return df


df_temp = (
    df_from_csv("../data/preprocessed_data/outdoor_temp.csv")
    .rename({"value": "temp"}, axis=1)
    .set_index("date")
)
df_rh = (
    df_from_csv("../data/preprocessed_data/outdoor_rh.csv")
    .rename({"value": "rh"}, axis=1)
    .set_index("date")
)

df_data = pd.concat([df_temp, df_rh], axis=1)
df_data = df_data.dropna()
df_data["month"] = df_data.index.month_name()

df_data = df_data.reset_index()


# encode timestamp to column time_idx
df_data["time_idx"] = df_data.index

training_cut_off = "2019-01-01"

training = TimeSeriesDataSet(
    data=df_data[lambda x: x["date"] < training_cut_off],
    time_idx="time_idx",
    target="temp",
    group_ids=["rh", "month"],
    max_encoder_length=365,
    min_prediction_idx=0,
    max_prediction_length=365 * 3,
    time_varying_known_categoricals=["month"],
    time_varying_unknown_reals=["temp", "rh"],
    allow_missing_timesteps=True,
)

print(training)
