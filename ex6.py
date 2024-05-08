def main():
    try:
        n = int(input("Digite um número inteiro: "))
        if n < 0:
            print("Por favor, digite um número inteiro não negativo.")
            return
        
        for i in range(n + 1):
            print(i)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
