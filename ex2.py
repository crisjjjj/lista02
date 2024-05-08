import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

def main():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        
        raizes = calcular_raizes(a, b, c)
        
        if raizes is None:
            print("Nenhuma raiz")
        elif len(raizes) == 1:
            print("A raiz é", raizes[0])
        else:
            raizes_ordenadas = sorted(raizes)
            print("As raízes são", *raizes_ordenadas)
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()
