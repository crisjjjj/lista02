def calcular_fatorial(n):
    # Caso base: fatorial de 0 é 1
    if n == 0:
        return 1
    # Caso base: fatorial de 1 é 1
    elif n == 1:
        return 1
    # Caso recursivo: calcular o fatorial de n multiplicando n pelo fatorial de n-1
    else:
        return n * calcular_fatorial(n - 1)

def main():
    try:
        n = int(input("Digite um número inteiro: "))
        if n < 0:
            print("O fatorial não está definido para números negativos.")
        else:
            resultado = calcular_fatorial(n)
            print(resultado)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
