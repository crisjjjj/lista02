def main():
    try:
        a = int(input("Digite o primeiro número inteiro (a): "))
        b = int(input("Digite o segundo número inteiro (b): "))

        # Usamos um loop for para iterar de a até b (inclusive)
        for num in range(a, b + 1):
            # Verificamos se o número é múltiplo de 3, de 5 e não é múltiplo de 7
            if num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
                print(num)
    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
