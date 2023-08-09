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
            print("\n")
            nome  = input("Como chamaremos o novo quaternion? ")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de bi: "))
            c = float(input("Digite o valor de cj: "))
            d = float(input("Digite o valor de dk: "))
            
            quaternions.append(Quaternion(nome, a, b, c, d))
            print("\n")
            print("Quaternion definido:")
            print("\n" + quaternions[-1].__str__() + "\n")
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
