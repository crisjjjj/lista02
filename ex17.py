import math

def aplicar_funcao(numero, opcao):
    if opcao == 1:
        return int(math.factorial(numero))
    elif opcao == 2:
        return int(math.sqrt(numero))
    else:
        return numero

def main():
    numeros = []

    while True:
        entrada = input("Digite um número inteiro positivo ou 's' para sair: ")
        
        if entrada.lower() == 's':
            break
        
        try:
            numero = int(entrada)
            if numero > 0:
                numeros.append(numero)
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    if not numeros:
        print("Nenhum número foi digitado.")
    else:
        opcao = int(input("Digite 1 para aplicar factorial ou 2 para aplicar sqrt: "))
        if opcao not in [1, 2]:
            print("Opção inválida. Por favor, escolha 1 ou 2.")
        else:
            resultado = [aplicar_funcao(num, opcao) for num in numeros]
            print("Lista resultante:", resultado)

if __name__ == "__main__":
    main()
