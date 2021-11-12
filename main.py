import numpy as np
import pdb
import pandas as pd
import os
from scripts import parse_xml, pqc_measurement, plotter

#####
path = "/home/mw/cernbox/HEPHY_data/PQC/analysis_September21/"
#####


filenames = parse_xml.get_filelist(path)

pqc_dicts = []
for i, f in enumerate(filenames):
    tree, root = parse_xml.read_xmlfile(filename=f, stdout=False)
    pqc_dicts.append(parse_xml.get_pqc_data(root))

reduced = parse_xml.reduce_data(
    pqc_dicts, {"KIND_OF_HM_FLUTE_ID": "PQC4", "PROCEDURE_TYPE": "N+ CBKR"}
)

parse_xml.print_dict(pqc_dicts, ["NAME_LABEL", "PROCEDURE_TYPE"])
