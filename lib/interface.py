def linha(tam=51):
    return "=" * tam


def cabecalho(txt):
    print()
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i, item in enumerate(lista):
        print(f"{i + 1} - {item}")
    print(linha())
    opc = int(input("Sua opção: "))
    return opc
