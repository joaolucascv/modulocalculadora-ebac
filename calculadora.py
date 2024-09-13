class Calculadora(object):
    def __init__(self) -> None:
      pass    

    def somar() -> float:
        from functools import reduce
        valores = []
        contagem = 1
        valor = input(f"Insira o {contagem}º valor: ")
        
        while valor != "":
            try:
                valor = float(valor)
                valores.append(valor)
                contagem += 1
                valor = input(f"Insira o {contagem}º valor ou pressione 'Enter' para somar tudo: ")
            except ValueError:
                print("Erro: Deve ser um valor numérico ")
                valor = input("Insira o valor numérico novamente: ")