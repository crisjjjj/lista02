def main():
    print("Digite os números inteiros. Digite 's' para sair.")

    menor_numero = None

    while True:
        entrada = input("Digite um número inteiro ou 's' para sair: ")
        
        if entrada.lower() == 's':
            break
        
        try:
            numero = int(entrada)
            if menor_numero is None or numero < menor_numero:
                menor_numero = numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    if menor_numero is not None:
        print(menor_numero)
    else:
        print("Nenhum número foi digitado.")

if __name__ == "__main__":
    main()
