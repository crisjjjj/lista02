import math

def calcular_medias(n1, n2, n3):
    # Média Aritmética
    media_aritmetica = (n1 + n2 + n3) / 3
    
    # Média Harmônica
    media_harmonica = 3 / ((1/n1) + (1/n2) + (1/n3))
    
    # Média Geométrica
    media_geometrica = math.pow((n1 * n2 * n3), (1/3))
    
    # Média Quadrática
    media_quadratica = math.sqrt((n1**2 + n2**2 + n3**2) / 3)
    
    return media_aritmetica, media_harmonica, media_geometrica, media_quadratica

def main():
    try:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))
        
        if n1 <= 0 or n2 <= 0 or n3 <= 0:
            print("As notas devem ser maiores que zero.")
            return
        
        medias = calcular_medias(n1, n2, n3)
        menor_media = min(medias)
        maior_media = max(medias)
        
        print("Menor :", menor_media)
        print("Maior :", maior_media)
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()
