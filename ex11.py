def encontrar_primos(n):
    # Inicializa uma lista de booleanos representando se cada número é primo ou não
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False  # 0 e 1 não são primos
    
    # Percorre os números de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:  # Se i é primo
            # Marca todos os múltiplos de i como não primos
            for j in range(i*i, n + 1, i):
                primos[j] = False
    
    # Retorna uma lista dos números primos
    return [i for i in range(2, n + 1) if primos[i]]

def main():
    try:
        n = int(input("Digite um número natural: "))
        primos = encontrar_primos(n)
        for primo in primos:
            print(primo)
    except ValueError:
        print("Por favor, digite um número natural válido.")

if __name__ == "__main__":
    main()
