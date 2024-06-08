#!/usr/bin/python3
"""Module for XML manipulation"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Function to serialize dictionary into XML"""

    # Creating the root element
    root = ET.Element('data')

    # Converting the dictionary into Element
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Converting tree to ElementTree
    tree = ET.ElementTree(root)

    # Writing content to the file
    tree.write(filename)


def deserialize_from_xml(filename):
    """Function to deserialize XML file into dictionary"""

    # Parsing the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}

    # Converting data into dictionary
    for child in root:
        data[child.tag] = child.text
    return data
