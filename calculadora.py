from quaternion import Quaternion

def callMenu():
    print("\nMenu de Opções:")
    print("1. Definir Novo Quaternion")
    print("2. Selecionar Quatérnion")
    print("3. Exibir todos os Quaternions")
    print("4. Operação Personalizada")
    print("5. Sair")

    return int(input("Escolha uma opção: "))

def calc_qe(operador, q1, valor_escalar):
    if operador == '+':
        a = q1.a + float(valor_escalar)
        b = q1.b + float(valor_escalar)
        c = q1.c + float(valor_escalar)
        d = q1.d + float(valor_escalar)
    elif operador == '-':
        a = q1.a - float(valor_escalar)
        b = q1.b - float(valor_escalar)
        c = q1.c - float(valor_escalar)
        d = q1.d - float(valor_escalar)
    elif operador == '*':
        a = q1.a * float(valor_escalar)
        b = q1.b * float(valor_escalar)
        c = q1.c * float(valor_escalar)
        d = q1.d * float(valor_escalar)
    elif operador == "/":
        a = q1.a / float(valor_escalar)
        b = q1.b / float(valor_escalar)
        c = q1.c / float(valor_escalar)
        d = q1.d / float(valor_escalar)
    
    return Quaternion('r', a, b, c, d)
        

#função para executar operações entre dois quaternions
def calc_qq(operador, q1, q2):
    if operador == '+':
        a = q1.a + q2.a
        b = q1.b + q2.b
        c = q1.c + q2.c
        d = q1.d + q2.d

    elif operador == '-':
        a = q1.a - q2.a
        b = q1.b - q2.b
        c = q1.c - q2.c
        d = q1.d - q2.d

    elif operador == '*':
        a = q1.a * q2.a
        b = q1.b * q2.b
        c = q1.c * q2.c
        d = q1.d * q2.d
        
    elif operador == "/":
        a = q1.a / q2.a
        b = q1.b / q2.b
        c = q1.c / q2.c
        d = q1.d / q2.d
    
    return Quaternion('r', a, b, c, d)

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
               
                
        elif choice == 5:
            print("\n")
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
