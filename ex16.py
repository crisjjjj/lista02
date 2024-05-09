def main():
    resultado = 0

    while True:
        entrada = input("Digite um número inteiro positivo ou 's' para sair: ")
        
        if entrada.lower() == 's':
            break
        
        try:
            numero = int(entrada)
            if numero <= 0:
                print("Por favor, digite um número inteiro positivo.")
                continue
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
        
        resultado ^= numero
    
    print(resultado)

if __name__ == "__main__":
    main()
