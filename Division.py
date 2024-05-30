def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"
    
print("4. Divisiónes")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Resultado:", division(num1, num2))