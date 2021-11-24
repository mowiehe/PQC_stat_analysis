import xml.etree.ElementTree as ET
import os


def get_filelist(path, extension=".xml"):
    # creates a list of files with mathching extension, located anywhere under path
    filenames = []
    for root, dirs, files in os.walk(path):
        xml_files = [
            filename for filename in files if os.path.splitext(filename)[1] == extension
        ]
        for xml_file in xml_files:
            filenames.append(root + os.sep + xml_file)
    return filenames


def read_xmlfile(filename="dict.xml", stdout=False):
    # open xml file and read file content
    tree = ET.parse(filename)
    root = tree.getroot()
    if stdout:
        print(ET.tostring(root, encoding="utf8").decode("utf8"))
    return tree, root


def element_tag(xml_element):
    # turns an xml-elemant into a dictonary
    # usually: xml_element[0] now: xml_element['tag_name']
    # careful, does not work with identical tags
    return {e.tag: e for e in xml_element}


def element_tags(xml_element, tag_list):
    # access elements in xml-files by tag names
    # does not work with identical tags
    # use: element_tags(root, ["DATA_SET", "PART", "NAME_LABEL"]).text
    current = xml_element
    for tag in tag_list:
        current = element_tag(current)[tag]
    return current


def get_pqc_data(root):
    # parse pqc data and obtain measurement results
    # get device ID
    pqc_dict = {
        "NAME_LABEL": element_tags(root, ["DATA_SET", "PART", "NAME_LABEL"]).text,
    }

    # get struct data
    el_struct_data = element_tags(
        root,
        [
            "DATA_SET",
            "DATA",
        ],
    )
    struct_pars = [i.tag for i in el_struct_data.getchildren()]
    for i, par in enumerate(struct_pars):
        pqc_dict[par] = element_tags(el_struct_data, [par]).text

    # get PQC data
    el_data = element_tags(
        root,
        [
            "DATA_SET",
            "CHILD_DATA_SET",
            "DATA_SET",
            "CHILD_DATA_SET",
            "DATA_SET",
            "DATA",
        ],
    )
    pars = [i.tag for i in el_data.getchildren()]
    for i, par in enumerate(pars):
        pqc_dict[par] = float(element_tags(el_data, [par]).text)

    return pqc_dict
