import requests
import json
from datetime import date

"""
JSON que no funcionan:

https://api.nytimes.com/svc/books/v3/lists.json
https://api.nytimes.com/svc/books/v3/reviews.json

"""
api_key = "iXlGurXUvuIxi2QCHhlWD3nMh7e7pLeg"

lists = "https://api.nytimes.com/svc/books/v3/lists.json"
review = "https://api.nytimes.com/svc/books/v3/reviews.json"
names = "https://api.nytimes.com/svc/books/v3/lists/names.json"

# date_list = f"https://api.nytimes.com/svc/books/v3/lists/{date}/{list}.json"


class BestSellers:
    def __init__(self):
        self.key = "iXlGurXUvuIxi2QCHhlWD3nMh7e7pLeg"
        self.listas = []
        self.listaSelect = ""
        self.jsonLista = ""
        self.jsonAge = []
        self.jsonPrice = []

    def get_lista(self):
        lists = "https://api.nytimes.com/svc/books/v3/lists/names.json"
        x = requests.get(f"{lists}?api-key={self.key}")
        xRestults = json.loads(x.text)["results"]
        for i in xRestults:
            self.listas.append(i["list_name"])

    def show_lista(self):
        cont = 1
        for i in self.listas:
            print(f"{cont}: {i}")
            cont += 1
        listaSelect = int(input("Ingresa una opción: "))
        print(f"\nElegiste: {self.listas[listaSelect - 1]}\n")
        self.listaSelect = self.listas[listaSelect - 1]

    def get_fecha(self):
        print("1: Fecha actual\n2: Fecha específica")
        op = int(input("Ingresa una opción: "))
        if op == 1:
            fecha = str(date.today())
            print(f"\nElegiste: Fecha actual\n")
        elif op == 2:
            print(f"\nElegiste: Fecha actual\n")
            fecha = input("Ingresa una fecha (YYYY-MM-DD): ")
            print(f"\nFecha: {fecha}\n")
        date_list = f"https://api.nytimes.com/svc/books/v3/lists/{fecha}/{self.listaSelect}.json"
        x = requests.get(f"{date_list}?api-key={self.key}")
        self.jsonLista = json.loads(x.text)["results"]

        # print(self.jsonLista)
        # json_object = json.dumps(self.jsonLista, indent=4)
        # with open("sample.json", "w") as outfile:
        #     outfile.write(json_object)

    def set_price(self):
        price = float(input("Ingresa un precio: "))
        price = round(price, 2)
        price = str(price)
        for i in self.jsonLista["books"]:
            if i["price"] == "0.00":
                self.jsonPrice.append(i)
        print()

    def set_age(self):
        age1 = input("Ingresa la edad menor de tu rango: ")
        age2 = input(
            "Ingresa la edad mayor de tu rango (escribe 'up' si no hay máximo): "
        )
        if age2 == "up":
            ageFull = f"Ages {age1} and up"
        elif age1 == "" and age2 == "":
            ageFull = ""
        elif age1 != "" and age2 != "up":
            ageFull = f"Ages {age1} to {age2}"

        for i in self.jsonPrice:
            if ageFull == i["age_group"]:
                self.jsonAge.append(i)

    def show_data(self):
        print("\n-------------------------------")
        print(f"Lista:{self.listaSelect}\n")
        for i in self.jsonAge:
            print("Title: " + i["title"])
            print("Author: " + i["author"])
            print("Age: " + i["age_group"])
            print("Price: " + i["price"])
            print("Links:")
            for j in i["buy_links"]:
                print("\t" + j["name"] + ": " + j["url"])
            print()

    def main(self):
        self.get_lista()
        self.show_lista()
        self.get_fecha()
        self.set_price()
        self.set_age()
        self.show_data()


bs = BestSellers()
bs.main()
