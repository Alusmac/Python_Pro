import xml.etree.ElementTree as ET

filename = "shop.xml"

tree = ET.parse(filename)
root = tree.getroot()

print("Products and quantities in stock:")
for product in root.findall("product"):
    name = product.find("name").text
    quantity = product.find("quantity").text
    print(f"- {name}: {quantity} pieces.")

for product in root.findall("product"):
    if product.find("name").text == "Milk":
        old_qty = int(product.find("quantity").text)
        product.find("quantity").text = str(old_qty + 20)
    if product.find("name").text == "Bread":
        old_qty = int(product.find("quantity").text)
        product.find("quantity").text = str(old_qty + 10)

tree.write(filename, encoding="utf-8", xml_declaration=True)
