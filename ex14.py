import math

def f(x):
    return x * math.sin(x) * math.log(x)

def calcular_integral(a, b, n):
    # Calcula o tamanho de cada subintervalo
    delta_x = (b - a) / n
    
    # Inicializa a soma da integral
    integral = 0
    
    # Calcula a soma de Riemann
    for i in range(1, n + 1):
        x_i = a + i * delta_x
        integral += f(x_i)
    
    # Multiplica pela largura do subintervalo
    integral *= delta_x
    
    return integral

def main():
    try:
        a = float(input("Digite o limite inferior do intervalo (a): "))
        b = float(input("Digite o limite superior do intervalo (b): "))
        
        # Calcula n grande o suficiente
        n = int((b - a) / 0.001)
        
        # Calcula a integral
        resultado = calcular_integral(a, b, n)
        
        print(resultado)
    except ValueError:
        print("Por favor, digite números reais válidos.")

if __name__ == "__main__":
    main()
