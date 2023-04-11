import xml.etree.ElementTree as ET

# Открытие файла для записи
with open("1_resultReverse.txt", "w", encoding='utf-8') as f:
    # Загрузка файла XML
    tree = ET.parse('1_forReverse.xml')
    root = tree.getroot()

    # Получение значения атрибута sku для каждого элемента offer
    for offer in root.iter('offer'):
        sku = offer.get('sku')
        print(sku, end='\t')

        # Получение значений элементов model и brand
        model = offer.find('model').text
        brand = offer.find('brand').text
        f.write(sku + "\t" + model + "\t" + brand + "\t")
        print(model, end='\t')
        print(brand, end='\t')


        # Получение значений элементов cityprice для каждого элемента cityprices
        for cityprice in offer.findall(".//cityprice[@cityId='591010000']"):
            city_id = cityprice.get('cityId')
            price = cityprice.text
            f.write(price + "\n")
            print(price, end='\t\n')