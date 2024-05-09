try:
    massa = float(input("Digite a massa da pessoa (em kg): "))
    altura = float(input("Digite a altura da pessoa (em metros): "))
    
    imc = massa / (altura ** 2)
    
    if imc < 18.5:
        print("Baixo peso")
    elif imc < 25:
        print("Peso adequado")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")
except ValueError:
    print("Por favor, digite valores numéricos válidos.")
