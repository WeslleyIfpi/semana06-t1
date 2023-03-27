def paraASCII(entrada):
    return ord(entrada)

def main():
    caractere = input('Digite um caracte: ')
    print(f'Em ASCII: {paraASCII(caractere)}')

if __name__ == "__main__":
    main()