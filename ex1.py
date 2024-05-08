def calcular_imc(massa, altura):
    return massa / (altura ** 2)

def classificar_situacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso adequado"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    try:
        massa = float(input("Digite a massa da pessoa (em kg): "))
        altura = float(input("Digite a altura da pessoa (em metros): "))
        
        imc = calcular_imc(massa, altura)
        situacao = classificar_situacao(imc)
        
        print(situacao)
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()
