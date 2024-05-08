def main():
    print("Digite os valores para calcular seus quadrados. Digite 's' para sair.")

    while True:
        entrada = input("Digite um valor ou 's' para sair: ")
        
        if entrada.lower() == 's':
            break
        
        try:
            valor = float(entrada)
            quadrado = valor ** 2
            print(quadrado)
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    main()
