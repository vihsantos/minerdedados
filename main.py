import csv


def change_values(lista):

    for dicionario in lista:
        for chave, valor in dicionario.items():
            if valor == "sim":
                dicionario.update({chave: 1})

            if valor == "não":
                dicionario.update({chave: 0})


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
    path = str(input("Digite o caminho do arquivo csv: "))

    lista = csv_to_list(path)

    keys = list(lista[0].keys())
    del keys[0]

    contador = 1
    for key in keys:
        print(f"Item {contador}: {key}")
        contador += 1

    index_item1 = int(input("Digite o valor do primeiro item escolhido:\n Por exemplo: Se você escolher o item 1, "
                            "o valor esperado é: 1.\n "))

    index_item2 = int(input("Digite o valor do segundo item:\n"))

    question = int(input("Deseja calcular confiança ou suporte?\n"
                         "Digite 1 para 'SUPORTE'.\n"
                         "Digite 2 para 'CONFIANÇA'.\n"))

    # confianca = calcular_confianca(lista, index_item1, index_item2)
    # suporte = calcular_suporte(lista, index_item1, index_item2)


main()
