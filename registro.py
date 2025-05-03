from time import sleep
utl = str(input(("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
      "-     Registro Hopitalario    -\n"
      "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
      "-                             -\n"
      "-Gostaria de adicionar um     -\n"
      "-Registro ou buscar alguem?   -\n"
                 "-[R/B/N                       -\n"
                 "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
                 "")))
if utl == "R":
    print("0%")
    sleep(2)
    print("50%")
    sleep(2)
    print("100%")
    sleep(2)
    fich = str(input("Qual é o nome do ficheiro de registro?: "))
    file = open(f'{fich}.txt', "w")
    proceed = 1
    while proceed == 1:
        nome = str(input("Nome do utente? "))
        file.write(f'nome: {nome}/')
        idade = str(input("Quantos anos é que tem? "))
        file.write(f'idade: {idade}\n')
        con = str(input("Continuar? [Y/N]"))
        if con == "Y":
            proceed = 1
        else:
            print("Obrigado por usar")
            sleep(5)
            proceed = 0

elif utl == "B":
    print("0%")
    sleep(2)
    print("50%")
    sleep(2)
    print("100%")
    sleep(2)
    fich = str(input("Qual é o nome do ficheiro de registro?: "))
    file = open(f'{fich}.txt', "r")
    proceed = 1
    while proceed == 1:
        plv = input("Digite o utente a procurar: ")

        with open(f'{fich}.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                if plv in linha:
                    print(linha.strip())
else:
    print("Obrigado por usar")
    sleep(2)
    quit()

