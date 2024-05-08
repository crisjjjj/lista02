def main():
    try:
        n = int(input("Digite um número inteiro: "))
        
        for i in range(1, n + 1):
            if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0 and i % 11 == 0 and i % 13 == 0:
                print(i)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
