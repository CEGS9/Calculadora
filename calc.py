print("Calculadora")
primeiroNumero = int(input("Insira o primeiro número: "))
print("Escolha o operador aritmético:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
acao = int(input())
segundoNumero = int(input("Insira o segundo número: "))

if acao == 1:
    resultado = primeiroNumero + segundoNumero
elif acao == 2:
    resultado = primeiroNumero - segundoNumero
elif acao == 3:
    resultado = primeiroNumero * segundoNumero
elif acao == 4:
    if segundoNumero != 0:
        resultado = primeiroNumero / segundoNumero
    else:
        print("0")
        resultado = None
else:
    print("0")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)