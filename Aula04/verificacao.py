entrada = '1.21+3*4'
entrada_mod1 = entrada.replace('+', '|').replace('-','|').replace('*', '|').replace('/', '|')
entrada_mod2 = entrada_mod1.split('|')


for i in range(len(entrada_mod2)):
    print(entrada_mod2[i].replace('.', '1', 1).isnumeric())
    if not entrada_mod2[i].replace('.', '1', 1):
        controle = 1
        break
