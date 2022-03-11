import numpy as np
import matplotlib.pyplot as plt
from . import df_ops
from . import plot_options
import pdb
import helper as hp
import scipy.stats


def prepare_data(df, data_column, process_column):
    # extracts data from df according to given column names and applies filters
    # output are arrays with corresponding data and label
    options = plot_options.plot_options
    xlabel = options[data_column][0]
    value_mult = options[data_column][1]
    xmin = options[data_column][2]
    xmax = options[data_column][3]

    # get all options from process_column
    proc = list(set(df[process_column]))
    proc.sort()
    data = []
    label = []
    overflow = []
    failed = []
    for i in proc:  # loop over selected process splits, e.g. oxide type A,B,C,..
        i_data_all = np.array(df.loc[(df[process_column] == i), data_column])
        i_data_all = i_data_all * value_mult  # changing unit
        i_data = i_data_all[
            (i_data_all >= xmin) & (i_data_all <= xmax) & ~np.isnan(i_data_all)
        ]  # filtering
        i_overflow = i_data_all[
            ~np.isin(i_data_all, i_data) & ~np.isnan(i_data_all)
        ]  # all values in original data, which did not pass the filter, excluding nans
        i_failed = len(i_data_all[np.isnan(i_data_all)])

        data.append(i_data)
        overflow.append(i_overflow)
        failed.append(i_failed)

        if len(i_data) == 0:
            mean, std = np.nan, np.nan
        else:
            mean, std = hp.get_mean_std_rounded(i_data.mean(), i_data.std())
        label.append(process_column + " " + str(i) + f" ({mean} / {std})")
    return data, label, xlabel, overflow, failed


def boxplot(df, data_column, process_column):
    # creates a single boxplot of data in data_column for different process variants
    # change plot options
    data, label, xlabel, overflow, failed = prepare_data(
        df, data_column, process_column
    )
    fig, ax = plt.subplots()
    n, bins, _ = ax.hist(data, label=label, rwidth=1.0, histtype="barstacked", bins=20)
    ax.set_xlabel(xlabel)
    #   ax.set_xlim(xmin, xmax)
    ax.set_ylabel("Occurences")
    total_data = sum([len(i) for i in data])
    total_overflow = sum([len(i) for i in overflow])
    total_failed = sum(failed)
    ax.legend(title="Type, (mean / std.)")
    ax.set_title(
        f"Plotted: {total_data}, overflow: {total_overflow}, failed: {total_failed}"
    )
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
        if save_file:
            out_file = (
                out_folder + plot_data_column + "_" + plot_process_column + ".png"
            )
            print("save plot to", out_file)
            plt.savefig(out_file)
            plt.close()


def get_correlations(df, plot_data_columns):
    # return paired plot data columns and corresponding correlations
    pairs = []
    correlations = []
    for i in plot_data_columns:
        for j in plot_data_columns:
            # make sure no pair is evaluated twice
            this_pair = [i, j]
            if (
                any([all([col in pair for col in this_pair]) for pair in pairs])
                or i == j
            ):
                continue

            fig, ax, r, p = correlation_plot(
                df, i, j, process_column="NAME_LABEL", plot=False
            )
            correlations.append(r)
            pairs.append(this_pair)
    return pairs, correlations


def correlation_plot(
    df,
    data_column_x,
    data_column_y,
    process_column="NAME_LABEL",
    plot=False,
    out_folder="",
    save_file=True,
):
    # creates a correlation_plot of two data_columns for different process variants
    # change plot options
    label_x, value_mult_x, min_x, max_x = plot_options.plot_options[data_column_x]
    label_y, value_mult_y, min_y, max_y = plot_options.plot_options[data_column_y]

    df = df.copy()
    df = df[
        ~np.isnan(df[data_column_x]) & ~np.isnan(df[data_column_y])
    ]  # get rid of nans
    df[data_column_x] = df[data_column_x] * value_mult_x  # change units x
    df[data_column_y] = df[data_column_y] * value_mult_y  # change units y
    df = df[(df[data_column_x] >= min_x) & (df[data_column_x] <= max_x)]  # limit in x
    df = df[(df[data_column_y] >= min_y) & (df[data_column_y] <= max_y)]  # limit in y

    r, p = scipy.stats.pearsonr(df[data_column_x], df[data_column_y])

    if plot:
        fig, ax = plt.subplots()

        # get all options from process_column
        proc = list(set(df[process_column]))
        proc.sort()

        for i in proc:
            label = process_column + " " + str(i)
            ax.plot(
                data_column_x,
                data_column_y,
                "o",
                data=df[df[process_column] == i],
                label=label,
            )

        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        if (
            process_column != "NAME_LABEL"
        ):  # only show legend if process_column is given
            ax.legend(title=f"Pearson-r: {np.round(r,2)}")
        if save_file:
            out_file = (
                out_folder
                + data_column_x
                + "_"
                + data_column_y
                + "_"
                + process_column
                + ".png"
            )
            print("save plot to", out_file)
            plt.savefig(out_file)
            plt.close()

    else:
        fig, ax = None, None

    return fig, ax, r, p


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
