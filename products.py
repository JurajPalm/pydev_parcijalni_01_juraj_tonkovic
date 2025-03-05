#Datoteka u kojoj zelim imati kod vezan uz klase

class Product:
    def __init__(self, 
                 name: str,
                 price: float,
                 description =''):
        self.name = name
        self.price = price
        self.description = description
              
    def __repr__(self) -> str: #repr je posebna metoda (funkcija unutar klase) koja reprezentira objekt klase kao string
        return f'repr Naziv: {self.name}'
