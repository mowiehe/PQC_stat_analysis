import matplotlib.pyplot as plt

from get_full_df import df
from PQC_stat_analysis import plotter

plot_process_column = "Oxide-type"  # "Thickness"  # "P-Stop"  # "Oxide-type"
out_folder = "./Output/"

plot_data_columns = ["FET_PSS_VTH_V", "MOS_QUARTER_VFB_V", "VDP_STOP_RSH_OHMSQR_x"]
#####

# define correlation_plot manually
fig, ax, r, p = plotter.correlation_plot(
    df,
    data_column_x="FET_PSS_VTH_V",
    data_column_y="MOS_QUARTER_VFB_V",
    process_column=plot_process_column,
    plot=True,
    out_folder=out_folder,
    save_file=True,
)

# or automatically find correlation_plots

# calculate correlations for all pairs
pairs, correlations = plotter.get_correlations(df, plot_data_columns)

# plot only those pairs with a certain minimum correlation
min_corr = 0.5
for icorr, corr in enumerate(correlations):
    if abs(corr) > min_corr:
        i, j = pairs[icorr]
        fig, ax, r, p = plotter.correlation_plot(
            df,
            data_column_x=i,
            data_column_y=j,
            process_column=plot_process_column,
            plot=True,
            out_folder=out_folder,
            save_file=True,
        )
