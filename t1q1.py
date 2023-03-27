def contaCaracteres(entrada):
    return len(entrada)

def main():
    nome = input('Digite seu nome: ')
    print(f'Seu nome tem {contaCaracteres(nome)} caracteres.')

if __name__ == '__main__':
    main()