class idadeValidaError (Exception):
     pass

def validaIdade(idade):
    if idade <=0 or idade >150:
            raise idadeValidaError("idade incorreta ")
    elif (idade >=18):
        print("maior de idade ") 
    else:
         print("menor de idade")  

try:
    validaIdade(-1)
except idadeValidaError as e:
    print(f"erro  {e} ")
