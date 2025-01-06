def calc(x, y, operador):
    if operador == "soma":
        return(x + y)
    elif operador == "subtracao":
        return(x - y)
    elif operador == "multiplicacao":
        return(x * y)
    elif operador == "divisao":
        return(x / y)
    else:
        return(0)

resultado = calc(4, 7, "soma")
print(resultado)
