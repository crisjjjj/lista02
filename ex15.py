def main():
    numeros = []

    while True:
        entrada = input("Digite um número ou 's' para sair: ")
        
        if entrada.lower() == 's':
            break
        
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

    print(numeros)

if __name__ == "__main__":
    main()
