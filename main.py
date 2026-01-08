#Calculadora en python


def calc(n1,n2,sign):
    if sign == "+":
        return n1 + n2
    elif sign == "-":
        return n1 - n2
    elif sign == "*" or sign == "x":
        return n1 * n2
    elif sign == "/":
        return n1 / n2
    else:
        return f"{sign} no valido"

number1 = int(input("Coloca el primer numero: "))
number2 = int(input("Coloca el segundo numero: "))
signo = input("Coloca el signo: ")

call = calc(number1, number2, signo)
print(call)
