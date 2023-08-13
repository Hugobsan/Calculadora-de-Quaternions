from quaternion import Quaternion
from operacao import Operacao

def callMenu():
    print("-"*50)
    print("Menu de Opções:")
    print("\n")
    print("1. Definir Novo Quaternion")
    print("2. Exibir Quaternion")
    print("3. Listar Quaternions")
    print("4. Operação Personalizada")
    print("5. Sair")
    print("-"*50)
    print("\n")

    return int(input("Escolha uma opção: "))

def main():
    quaternions = []
    
    while True:
        choice = callMenu()
        
        if choice == 1:
            reserved_keys = ['i', 'j', 'k', 'm', 'c', 'v']
            print("\n")
            equacao = input("Insira o quaternion (ex: p = 1 + 2i + 3j - 4k): ")
            # separando o nome do quaternion
            nome, valores_str = equacao.split("=")
            nome = nome.strip()

            if nome in reserved_keys:
                print("\n")
                print("Nome inválido. Escolha outro nome.")
                continue
            
            # separando os valores do quaternion
            valores = valores_str.strip().split(" ")

            a = valores[0]
            b = ""
            c = ""
            d = ""

            for valor in valores[2:]:
                if 'i' in valor:
                    b = valor.replace("i", "")
                elif 'j' in valor:
                    c = valor.replace("j", "")
                elif 'k' in valor:
                    d = valor.replace("k", "")

            if valores[1] == "-":
                b = "-" + b
            if valores[3] == "-":
                c = "-" + c
            if valores[5] == "-":
                d = "-" + d

            new_q = Quaternion(nome, float(a), float(b), float(c), float(d))
            
            quaternions.append(new_q)
            quaternions.append(new_q.q_multi_i())
            quaternions.append(new_q.q_multi_j())
            quaternions.append(new_q.q_multi_k())
            quaternions.append(new_q.i_multi_q())
            quaternions.append(new_q.j_multi_q())
            quaternions.append(new_q.k_multi_q())
            quaternions.append(new_q.conjugado())
            quaternions.append(new_q.vetorial())

            print("\n")
            print("Quaternions definidos:")
            print("\n" + new_q.__str__() + "\n")

        elif choice == 2:
            if not quaternions:
                print("\n")
                print("Defina pelo menos um quaternion primeiro.")
            else:
                nome = input("Digite o nome do quaternion: ")
                for quaternion in quaternions:
                    if quaternion.nome == nome:
                        print("\n")
                        print("-"*50)
                        print(f"Quaternion {nome} encontrado:"+ "\n")
                        print(quaternion.__str__() + "\n")
                        print("Módulo: " + str(quaternion.modulo()) + "\n")
                        print("Conjugado: " + quaternion.conjugado().__str__() + "\n")
                        print(quaternion.q_multi_i().__str__() + "\n")
                        print(quaternion.q_multi_j().__str__() + "\n")
                        print(quaternion.q_multi_k().__str__() + "\n")
                        break
                    else:
                        print("Quaternion não encontrado.")
        elif choice == 3:
            if not quaternions:
                print("\n")
                print("Defina pelo menos um quaternion primeiro.")
            else:
                print('-'*50)
                print("\n")
                print("Quaternions definidos:")
                print("\n")
                for quaternion in quaternions:
                    print(quaternion.__str__() + "\n")
        elif choice == 4:
            if not quaternions:
                print("\n")
                print("Defina pelo menos um quaternion primeiro.")
            else:
                print("\n")
                operacao = input("Digite a equação a ser realizada: ")
                partes = operacao.split()
                operadores = ["+", "-", "*", "/"]
                quat_operados = []
                
                for parte in partes:
                    for quaternion in quaternions:
                        if parte == quaternion.nome:
                            quat_operados.append(quaternion)
                    if parte.isnumeric():
                        quat_operados.append(parte)
                    if parte in operadores:
                        operador = parte
                resultado = Operacao(quat_operados[0], operador, quat_operados[1])
                print("\n")
                print("Resultado da operação: " + resultado.calcular().__str__())

        elif choice == 5:
            print("\n")
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    print("Bem vindo ao programa de Quaternions!\n")
    main()
