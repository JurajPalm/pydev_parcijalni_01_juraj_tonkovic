#Datoteka u kojoj zelim imati kod vezan uz klase

class Product:
    def __init__(self, 
                 name: str,
                 price: float,
                 description =''):
        self.name = name
        self.price = price
        self.description = description
    #nakon unosa argumenata za funkciju def__init__, Python prvo kreira varijablu self u koju sprema unesene podatke o objektu
    #Python zatim zapisuje kreirani objekt u varijablu self na način koji definira funkcija def__repr__(self)
    #Python zatim dodijeljuje varijabli self zeljeni naziv objekta (npr. laptop)
    #svaki objekt se pohranjuje na svoju lokaciju u memoriji
    def __repr__(self) -> str: #repr je posebna metoda (funkcija unutar klase) koja reprezentira objekt klase kao string
        return f'repr Naziv: {self.name}'
