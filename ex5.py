def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def data_existe(dia, mes, ano):
    # Lista com o número de dias em cada mês
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verifica se o ano é bissexto e atualiza o número de dias de fevereiro
    if eh_bissexto(ano):
        dias_por_mes[2] = 29
    
    # Verifica se o mês e o dia estão dentro dos limites
    if mes < 1 or mes > 12 or dia < 1 or dia > dias_por_mes[mes]:
        return False
    else:
        return True

def main():
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        
        if data_existe(dia, mes, ano):
            print("existe")
        else:
            print("não existe")
    except ValueError:
        print("Por favor, digite valores inteiros válidos.")

if __name__ == "__main__":
    main()
