# -- coding: utf-8 --

Created on Thu Mar 31 13:23:38 2022

init

@author: nicosio

import math

# Creamos una clase class Vector:

# Un contructor es un metodo que se invoca automaticamente cuando # el objeto es creado/instanciado

# El constructor en python es el metodo new, pero se usa solamente

# en casos avanzados

# El metodo init tambien se invoca automaticamente en el proces

# de instanciacion y es la opcion preferida para llevar a cabo

# las inicializaciones del objeto en python

def _init_(self, x, y): # Colocamos los atributos

self.x=x

self.y=y

# Creamos otro metodo

def Muestra(self): print(self.x, self.y)

# Y un metodo que regrese un valor

def magnitud(self):

return math.sqrt(self.x*2+self.y*2)

# Creamos el objeto

# Ya no necesitamos invocar a inicializa manualmente

# Simplemente pasamos los parametros al instanciar el objeto

v1=Vector (4,5)
