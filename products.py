#Datoteka u kojoj zelim imati kod vezan uz klase

class Product:
    def __init__(self, 
                 name: str,
                 price: float,
                 description =''):
        self.name = name
        self.price = price
        self.description = description
              
    def __repr__(self) -> str:
        return f'repr Naziv: {self.name}'
