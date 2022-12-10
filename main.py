import csv
def change_values(lista):

    for dicionario in lista:
        for chave, valor in dicionario.items():
            if valor == "sim":
                dicionario.update({chave: 1})

            if valor == "não":
                dicionario.update({chave: 0})


def show_keys(keys):
    del keys[0]

    contador = 1
    for key in keys:
        print(f"Item {contador}: {key}")
        contador += 1


def calcular_suporte(lista, key1, key2):

    quant_key1 = list(filter(lambda item: item[key1] == 1, lista)).__len__()

    quant_key2 = list(filter(lambda item: item[key2] == 1, lista)).__len__()

    suporte = (quant_key1+quant_key2)/lista.__len__()
    return suporte


def calcular_confianca(lista, key1, key2):

    quant_key1 = list(filter(lambda item: item[key1] == 1, lista)).__len__()

    quant_key2 = list(filter(lambda item: item[key2] == 1, lista)).__len__()

    confianca = (quant_key1+quant_key2)/quant_key1
    return confianca


def csv_to_list(path):
    dicts = []

    # read csv file
    with open(path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        leitor_de_csv = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in leitor_de_csv:
            # add this python dict in list
            dicts.append(row)

    change_values(dicts)

    return dicts


def main():
    menu = 0

    while menu != 3:
        menu = int(input("---------------- MENU ----------------\n"
                         "DIGITE '1' PARA CALCULAR SUPORTE\n"
                         "DIGITE '2' PARA CALCULAR CONFIANÇA\n"
                         "DIGITE '3' PARA SAIR\n"))

        if menu == 1:
            path = str(input("Digite o caminho do arquivo csv: "))
            lista = csv_to_list(path)
            keys = list(lista[0].keys())
            show_keys(keys)

            print("ATENÇÃO: O código do item é o seu número\n")
            cod_um = int(input("Informe o código do primeiro item: \n"))
            cod_dois = int(input("Informe o código do segundo item: \n"))

            suporte = calcular_suporte(lista, keys[cod_um], keys[cod_dois])

            print(f'O valor do suporte é: {suporte}')

        elif menu == 2:
            path = str(input("Digite o caminho do arquivo csv: "))
            lista = csv_to_list(path)
            keys = list(lista[0].keys())
            show_keys(keys)

            print("ATENÇÃO: O código do item é o seu número\n")
            cod_um = int(input("Informe o código do primeiro item: \n"))
            cod_dois = int(input("Informe o código do segundo item: \n"))

            confianca = calcular_confianca(lista, keys[cod_um], keys[cod_dois])

            print(f'O valor do confiança é: {confianca}')
        elif menu == 3:
            print("Finalizando a aplicação...")
        else:
            print("Você escolheu um número diferente do que está no MENU")


main()
