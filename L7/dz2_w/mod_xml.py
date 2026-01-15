import xml.etree.ElementTree as etr


def save_xml(filename: str, root_tag: str, data: dict) -> None:
    """Saving file in xml
    """
    try:
        root = etr.Element(root_tag)
        for key, value in data.items():
            elem = etr.SubElement(root, key)
            elem.text = str(value)

        tree = etr.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print(f"[OK] XML saved: {filename}")

    except Exception as e:
        print(f"[Error] Cann not save in XML: {e}")


def load_xml(filename: str) -> dict:
    """Reading XML file.
    """
    try:
        tree = etr.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}

    except Exception as e:
        print(f"[Error] Cann not reading from XML: {e}")
        return {}
