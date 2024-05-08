def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        ano = int(input("Digite um ano: "))
        if eh_bissexto(ano):
            print("bissexto")
        else:
            print("normal")
    except ValueError:
        print("Por favor, digite um ano válido.")

if __name__ == "__main__":
    main()
