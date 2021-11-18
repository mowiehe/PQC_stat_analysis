import numpy as np


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
