from PQC_stat_analysis import plotter
from get_full_df import df

import numpy as np
import matplotlib.pyplot as plt

plot_process_column = "Oxide-type"  # or e.g."Thickness"

out_folder = "./Output/"

plot_data_columns = [
    "FET_PSS_VTH_V",
    "MOS_QUARTER_VFB_V",
]
#####

plotter.boxplots(
    df,
    plot_data_columns=plot_data_columns,
    plot_process_column=plot_process_column,
    out_folder=out_folder,
)

plotter.stat_plot(
    df,
    plot_data_columns,
    plot_process_column,
    out_folder=out_folder,
    save_file=True,
)

plt.show()
