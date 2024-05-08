def main():
    try:
        n = int(input("Digite um número inteiro: "))
        d = int(input("Digite um divisor: "))
        
        # Lista comprehension para gerar os múltiplos de d de 1 até n
        multiplos = [x for x in range(1, n + 1) if x % d == 0]

        # Imprime os múltiplos em uma linha, separados por vírgula
        print(','.join(map(str, multiplos)), end='')
    except ValueError:
        print("Por favor, digite valores inteiros válidos.")

if __name__ == "__main__":
    main()
