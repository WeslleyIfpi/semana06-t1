def maior_menor(numero, maior = -999999999999, menor = 99999999999, total=0):
    if numero > maior:
        maior = numero
 
    if numero < menor:
        menor = numero
    total += numero

    return maior, menor , total

def main():
    maior = -999999999999
    menor = 999999999999
    total = 0
    for i in range(5): 
        entrada = int(input('Difite um número: '))
        maior, menor, total = maior_menor(entrada, maior, menor, total)
    media = total / 5
    print(f'O maior número: {maior}')
    print(f'O menor número: {menor}')
    print(f'média: {media}')

if __name__ == '__main__':
    main()