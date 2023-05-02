print('Este é um programa para a conversão de números de base decimal para Binário ou Hexadecimal')
#O programa está limitado à representações em 8 bits

a1 = input('Aperte ENTER para continuar.')
print('==='*25)
while True:
    num = int(input('Digite um número para converter:'))
    print('==='*25)

    print('Binário')
    print('Hexadecimal')

    base = (input('Selecione para qual base deseja converter:')).upper()
    while base != 'HEXADECIMAL' and base != 'BINÁRIO':
        base = input('Resposta Inválida. Tente novamente:').upper()
    print('==='*25)
    binumber = []
    hexnumber = []

    if base == 'BINÁRIO':
        if (num /2) >= 8:
            r = 8
        else:
            r= 4
        for i in range (r):
            quo = num // 2
            bi = num % 2
            binumber.append(bi)
            num = quo
        binumber.reverse()
        print(f'O número em binário é: {binumber}')

    elif base == 'HEXADECIMAL':
        print(f'O número {num} em Hexadecimal é:')
        overNine = ('A','B','C','D','E','F')
        if num / 16 >= 1:
            r = 2
        else:
            r = 1
        for j in range (r):
            quo = num // 16
            hexa = num % 16
            num = quo
            if hexa > 9:
                hexa = overNine[hexa-10]
            hexnumber.append(hexa)

        hexnumber.reverse()
        for hexan in hexnumber:
            print(f'{hexan}',end="")
    
    a2 = input('\nDeseja converter outro número?(S/N)').upper()
    if a2 == 'N':
        break    
       
        