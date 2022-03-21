def convert_to_float(a):
    try:
        return float(a)
    except ValueError:
        return a


def get_mean_std_rounded(mean, std):
    if std == 0 or np.isnan(std):
        mean_rounded = mean
        std_rounded = std
    elif int(std) > 1:  # e.g. 345 +/- 2
        mean_rounded = np.round(mean)
        std_rounded = np.round(std)
    elif int(std) == 1:  # e.g. 345.1 +/- 1.2
        mean_rounded = np.round(mean, 1)
        std_rounded = np.round(std, 1)
    elif int(std) == 0:
        # find the first non zero digit
        index = 1
        while int(10 ** index * std) <= 1:
            # increase index,
            # e.g. 345.03 +/- 0.12
            # or 345.0 +/- 0.2
            # or 345.03 +/- 0.02
            index += 1
        mean_rounded = np.round(mean, index)
        std_rounded = np.round(std, index)
    else:
        mean_rounded = np.nan
        std_rounded = np.nan
    return mean_rounded, std_rounded
