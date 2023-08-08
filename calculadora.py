from quaternion import Quaternion
from operacao import Operacao

def callMenu():
    print("\nMenu de Opções:")
    print("1. Definir Novo Quaternion")
    print("2. Selecionar Quatérnion")
    print("3. Exibir todos os Quaternions")
    print("4. Operação Personalizada")
    print("5. Sair")

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

            print("Quaternion definido!")
            print(quaternions[-1].__str__() + "\n")
        elif choice == 2:
            if not quaternions:
                print("\n")
                print("Defina pelo menos um quaternion primeiro.")
            else:
                nome = input("Digite o nome do quaternion: ")
                for quaternion in quaternions:
                    if quaternion.nome == nome:
                        print("\n")
                        print(f"Quaternion {nome} encontrado:"+ "\n")
                        print(quaternion.__str__() + "\n")
                        break
                    else:
                        print("Quaternion não encontrado.")
        elif choice == 3:
            if not quaternions:
                print("\n")
                print("Defina pelo menos um quaternion primeiro.")
            else:
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
                contador = 0

                for parte in partes:
                    if contador == 0:
                        if 
        elif choice == 5:
            print("\n")
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
