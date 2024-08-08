class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mostrar(self):
        print(f"Las coordenadas del puunto son ({self.x} y {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x )**2 + (self.y - otro_punto.y)**2)

class Circulo:
    def __int__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    def contiene_punto(self, punto):
        self.centro.calcular_distancia(punto) <= self.radio


class Carta:
    CORAZONES = "Corazones"
    TREBOLES = "Tréboles"
    PICAS = "picas"
    DIAMANTES = "Diamante"
    def __init__(self,valor,pinta):
        self.valor = valor
        self.pinta = pinta
class CuentaBancaria:
    def __init__(self,numero_cuentas,proíetarios,balance):
        self.numero_cuentas = numero_cuentas
        self.propietarios = proíetarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto

    def retirar(self,monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("Fondos insuficientes")
    def aplicar_cuota_manejo(self):
        self.balance -= self.balance * 0.02

    def mostrar_detalles(self):
        print(f"Numero de cuenta: {self.numero_cuentas}")
        print(f"Propietario:{self.propietarios}")
        print(f"Blance:{self.balance}")

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        ancho = abs(self.punto1.x - self.punto2.x )
        alto = abs(self.punto1 - self.punto2.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1 - self.punto2.y)
        return ancho * alto

class Cuadrado:
    def es_cuadrado(self):
        return abs(self.punto.x - self.punto2.x) == abs(self.punto.y - self.punto2.y)


