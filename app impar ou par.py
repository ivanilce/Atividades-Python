#Projeto.par.ou.impar
while True:
    try:
        valor = int(input('Digite um valor:'))
        if valor % 2 == 0:
            print('Número Par')
        else:
            print('Número Ímpar')
            
    except:
        print('Digite apenas números!')

