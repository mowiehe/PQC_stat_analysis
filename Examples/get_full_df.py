from PQC_stat_analysis import df_ops
import pandas as pd
import numpy as np

path_to_data = "./Data/"
process_info = "./Data/process_info.csv"

# The raw dataframe contains one row per xml file. Therefore each structure takes several rows and the data columns contain many nan-values. PQC identifiers like 'KIND_OF_HM_FLUTE_ID' or the measurement 'FILE_NAME' are included as data column. The 'raw_measurement' data is included in form of a dictionary. Useful for quick checks and debugging.

df_raw = df_ops.get_raw_df(path_to_data)


# The 'full' dataframe contains only a single row per structure. Column names are changed to identify the measured parameter and the pqc structure. Raw data is included in columns with '_raw' name.

df = df_ops.get_full_df(path_to_data)

# extract the scratch pad ID from the name label for merging with the process information
df["Scratch_pad_ID"] = [i.split("_")[2] for i in df["NAME_LABEL"]]

# Columns of process_info will be added to dataframe
df = df_ops.add_process_info(df, process_info, merge_on="Scratch_pad_ID", sep=",")
