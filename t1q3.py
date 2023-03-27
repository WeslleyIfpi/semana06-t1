def segundosParaHMS(totalSegundos):
    horas = totalSegundos // 3600
    minutos = (totalSegundos % 3600) // 60
    segundos = (totalSegundos % 3600) % 60

    return f'{horas:02}:{minutos:02}:{segundos:02}'

def main():
    totalSegundos = int(input('Digite o total de segundos: '))
    print(f'Convertido :{segundosParaHMS(totalSegundos)}')

if __name__ == '__main__':
    main()