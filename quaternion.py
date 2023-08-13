import math

# Hamiltonian Quaternions

# Hamilton chamou os números P = a + bi +cj + dk de quaternions e os denotou por H
# Onde a, b, c, d são números reais e i, j, k são números imaginários


class Quaternion:
    def __init__(self, nome, a, b, c, d):
        self.nome = nome
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # Retorna uma string representando o quaternion
    def __str__(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d

        a_str = a
        b_str = f"- {-b}" if b < 0 else f"+ {b}"
        c_str = f"- {-c}" if c < 0 else f"+ {c}"
        d_str = f"- {-d}" if d < 0 else f"+ {d}"

        return f"{self.nome} = {a_str} {b_str}i {c_str}j {d_str}k"

    # Calcula o módulo do quaternion
    def modulo(self):
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)
    
    # Calcular o escalar
    def escalar(self):
        return self.a
    
    # Calcular o vetorial
    def vetorial(self):
        return Quaternion('v'+self.nome, 0, self.b, self.c, self.d)

    # Calcula o conjugado do quaternion
    def conjugado(self):
        return Quaternion('c'+self.nome, self.a, -self.b, -self.c, -self.d)
    
    def q_multi_i(self):
        return Quaternion(self.nome+'i', -self.b, self.a, self.d, -self.c)

    def q_multi_j(self):
        return Quaternion(self.nome+'j', -self.c, -self.d, self.a, self.b)
    
    def q_multi_k(self):
        return Quaternion(self.nome+'k', -self.d, self.c, -self.b, self.a)
    
    def i_multi_q(self):
        return Quaternion('i'+self.nome, -self.b, self.a, -self.d, self.c)
    
    def j_multi_q(self):
        return Quaternion('j'+self.nome, -self.c, self.d, self.a, -self.b)
    
    def k_multi_q(self):
        return Quaternion('k'+self.nome, -self.d, -self.c, self.b, self.a)