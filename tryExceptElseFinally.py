def abrirArquivo():
    try:
        arquivo =  open("test.text","r")
    except FileNotFoundError:
        print("o arquivo nao foi encontrado")
    else:
        print(arquivo.read())
    finally:
        print("fim da tentativa de acesso ao arquivo")

abrirArquivo()
