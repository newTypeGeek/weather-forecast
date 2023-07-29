import argparse
import os

import schema
import loguru
import constants
import data_preprocessor


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--mode", type=schema.Mode, choices=list(schema.Mode))

    args = arg_parser.parse_args()

    if args.mode == schema.Mode.PREPROCESS:
        loguru.logger.info("Preprocessing raw data")

        # outdoor temperature
        df_raw_temp = data_preprocessor.read_raw_data(
            constants.RAW_OUTDOOR_TEMP_DATA_FILE_PATH
        )
        df_preprocessed_temp = data_preprocessor.preprocess_data(df_raw_temp)

        # outdoor relative humidity
        df_raw_rh = data_preprocessor.read_raw_data(
            constants.RAW_OUTDOOR_RH_DATA_FILE_PATH
        )
        df_preprocessed_rh = data_preprocessor.preprocess_data(df_raw_rh)

        # output preprocessed data to csv
        os.makedirs(constants.PREPROCESSED_DATA_DIR, exist_ok=True)
        data_preprocessor.write_df_to_csv(
            df_preprocessed_temp, constants.PREPROCESSED_OUTDOOR_TEMP_DATA_FILE_PATH
        )
        data_preprocessor.write_df_to_csv(
            df_preprocessed_rh, constants.PREPROCESSED_OUTDOOR_RH_DATA_FILE_PATH
        )
