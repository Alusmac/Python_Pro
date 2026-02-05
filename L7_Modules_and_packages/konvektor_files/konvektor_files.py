import csv
import json
import xml.etree.ElementTree as ET


class CSVtoJSONConvector:
    def __init__(self, csv_file: str) -> None:
        self.csv_file = csv_file

    def convert(self):
        """Reads CSV
        """
        data = []
        with open(self.csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

    def save_json(self, json_file: str) -> None:
        """Convert from CSV to JSON and saving in file
        """
        data = self.convert()
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class JSONtoCSVConvector:
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file

    def convert(self):
        """Reads JSON
        """
        with open(self.json_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_csv(self, csv_file: str) -> None:
        """Convert from JSON to CSV and saving in file
        """
        data = self.convert()
        if not data:
            return
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class XMLtoJSONConvector:
    def __init__(self, xml_file: str):
        self.xml_file = xml_file

    def convert(self):
        """Reads XML
        """
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        data = []
        for elem in root.findall("product"):
            record = {}
            for child in elem:
                record[child.tag] = child.text
            data.append(record)
        return data

    def save_json(self, json_file: str) -> None:
        """Convert from XML to JSON and saving in file"""
        data = self.convert()
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    csv_adapter = CSVtoJSONConvector("../students.csv")
    csv_adapter.save_json("students.json")
    print("CSV → JSON Done!")

    json_adapter = JSONtoCSVConvector("students.json")
    json_adapter.save_csv("students_copy.csv")
    print("JSON → CSV Done!")

    xml_adapter = XMLtoJSONConvector("shop.xml")
    xml_adapter.save_json("shop.json")
    print("XML → JSON Done!")
