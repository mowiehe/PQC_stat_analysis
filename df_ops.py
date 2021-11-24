import numpy as np
import pandas as pd
from . import parse_xml

data_columns = [
    "FET_PSS_VTH_V",
    "MOS_QUARTER_VFB_V",
    "MOS_QUARTER_CACC_PFRD",
    "MOS_QUARTER_TOX_NM",
    "MOS_QUARTER_NOX",
    "VDP_POLY_RSH_OHMSQR_x",
    "VDP_POLY_RSH_OHMSQR_y",
    "VDP_STRIP_RSH_OHMSQR_x",
    "VDP_STRIP_RSH_OHMSQR_y",
    "VDP_STOP_RSH_OHMSQR_x",
    "VDP_STOP_RSH_OHMSQR_y",
    "CAP_W_CAC_PFRD",
    "CAP_E_CAC_PFRD",
    "GCD_ISURF_PAMPR",
    "GCD_S0_CMSEC",
    "LINEWIDTH_STRIP_T_UM",
    "LINEWIDTH_STOP_T_UM",
    "DIEL_SW_VBD_V",
    "DIODE_HALF_I600_PAMPR",
    "DIODE_HALF_VD_V",
    "DIODE_HALF_RHO_KOHMCM",
    "DIODE_HALF_NA",
    "MEANDER_METAL_R_OHM",
    "CLOVER_METAL_RSH_OHMSQR_x",
    "CLOVER_METAL_RSH_OHMSQR_y",
    "VDP_EDGE_RSH_OHMSQR_x",
    "VDP_EDGE_RSH_OHMSQR_y",
    "VDP_EDGE_T_UM",
    "VDP_BULK_RSH_OHMSQR_x",
    "VDP_BULK_RSH_OHMSQR_y",
    "VDP_BULK_RHO_KOHMCM",
    "GCD05_ISURF_PAMPR",
    "GCD05_S0_CMSEC",
    "CBKR_POLY_R_OHM",
    "CBKR_STRIP_R_OHM",
    "CC_EDGE_R_OHM",
    "CC_POLY_R_OHM",
    "CC_STRIP_R_OHM",
]


def get_PQC_batch_tables(df):
    # create emtpy df with samplenames
    dfnew = df[["NAME_LABEL"]]
    dfnew = dfnew.drop_duplicates(["NAME_LABEL"])
    dfnew.reset_index(drop=True, inplace=True)

    ### KIND_OF_HM_FLUTE_ID, KIND_OF_HM_STRUCT_ID, KIND_OF_HM_CONFIG_ID, XML column name
    parlists = [
        ["PQC1", "FET_PSS", "Not Used", "VTH_V"],
        ["PQC1", "MOS_QUARTER", "Not Used", "VFB_V"],
        ["PQC1", "MOS_QUARTER", "Not Used", "CACC_PFRD"],
        ["PQC1", "MOS_QUARTER", "Not Used", "TOX_NM"],
        ["PQC1", "MOS_QUARTER", "Not Used", "NOX"],
        ["PQC1", "VDP_POLY", "STANDARD", "RSH_OHMSQR"],
        ["PQC1", "VDP_POLY", "ROTATED", "RSH_OHMSQR"],
        ["PQC1", "VDP_STRIP", "STANDARD", "RSH_OHMSQR"],
        ["PQC1", "VDP_STRIP", "ROTATED", "RSH_OHMSQR"],
        ["PQC1", "VDP_STOP", "STANDARD", "RSH_OHMSQR"],
        ["PQC1", "VDP_STOP", "ROTATED", "RSH_OHMSQR"],
        ["PQC1", "CAP_W", "Not Used", "CAC_PFRD"],
        ["PQC1", "CAP_E", "Not Used", "CAC_PFRD"],
        ["PQC2", "GCD", "Not Used", "ISURF_PAMPR"],
        ["PQC2", "GCD", "Not Used", "S0_CMSEC"],
        ["PQC2", "R_POLY", "Not Used", "RPOLY_MOHM"],
        ["PQC2", "LINEWIDTH_STRIP", "Not Used", "T_UM"],
        ["PQC2", "LINEWIDTH_STOP", "Not Used", "T_UM"],
        ["PQC2", "DIEL_SW", "Not Used", "VBD_V"],
        ["PQC3", "DIODE_HALF", "Not Used", "I600_PAMPR"],
        ["PQC3", "DIODE_HALF", "Not Used", "VD_V"],
        ["PQC3", "DIODE_HALF", "Not Used", "RHO_KOHMCM"],
        ["PQC3", "DIODE_HALF", "Not Used", "NA"],
        ["PQC3", "MEANDER_METAL", "Not Used", "R_OHM"],
        ["PQC3", "CLOVER_METAL", "STANDARD", "RSH_OHMSQR"],
        ["PQC3", "CLOVER_METAL", "ROTATED", "RSH_OHMSQR"],
        ["PQC3", "VDP_EDGE", "STANDARD", "RSH_OHMSQR"],
        ["PQC3", "VDP_EDGE", "ROTATED", "RSH_OHMSQR"],
        ["PQC3", "VDP_EDGE", "LINEWIDTH", "T_UM"],
        ["PQC3", "VDP_BULK", "STANDARD", "RSH_OHMSQR"],
        ["PQC3", "VDP_BULK", "ROTATED", "RSH_OHMSQR"],
        ["PQC3", "VDP_BULK", "STANDARD", "RHO_KOHMCM"],
        ["PQC4", "GCD05", "Not Used", "ISURF_PAMPR"],
        ["PQC4", "GCD05", "Not Used", "S0_CMSEC"],
        ["PQC4", "CBKR_POLY", "STANDARD", "R_OHM"],
        ["PQC4", "CBKR_STRIP", "STANDARD", "R_OHM"],
        ["PQC4", "CC_EDGE", "Not Used", "R_OHM"],
        ["PQC4", "CC_POLY", "Not Used", "R_OHM"],
        ["PQC4", "CC_STRIP", "Not Used", "R_OHM"],
    ]

    for parlist in parlists:

        if parlist[3] in df.keys():
            single_entry = df.loc[
                (df["KIND_OF_HM_FLUTE_ID"] == parlist[0])
                & (df["KIND_OF_HM_STRUCT_ID"] == parlist[1])
                & (df["KIND_OF_HM_CONFIG_ID"] == parlist[2])
                & (
                    np.isnan(df[parlist[3]]) == False
                ),  # relevant to separate IV/CV on Diode Half
                [
                    "NAME_LABEL",
                    parlist[3],
                ],
            ]
            single_entry = single_entry.rename(
                columns={parlist[3]: parlist[1] + "_" + parlist[3]}
            )
            dfnew = dfnew.merge(single_entry, on="NAME_LABEL", how="left")

            if len(single_entry) != len(dfnew):
                print("Missing measurements for", parlist)
        else:
            print("No entry for", parlist)

    return dfnew


def drop_entry(df, droplist, column_name="NAME_LABEL"):
    df.drop(df.loc[df[column_name].isin(droplist)].index, inplace=True)
    return df


def get_stat_point(df, data_column, process_column, proc):
    # returns the relative mean and standarddeviation of process type with respect to the full data_set for a single data_column, needs to be executed for each data_column, for each process type
    full_mean = df[data_column].mean()
    full_std = df[data_column].std()
    proc_mean = df.loc[df[process_column] == proc, data_column].mean()
    proc_std = df.loc[df[process_column] == proc, data_column].std()

    if full_std == 0 and proc_mean == full_mean:  # no variation in the data
        relative_mean = 0
        relative_std = 0
    else:  # usual case
        relative_mean = (proc_mean - full_mean) / full_std
        relative_std = proc_std / full_std

    return relative_mean, relative_std


def get_stat_graph(df, data_columns, process_column, proc):
    # returns arrays of relative mean and standarddeviation for a list of data_columns, for a single process type
    stat_points = [
        get_stat_point(df, data_column, process_column, proc)
        for data_column in data_columns
    ]
    relative_means = np.transpose(stat_points)[0]
    relative_stds = np.transpose(stat_points)[1]
    return relative_means, relative_stds


def get_full_df(path, process_info=None):
    # reads all xml files under path and exctracts PQC parameters, returns dataframe
    print("Reading all xml-files under", path, "and extracting PQC parameters")
    filenames = parse_xml.get_filelist(path)  # get all xml files

    # parse xml files and create dataframe
    pqc_dicts = []
    for i, f in enumerate(filenames):
        tree, root = parse_xml.read_xmlfile(filename=f, stdout=False)
        pqc_dicts.append(parse_xml.get_pqc_data(root))
    df = pd.DataFrame(pqc_dicts)
    df = df.sort_values("NAME_LABEL")
    if process_info:
        df = add_process_info(df, process_info)
    df = get_PQC_batch_tables(df)  # reduce table to significant values
    return df


def add_process_info(df, process_info, merge_on="NAME_LABEL", sep="\t"):
    print("Adding proccess info from", process_info)
    pi = pd.read_csv(process_info, sep=sep, dtype="object")  # open process information
    df = df.merge(pi, how="left", on=merge_on)  # add process info to dataframe

    print(df[["NAME_LABEL"] + [i for i in pi.keys()]])
    return df
