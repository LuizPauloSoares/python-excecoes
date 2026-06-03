def divisao(n1):
    try:
        n2 = 0
        return n1/n2
    except ZeroDivisionError as e :
        print(f"erro {e} nao pode dividir por zero")
        return None

resultado1=divisao(5)

print(resultado1)

print("\n ========================================= \n")

def divisao2 (n1,n2):
    try:
       resultado = int (n1/n2)
    
    except ZeroDivisionError as e :
        print(f"erro {e} nao pode dividir por zero")

    else:
        print(resultado)

    finally:
        print("muito obrigado por participar")

n1 =int (input("me fale um numero : "))
n2 =int (input("me fale outro numero : "))

divisao2(n1,n2)