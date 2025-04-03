from calculadora import soma, subtracao, multiplicacao, divisao
from matematica_avancada import potencia, raiz_quadrada, fatorial

def saudacao():
    print("Olá, bem-vindo à calculadora Python avançada!")

def exibir_menu():
    print("\nOperações disponíveis:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Sair")

if __name__ == "__main__":
    saudacao()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma operação (1-8): ")
        
        if opcao == '8':
            print("Obrigado por usar a calculadora!")
            break
            
        try:
            if opcao in ['1', '2', '3', '4', '5']:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: ")) if opcao != '5' else int(input("Digite o expoente: "))
                
                if opcao == '1':
                    print(f"Resultado: {soma(a, b)}")
                elif opcao == '2':
                    print(f"Resultado: {subtracao(a, b)}")
                elif opcao == '3':
                    print(f"Resultado: {multiplicacao(a, b)}")
                elif opcao == '4':
                    print(f"Resultado: {divisao(a, b)}")
                elif opcao == '5':
                    print(f"Resultado: {potencia(a, b)}")
            elif opcao == '6':
                a = float(input("Digite o número para calcular a raiz: "))
                print(f"Resultado: {raiz_quadrada(a)}")
            elif opcao == '7':
                a = int(input("Digite o número para calcular o fatorial: "))
                print(f"Resultado: {fatorial(a)}")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite números válidos.")