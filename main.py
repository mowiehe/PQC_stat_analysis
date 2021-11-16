import pandas as pd
import matplotlib.pyplot as plt
from .scripts import parse_xml, pqc_measurement, plotter, df_ops


def get_full_df(path, process_info=None):
    # reads all xml files under path and exctracts PQC parameters, returns dataframe
    filenames = parse_xml.get_filelist(path)  # get all xml files

    # parse xml files and create dataframe
    pqc_dicts = []
    for i, f in enumerate(filenames):
        tree, root = parse_xml.read_xmlfile(filename=f, stdout=False)
        pqc_dicts.append(parse_xml.get_pqc_data(root))
    df = pd.DataFrame(pqc_dicts)
    df = df.sort_values("NAME_LABEL")
    df = df_ops.get_PQC_batch_tables(df)  # reduce table to significant values
    if process_info:
        pi = pd.read_csv(process_info, sep="\t")  # open process information
        df = df.merge(pi, on="NAME_LABEL")  # add process info to dataframe

        print(
            df[
                [
                    "NAME_LABEL",
                    "P-stop-layout",
                    "Thickness",
                    "Vfb",
                    "Oxide",
                    "P-stop",
                    "Proc.",
                ]
            ]
        )
    return df


def box_plot(df, plot_data_columns=None, plot_process_column=None, out_folder=""):
    if not plot_data_columns:  # if none selected, plot all
        plot_data_columns = [
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

    # create boxplots and save to file
    for plot_data_column in plot_data_columns:
        fig, ax = plotter.boxplot(df, plot_data_column, plot_process_column)
        print(df[["NAME_LABEL", plot_data_column, plot_process_column]])

        out_file = out_folder + plot_data_column + "_" + plot_process_column + ".png"
        print("save plot to", out_file)
        plt.savefig(out_file)

    plt.show()
