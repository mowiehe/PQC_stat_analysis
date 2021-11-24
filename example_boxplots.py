from PQC_stat_analysis import df_ops, plotter
import numpy as np
import pdb
import matplotlib.pyplot as plt


#####
path_to_data = "/home/mw/cernbox/HEPHY_data/PQC/HGC/analysis_ProtoA_Nov21/"
process_info = (
    "/home/mw/cernbox/HEPHY_data/PQC/HGC/ANALYSIS_ProtoA_Nov21/process_info.csv"
)
plot_process_column = "Oxide-type"
out_folder = "/home/mw/cernbox/HEPHY_data/PQC/HGC/ANALYSIS_ProtoA_Nov21/OUT/"

droplist = ["HPK_HGCPROTO-A_N4790_2_LR", "HPK_HGCPROTO-A_N4791_7_UL"]

plot_data_columns = [
    "FET_PSS_VTH_V",
    "MOS_QUARTER_VFB_V",
    "MOS_QUARTER_CACC_PFRD",
    "MOS_QUARTER_TOX_NM",
    "MOS_QUARTER_NOX",
    # "VDP_POLY_RSH_OHMSQR_x",
    # "VDP_POLY_RSH_OHMSQR_y",
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
    # "CBKR_POLY_R_OHM",
    "CBKR_STRIP_R_OHM",
    "CC_EDGE_R_OHM",
    # "CC_POLY_R_OHM",
    "CC_STRIP_R_OHM",
]
#####

df = df_ops.get_full_df(path_to_data)

# obtain scratch_pad ID
df["Scratch_pad_ID"] = [i.split("_")[2] for i in df["NAME_LABEL"]]

df = df_ops.drop_entry(df, droplist)

df = df_ops.add_process_info(df, process_info, merge_on="Scratch_pad_ID", sep=",")

# plotter.boxplots(
#     df,
#     plot_data_columns=plot_data_columns,
#     plot_process_column=plot_process_column,
#     out_folder=out_folder,
# )

plotter.stat_plot(
    df, plot_data_columns, plot_process_column, out_folder=out_folder, save_file=True
)

plt.show()
