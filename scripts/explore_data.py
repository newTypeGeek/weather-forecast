import matplotlib.pyplot as plt
import pandas as pd
import os


output_dir = os.path.join("..", "results", "eda")
os.makedirs(output_dir, exist_ok=True)

file_path_to_setting = {
    "../data/preprocessed_data/outdoor_temp.csv": {
        "title": "Outdoor Temperature",
        "ylabel": "Temperature (°C)",
        "output_file_path": os.path.join(output_dir, "outdoor_temp.png"),
    },
    "../data/preprocessed_data/outdoor_rh.csv": {
        "title": "Outdoor RH",
        "ylabel": "RH (%)",
        "output_file_path": os.path.join(output_dir, "outdoor_rh.png"),
    },
}


for file_path, setting in file_path_to_setting.items():
    with open(file_path, "r") as f:
        df = pd.read_csv(f)

    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index)

    print("Percentage of missing data = {:.2f}%".format(df.isna().sum().sum() / df.size * 100))

    fig, ax = plt.subplots(figsize=(14, 6))

    df.plot(ax=ax)

    ax.set_ylabel(setting["ylabel"], fontsize=14)
    ax.set_xlabel(ax.get_xlabel(), fontsize=14)
    ax.set_title(setting["title"], fontsize=16)

    plt.savefig(setting["output_file_path"], bbox_inches="tight")
