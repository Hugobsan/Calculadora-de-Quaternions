from quaternion import Quaternion

class Operacao:
    def __init__(self, quaternion, operador, valor):
        self.quaternion = quaternion
        self.operador = operador
        self.valor = valor
    
    def calcular():
        ##caso a operação seja de quatérnion/escalar
        new_quaternion = Quaternion('t', valor, valor, valor, valor)
        
        if self.operador == '+':
            a = self.quaternion.a + new_quaternion.a
            b = self.quaternion.b + new_quaternion.b
            c = self.quaternion.c + new_quaternion.c
            d = self.quaternion.d + new_quaternion.d

        elif self.operador == '-':
            a = self.quaternion.a - new_quaternion.a
            b = self.quaternion.b - new_quaternion.b
            c = self.quaternion.c - new_quaternion.c
            d = self.quaternion.d - new_quaternion.d

        elif self.operador == '*':
            a = self.quaternion.a * new_quaternion.a
            b = self.quaternion.b * new_quaternion.b
            c = self.quaternion.c * new_quaternion.c
            d = self.quaternion.d * new_quaternion.d
            
        elif self.operador == "/":
            a = self.quaternion.a / new_quaternion.a
            b = self.quaternion.b / new_quaternion.b
            c = self.quaternion.c / new_quaternion.c
            d = self.quaternion.d / new_quaternion.d
    
        return Quaternion('r', a, b, c, d)