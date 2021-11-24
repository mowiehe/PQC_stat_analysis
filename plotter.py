import numpy as np
import matplotlib.pyplot as plt
from . import df_ops


def boxplot(df, data_column, process_column=None):
    # creates a single boxplot of data in data_column for different process variants
    # get all options from process_column
    if process_column:
        proc = set(df[process_column])
        data = []
        label = []
        for i in proc:  # loop over selected process splits, e.g. oxide type A,B,C,..
            i_data = np.array(df.loc[(df[process_column] == i), data_column])
            i_data = np.array([d for d in i_data if not np.isnan(d)])  # delete nans
            data.append(i_data)
            label.append(process_column + " " + str(i))
    else:
        data = np.array(df.loc[:, data_column])
        label = "All"

    fig, ax = plt.subplots()
    n, bins, _ = ax.hist(data, label=label, rwidth=1.0, histtype="barstacked")
    ax.set_xlabel(data_column)
    ax.set_ylabel("Occurences")

    ax.legend()
    return fig, ax


def boxplots(
    df, plot_data_columns=None, plot_process_column=None, out_folder="", save_file=True
):
    # creates boxplots for set of data_columns (or all) and saves to file
    if not plot_data_columns:  # if none selected, plot all
        plot_data_columns = df_ops.data_columns

    # create boxplots and save to file
    for plot_data_column in plot_data_columns:
        fig, ax = boxplot(df, plot_data_column, plot_process_column)
        print(df[["NAME_LABEL", plot_data_column, plot_process_column]])
        if save_file:
            out_file = (
                out_folder + plot_data_column + "_" + plot_process_column + ".png"
            )
            print("save plot to", out_file)
            plt.savefig(out_file)


def stat_plot(
    df, plot_data_columns, plot_process_column, out_folder="", save_file=True
):
    proc = list(set(df[plot_process_column]))
    proc.sort()

    fig, ax = plt.subplots(figsize=(14, 8))

    for i in proc:
        relative_means, relative_stds = df_ops.get_stat_graph(
            df, plot_data_columns, plot_process_column, i
        )

        ax.errorbar(
            plot_data_columns,
            relative_means,
            yerr=relative_stds,
            fmt="o",
            label=plot_process_column + " " + str(i),
            capsize=3,
        )

    ax.set_ylabel("Deviation from the mean / std.dev.", fontsize=16)
    ax.set_xticks(list(range(len(plot_data_columns))))
    ax.set_xticklabels(plot_data_columns, rotation=45, ha="right")  # ha="right"
    ax.grid()
    ax.legend()
    fig.tight_layout()

    if save_file:
        out_file = out_folder + "stat_" + plot_process_column + ".png"
        print("save plot to", out_file)
        plt.savefig(out_file)
