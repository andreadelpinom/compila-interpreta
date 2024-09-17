import random
#a = 10
#b = 15
#s = a+b 
#print("La suma es: ", s)


#Actividad en clase: 

#Ingresar 10 valores por teclado. Presentar la suma y promedio

valor1 = input(int("Ingresa un valor1: "))
valor2 = input(int("Ingresa un valor2: "))
valor3 = input(int("Ingresa un valor3: "))
valor4 = input(int("Ingresa un valor4: "))
valor5 = input(int("Ingresa un valor5: "))
valor6 = input(int("Ingresa un valor6: "))
valor7 = input(int("Ingresa un valor7: "))
valor8 = input(int("Ingresa un valor8: "))
valor9 = input(int("Ingresa un valor9: "))
valor10 = input(int("Ingresa un valor10: "))
sum = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9 + valor10
print("La suma es: ", sum)
print("El promedio es: ", sum/10)

#Generar 500 valores aleatorios entre 50 y 100. Presente cuantos valores pares y cuantos impares fueron generados. 

valor = 0
while valor < 5:
    for numero in range(1, 5):
        if numero % 2 == 0:
            sumPar = sumPar + numero  # Suma el número par a sumPar
        if numero % 2 == 1:
            sumImpar = sumImpar + numero  # Suma el número impar a sumImpar
    valor = valor + 1

print("Final Par: ", sumPar)
print("Final Impar: ", sumImpar)


#Genere 2 arreglos paralelos que representen las sucursales de una empresa y sus ventas. Existen 25 sucursales en la empresa
#Presente el promedio de ventas, asi como las curusales con ventas mayores al promedio. 

sucursales = list(range(1, 26))
ventas = [random.randint(1000, 10000) for _ in range(25)]

promedio_ventas = sum(ventas) / 25

print(f"Promedio de ventas: {promedio_ventas:.2f}\n")
print("Sucursales con ventas mayores al promedio:")
for i in range(25):
    if ventas[i] > promedio_ventas:
        print(f"Sucursal {sucursales[i]}: {ventas[i]}")









