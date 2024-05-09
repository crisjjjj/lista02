def main():
    lista1 = ler_lista("primeira")
    lista2 = ler_lista("segunda")

    numeros_comuns = set(lista1) & set(lista2)

    print("Números que aparecem em ambas as listas:")
    print(list(numeros_comuns))

def ler_lista(numero_lista):
    lista = []
    while True:
        entrada = input(f"Digite um número inteiro para a {numero_lista} lista ou 's' para encerrar: ")
        if entrada.lower() == 's':
            break
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    return lista

if __name__ == "__main__":
    main()
