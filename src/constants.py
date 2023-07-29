import os

BASE_DIR = os.path.join("..", "data")
RAW_DATA_DIR = os.path.join(BASE_DIR, "raw_data")

RAW_OUTDOOR_TEMP_DATA_FILE_PATH = os.path.join(RAW_DATA_DIR, "CLMTEMP_HKO_.csv")
RAW_OUTDOOR_RH_DATA_FILE_PATH = os.path.join(RAW_DATA_DIR, "daily_HKO_RH_ALL.csv")

PREPROCESSED_DATA_DIR = os.path.join(BASE_DIR, "preprocessed_data")
PREPROCESSED_OUTDOOR_TEMP_DATA_FILE_PATH = os.path.join(
    PREPROCESSED_DATA_DIR, "outdoor_temp.csv"
)
PREPROCESSED_OUTDOOR_RH_DATA_FILE_PATH = os.path.join(
    PREPROCESSED_DATA_DIR, "outdoor_rh.csv"
)
