import numpy as np
import matplotlib.pyplot as plt


def boxplot(df, data_column, process_column=None):
    # get all options from process_column
    if process_column:
        proc = set(df[process_column])
        data = []
        label = []
        for i in proc:
            i_data = np.array(df.loc[(df[process_column] == i), data_column])
            i_data = np.array([d for d in i_data if not np.isnan(d)])  # delete nans
            data.append(i_data)
            label.append(process_column + " " + str(i))
    else:
        data = np.array(df.loc[:, data_column])
        label = "All"

    fig, ax = plt.subplots()
    n, bins, _ = ax.hist(data, label=label, rwidth=1.0)
    ax.set_xlabel(data_column)
    ax.set_ylabel("Occurences")

    ax.legend()
    return fig, ax
