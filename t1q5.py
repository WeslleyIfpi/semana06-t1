def main():
    entrada = float(input('valor da compra: R$'))

    print(f'Valor a vista: R${entrada * 0.91:.2f}')
    print(f'Valor ema 5x: R${entrada / 5:.2f}')
    print(f'valor em 10x: R${(entrada * 1.17) / 10:.2f}')

if __name__ == '__main__':
    main()