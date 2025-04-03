from calculadora import soma, subtracao, multiplicacao, divisao

def saudacao():
    print("Olá, bem-vindo à calculadora Python!")

def exibir_menu():
    print("\nOperações disponíveis:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

if __name__ == "__main__":
    saudacao()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma operação (1-5): ")
        
        if opcao == '5':
            print("Obrigado por usar a calculadora!")
            break
            
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                print(f"Resultado: {soma(a, b)}")
            elif opcao == '2':
                print(f"Resultado: {subtracao(a, b)}")
            elif opcao == '3':
                print(f"Resultado: {multiplicacao(a, b)}")
            elif opcao == '4':
                print(f"Resultado: {divisao(a, b)}")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite números válidos.")