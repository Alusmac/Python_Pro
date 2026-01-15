from L7.dz2_w import *

download_page("https://pythonleiden.nl/meeting-2026-01-22.html", "dz2.txt")

save_csv("dz2.csv", [["name", "age", "hobby"], ["Emma", 35, "tennis"]])
print(load_csv("dz2.csv"))

save_json("dz2.json", {"name": "Tonny", "age": 40, "hobby": "football"})
print(load_json("dz2.json"))

save_xml("dz2.xml", "person", {"name": "Grit", "age": 50, "hobby": "books"})
print(load_xml("dz2.xml"))
