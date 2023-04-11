import xml.etree.ElementTree as ET
from operator import eq

print("Чем займёмся?\n"
      "1 - Из карточек в XML\n"
      "2 - Из XML в TXT\n"
      "3 - Изменение цен")
choise = int(input("Ваш выбор: "))

if choise == 1:

    with open("0_forFormating.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()

    with open("0_resultFormating.xml", "w", encoding='utf-8') as file:
        file.write("<offers>\n")
        for line in lines:
            parts = line.strip().split("\t")

            sku = parts[0]
            model = parts[1]
            brand = parts[2]
            price = int(parts[3])
            day = 0
            if eq(brand.lower(), "ваша мебель"):
                day = 14
            elif eq(brand.lower(), "диана"):
                day = 10
            elif eq(brand.lower(), "миф"):
                day = 11
            elif eq(brand.lower(), "альфа"):
                day = 14
            elif eq(brand.lower(), "элегант"):
                day = 30
            elif eq(brand.lower(), "бтс"):
                day = 30
            elif eq(brand.lower(), "классик"):
                day = 22
            else:
                day = 30

            if price > 500000:
                shortDelivery = 30000
                normalDelivery = 40000
                longDelivery = 50000
                veryLongDelivery = 70000
            elif price < 500000 & price > 300000:
                shortDelivery = 30000
                normalDelivery = 40000
                longDelivery = 50000
                veryLongDelivery = 70000
            elif price < 300000 & price > 100000:
                shortDelivery = 30000
                normalDelivery = 40000
                longDelivery = 50000
                veryLongDelivery = 70000
            else:
                shortDelivery = 30000
                normalDelivery = 40000
                longDelivery = 50000
                veryLongDelivery = 70000
            print(sku, model, brand, day, "дней", price, "тг")

            # print(parts[0])
            # print(parts[1])
            # print(parts[2])
            # print(parts[3])
            file.write(f"<offer sku=\"{sku}\">\n")
            file.write(f"\t<model>{model}</model>\n")
            file.write(f"\t<brand>{brand}</brand>\n")
            file.write("\t<availabilities>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP1\" preOrder=\"{day + 4}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP2\" preOrder=\"{day}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP3\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP4\" preOrder=\"{day + 4}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP5\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP6\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP7\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP8\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP9\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP10\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP11\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP12\" preOrder=\"{day + 2}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP13\" preOrder=\"{day + 4}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP15\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP16\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP17\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP18\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP19\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP20\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP21\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP22\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP23\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP24\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP25\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP26\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP27\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP28\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP29\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP30\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP31\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP32\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP33\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP34\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP35\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP36\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP37\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP38\" preOrder=\"{day + 6}\"/>\n")
            file.write(f"\t\t<availability available=\"yes\" storeId=\"PP39\" preOrder=\"{day + 6}\"/>\n")
            file.write("\t</availabilities>\n")
            file.write(f"\t<cityprices>\n")
            file.write(f"\t\t<cityprice cityId=\"591010000\">{price}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"710000000\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"111010000\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"551010000\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"111810000\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"391010000\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"117020100\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"113220100\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"116651100\">{price + shortDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"351010000\">{price + normalDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"352410000\">{price + normalDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"750000000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"471010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"231010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"471810000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"151010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"271010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"511010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"431010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"316621100\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"311010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"191010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"512610000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"631010000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"632810000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"632210000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"552210000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"351610000\">{price + longDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"273620100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"551610000\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"153220100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"433220100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"391610000\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"633420100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"634030100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"394420100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"316220100\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t\t<cityprice cityId=\"352210000\">{price + veryLongDelivery}</cityprice>\n")
            file.write(f"\t</cityprices>\n")
            file.write("</offer>\n")
        file.write("</offers>\n")
elif choise == 2:

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

elif choise == 3:
    print(3)