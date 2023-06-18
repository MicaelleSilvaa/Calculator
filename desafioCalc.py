# Exibe o cabeçalho e o menu de opções
def exibir_menu():
    print('Bem-vindo(a) à calculadora!')
    print('Qual operação deseja:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')

# Funções para as quatro operações básicas
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return 'Não é possível dividir por zero!'

# Lê a opção do usuário
def ler_opcao():
    opcao = int(input('Digite o número da operação desejada: '))
    if opcao == 0:
        print('Até logo!')
    elif opcao in [1, 2, 3, 4]:
        print('Vamos prosseguir')
    else:
        print('Opção inválida')
    return opcao


# Lê os números digitados pelo usuário
def ler_numeros():
    num1 = float(input('\nDigite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    return num1, num2

# Executa a operação escolhida pelo usuário
def calcular(opcao, num1, num2):
    resultado = None

    if opcao == 1:
        resultado = soma(num1, num2)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = divisao(num1, num2)
    elif opcao == 0:
        print('Encerrando a calculadora.')
        return
    else:
        resultado = "Operação inválida!"

    print("\nResultado:", resultado, '\n')

# Controla o fluxo da calculadora
def main():
    while True:
        exibir_menu()
        opcao = ler_opcao()
        if opcao == 0:
            break
        elif opcao in [1, 2, 3, 4]:
            num1, num2 = ler_numeros()
            calcular(opcao, num1, num2)
        else:
            print('Tente novamente.\n')

main()