#Datoteka u kojoj zelim imati kod vezan uz pokretanje programa
#file iz kojeg zelim pokrenuti aplikaciju mora imati main funkciju
#ovisno iz kojeg file-a pokrenem aplikaciju, program će sve 'gledati' iz tog file-a, tj. prema kodu u tom file-u

import products as pr #izbjegavam isti naziv liste i modula products

def main():
    products = []

    laptop = pr.Product(
         'Laptop',
        800.00,
        '15-inch display, 8GB RAM, 256GB SSD') #svaka .py datoteka je modul; da bih pozvao klasu Product, moram prije napisati modul u kojem se ta klasa nalazi
    products.append(laptop)
    print(laptop) #pokrene se funkcija def__repr__ iz modula products

    smartphone = pr.Product(
        'Smartphone',
        500.00,
        '6-inch display, 128GB storage'
    )
    products.append(smartphone)
    print(smartphone)

    print(products)

    #svaki ispis vrijednosti se moze pretvoriti u tekstualni podatak

#name je varijabla koja postoji u svakom Python modulu (file-u)
#default vrijednost varijable name je naziv modula (ovdje main_cls_01)
#ovakva konstrukcija osigurava da se funkcija main pokrene samo u ovom modu (a ne ako napravimo import modula)
if __name__ == '__main__':
    main()