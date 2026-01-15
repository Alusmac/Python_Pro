import requests
import xml.etree.ElementTree as ET


def save_page_xml(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        root = ET.Element("page")
        ET.SubElement(root, "url").text = url
        ET.SubElement(root, "content").text = response.text

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        print(f"Сторінку збережено у XML: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}")
