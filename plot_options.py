import numpy as np

# [new_axis_label,value_multiplier,xmin,xmax]
plot_options = {
    "FET_PSS_VTH_V": ["FET threshold voltage [V]", 1, -np.inf, np.inf],
    "MOS_QUARTER_VFB_V": ["MOS flatband voltage [V]", 1, 1.5, 6],
    "MOS_QUARTER_CACC_PFRD": ["MOS accumulation cap. [pF]", 1, 50, 80],
    "MOS_QUARTER_TOX_NM": ["MOS oxide thickness [nm]", 1, 700, 800],
    "MOS_QUARTER_NOX": ["MOS $N_{ox}$ [1e10/$cm^{2}$]", 1e-10, 5, 30],
    # ## "VDP_POLY_RSH_OHMSQR_x":[],#not relevant for HGC
    # ## "VDP_POLY_RSH_OHMSQR_y":[],#not relevant for HGC
    "VDP_STRIP_RSH_OHMSQR_x": ["VDP n sheet res. [$\\Omega$/sq.]", 1, -np.inf, np.inf],
    "VDP_STRIP_RSH_OHMSQR_y": ["VDP n sheet res. [$\\Omega$/sq.]", 1, -np.inf, np.inf],
    "VDP_STOP_RSH_OHMSQR_x": [
        "VDP p-stop sheet res. [k$\\Omega$/sq.]",
        1e-3,
        -np.inf,
        np.inf,
    ],
    "VDP_STOP_RSH_OHMSQR_y": [
        "VDP p-stop sheet res. [k$\\Omega$/sq.]",
        1e-3,
        -np.inf,
        np.inf,
    ],
    "CAP_W_CAC_PFRD": ["CAP_W oxide capacitance [pF]", 1, -np.inf, np.inf],
    "CAP_E_CAC_PFRD": ["CAP_E oxide capacitance [pF]", 1, -np.inf, np.inf],
    "GCD_ISURF_PAMPR": ["GCD surface current [pA]", -1, -np.inf, np.inf],
    "GCD_S0_CMSEC": ["GCD generation velocity [cm/s]", 1, -np.inf, np.inf],
    "LINEWIDTH_STRIP_T_UM": ["Linewidth n [$\\mu$m]", 1, -np.inf, np.inf],
    "LINEWIDTH_STOP_T_UM": ["Linewidth p-stop [$\\mu$m]", 1, -np.inf, np.inf],
    "DIEL_SW_VBD_V": ["Oxide breakdown voltage [V]", 1, -np.inf, np.inf],
    "DIODE_HALF_I300_PAMPR": ["Diode current (300V) [nA]", 1e-3, 0, 5],
    "DIODE_HALF_I600_PAMPR": ["Diode current (600V) [$\\mu$A]", 1e-6, -np.inf, np.inf],
    "DIODE_HALF_VD_V": ["Diode depletion voltage [V]", 1, -np.inf, np.inf],
    "DIODE_HALF_RHO_KOHMCM": ["Diode resistance [k$\\Omega$cm]", 1, 0, 5],
    "DIODE_HALF_NA": ["Diode $N_{A}$ [$1e12/cm^{3}$]", 1, 2, 10],
    "MEANDER_METAL_R_OHM": ["Metal meander [$\\Omega$]", 1, -np.inf, np.inf],
    "CLOVER_METAL_RSH_OHMSQR_x": [
        "Metal clover sheet res. [m$\\Omega$/sq.]",
        1e3,
        -np.inf,
        np.inf,
    ],
    "CLOVER_METAL_RSH_OHMSQR_y": [
        "Metal clover sheet res. [m$\\Omega$/sq.]",
        1e3,
        -np.inf,
        np.inf,
    ],
    "VDP_EDGE_RSH_OHMSQR_x": [
        "VDP p-edge sheet res. [k$\\Omega$/sq.]",
        1e-3,
        -np.inf,
        np.inf,
    ],
    "VDP_EDGE_RSH_OHMSQR_y": [
        "VDP p-edge sheet res. [k$\\Omega$/sq.]",
        1e-3,
        -np.inf,
        np.inf,
    ],
    "VDP_EDGE_T_UM": [
        "VDP p-edge linewidth [$\\mu$m]",
        1,
        -np.inf,
        np.inf,
    ],
    "VDP_BULK_RSH_OHMSQR_x": [
        "VDP bulk sheet res. [k$\\Omega$/sq.]",
        1e-3,
        -np.inf,
        np.inf,
    ],
    "VDP_BULK_RSH_OHMSQR_y": [
        "VDP bulk sheet res. [k$\\Omega$/sq.]",
        1e-3,
        -np.inf,
        np.inf,
    ],
    "VDP_BULK_RHO_KOHMCM": [
        "VDP bulk resistance [k$\\Omega$cm]",
        1,
        -np.inf,
        np.inf,
    ],
    "GCD05_ISURF_PAMPR": ["GCD05 surface current [pA]", -1, -np.inf, np.inf],
    "GCD05_S0_CMSEC": ["GCD05 generation velocity [cm/s]", 1, -np.inf, np.inf],
    # ## "CBKR_POLY_R_OHM":[],#not relevant for HGC
    "CBKR_STRIP_R_OHM": ["CBKR n res. [$\\Omega$]", 1, -np.inf, np.inf],
    "CC_EDGE_R_OHM": ["Contact chain p-edge [k$\\Omega$]", 1e-3, -np.inf, np.inf],
    # ## "CC_POLY_R_OHM":[],#not relevant for HGC
    "CC_STRIP_R_OHM": ["Contact chain n [k$\\Omega$]", 1e-3, -np.inf, np.inf],
}
