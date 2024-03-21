from enum import Enum

"""---------------
NUMERACIONES
------------------"""

class tipo(Enum):
    PAPELERIA = 1
    SUPERMERCADO =2
    FARMACIA =3
    

class Producto :
    __subsidio = False
    __calidad = 'A'
    __ivaDrogueria = 0.17
    __ivaSupermercado = 0.4
    __ivaPapeleria = 0.19
    
""" ___________________
CONSTANTES
_____________________"""

precioMaximo = 50000000    

"""____________________
Atributos
_________________________"""
__tipo = Enum('Tipo',['PAPELERIA','SUPERMERCADO','FARMACIA'])
__nombre= None
__valorUnitario = 0.0
__cantidadBodega = 0
__cantidadUnidadMinina = 0
__cantidadUnidadesVendidas = 0

"""____________________
Metodos
_________________________"""

def getNombre(self):
    self.__nombre
    
def getValorUnitario(self):
    self.__valorUnitario

def CantidadBodega(self):
    self.__cantidadBodega

def CantidadUnidadMinima(self):
    self.__cantidadUnidadMinima
    
def CantidadUnidadesVendidas(self):
    self.__cantidadUnidadesVendidas

    

    
def ejemplo(self):
    tipoVenta = self,__tipo.PAPELERIA