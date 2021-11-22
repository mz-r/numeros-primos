núm = int(input('Digite um número: '))
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

