# UNIVERSIDAD ESTATAL DE MILAGRO 
# OSCAR ALEXIS AGUIRRE BARBECH
# Ingenieria EN Software 
# 3 SEMESTRE A1

#tema 1

# EJERCICIOS DE LOGICA DE PROGRAMACION EN PYTHON 

# Ejercicio 1

Lista = ("Hola Mundo", "" , "Verdadero", "1", "c", "256", "8>19" )
print(Lista)

# En una colecciòn se guardarìa esos datos

#Ejercicio 2

#ejemplo
resultado = 2 *(4 - 10 + 8)/2* 36 *(1/2)
print(resultado)
print(type(resultado))

# El resultado estaria guardado en una variable de tipo Flotante (Float)

#Ejercicio 4

n1 = 5
n2 = 7

suma = n1 +n2 
resta = n1 - n2
multi = n1 * n2
div = n1 / n2
modulo = n1 % n2

print(suma)
print(resta)
print(multi)
print(div)
print(modulo)

# Ejercicio 5
import math

a = 5
b = 7
c = 9

#Formula General
disc = b * b - 4 * a * c
raiz = math.sqrt(disc)
#Raices discriminantes
x_1 = (-b + raiz) / (2 * a)
x_2 = (-b - raiz) / (2 * a)

print("Las soluciones son: ", x_1 , x_2)

#Ejercicio 6 

c1 = 5
c2 = 7

hipotenusa = math.sqrt((c1**2) + (c2**2))
print("Hipotenusa: ", hipotenusa)


#Ejercicio 7

numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("0")
else:
    print("1")

#Ejercicio 9

lista=[]
for x in range(4):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

repeticion = lista.count(1)
if repeticion % 2 == 0:
    print("El codigo de paridad es 1")
else:
    print("El codigo de paridad es 0")

#Ejercicio 10

numero_binario = int(input("Ingrese un numero binario de 4 digitos"))

numero_decimal = 0 

for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion

print("El número decimal que buscamos es: ", numero_decimal)

#Ejercicio 11

numero = int(input("Ingrese un numero entero de 4 digitos: "))
umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print("Unidades de millar: %i" % umil)
print("Centenas: %i" % centenas)
print("Decenas: %i" % decenas)
print("Unidades: %i" % unidades)

#tema 2 

# Estructuras De Control de Flujo de Datos

#Ejercicio 1

año = 0
lista_1 = []
def string_int(mi_info):
    for i in mi_info:
        lista_1.append(int(i))

pedir_fecha = input("Ingrese fecha en formato (ddmmaaaa): ")
string_int(pedir_fecha)

a = lista_1[7]
b = lista_1[6]
c = lista_1[5]
d = lista_1[4]

if año % 4 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0:
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")

#Ejercicio 2

lista_2 = []

def string_int(mi_info):
    for i in mi_info:
        lista_2.append(int(i))

pedir_num = input("Ingrese un numero entero de 5 digitos: ")
string_int(pedir_num)

a = lista_2[0]
b = lista_2[1]
c = lista_2[2]
d = lista_2[3]
e = lista_2[4]

if a == e:
    if b == d:
        print("EL numero ingresado es capicùa")
    else:
        print("EL numero ingresado no es capicùa")
else:
    print("EL numero ingresado no es capicùa")
    

#Ejercicio 3

h = int(input("Ingrese la cantidad de horas: "))
m = int(input("Ingrese la cantidad de minutos: "))

h_a_s = h * (3600)
m_a_s = m * (60)
total = h_a_s + m_a_s

print("El total de segundos es: ", total)

#Ejercicio 4

s = int(input("Ingrese la cantidad de segundos: "))

if s > 0 :
    m = s / 60
    h = s / 3600
    dias = s / 86400

    print("\n La cantidad de minutos es: ", m)
    print("\n La cantidad de horas es: ", h)
    print("\n La cantidad de dias es: ", dias)
else:
    print("Ingrese una cantidad de segundos validos")

#Ejercicio 5

A = int(input("Ingrese el primer numero entero positivo: "))

if A > 0 :
    B = int(input("Ingrese el el segundor numero entero positivo: "))
    if B > 0 :
        C = int(input("Ingrese el Tercer numero entero positivo: "))
        if C > 0:
            if A > B and A > C:
                print("\n El numero mayor es: ", A)
                if B > C:
                    print("\n El segundo mayor es: ", B)
                else:
                    print("\n El segundo mayor es: ", C)
            elif B > A and B > C:
                print("\n EL numero mayor es: ", B)
                if A > C:
                    print("\n El segundo mayor es: ", A)
                else:
                    print("\n El segundo mayor es: ", C)
            elif C > A and C > B:   
                print("\n EL numero mayor es: ", C)
                if A > B:
                    print("\n El segundo mayor es: ", A)
                else:
                    print("\n El segundo mayor es: ", B)
            else:
                print("No se ha podido deteerminar el mayor de los 3 numeros")                
        else:
            print("Por favor ingrese un numero entero positivo")  
    else:
        print("Por favor ingrese un numero entero positivo")          
else:
    print("Por favor ingrese un numero entero positivo") 

#Ejercicio 6

H_e = int(input("Ingrese de hora en formato de 12 en la que se estaciono: "))
if H_e >= 0 and H_e <= 12:   
    M_e = int(input("Ingrese el o los minutos en la que se estaciono: "))   
    if M_e >= 0 and M_e < 60: 
        AM_PM_e  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
        if AM_PM_e == "A" or AM_PM_e == "P" :
            H_s = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
            if H_s >= 0 and H_s <= 12:
                M_s= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                if M_s >= 0 and M_s < 60:
                    AM_PM_s = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                    if AM_PM_s == "A" or AM_PM_s == "P" :
                        if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "A" and AM_PM_s == "P" or AM_PM_e == "P" and AM_PM_s == "P":
                            if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "P" and AM_PM_s == "P":
                                resta_H = H_e - H_s
                                Total_H = resta_H * 4
                                resta_M = M_e - M_s
                                Total_M = resta_M/30
                                Total_M_2 = 0
                                if Total_M < 0 :
                                    Total_M_2 = 2.50
                                    Total_T = Total_H + Total_M_2
                                    print("El Valor a pagar es: Bs", Total_T)
                            elif AM_PM_e == "A" and AM_PM_s == "P":
                                H_s+=12
                                resta_H = H_e - H_s
                                Total_H = resta_H * 4
                                resta_M = M_e - M_s
                                Total_M = resta_M/30
                                Total_M_2 = 0
                                if Total_M < 0 :
                                    Total_M_2 = 2.50
                                    Total_T = Total_H + Total_M_2
                                    print("El Valor a pagar es: Bs", Total_T)
                        else:
                            print("Los datos de entrada y salida no coinciden")
                    else:
                        print("Ingrese una Letra Valida")
                else:
                    print("Ingrese unos minutos de salida valido")        
            else:
                print("Ingrese una hora de salida valida")
        else:
            print("Ingrese una letra valida")    
    else:
        print("Ingrese una cantidad de minutos valido")   
else:
    print("Ingrese una hora de entrada valida")

#Ejercicio 7

L = float(input("Ingrese su peso en Libras: "))
C = int(input("Ingrese su Altura en Centimetros: "))

P = L*0.453592
A = C /100

promedio = P/(A * A)

print("Su peso en Kg es: ", P)
print("Su altura en Metros es: ", A)
print("Su promedio es: ", promedio)

if promedio < 16 :
    print("Su categoria es Criterio de ingreso.")
elif promedio >= 16 and promedio <= 16.9:
    print("Su categoria es infra peso.")
elif promedio >= 17 and promedio <= 18.4:
    print("Su categoria es bajo peso.")
elif promedio >= 18.5 and promedio <= 24.9:
    print("Su categoria es peso normal.")
elif promedio >= 25 and promedio <= 29.9:
    print("Su categoria es sobrepeso.")
elif promedio >= 30 and promedio <= 34.9:
    print("Su categoria es obesidad pre-mórbida.")
elif promedio >= 40 and promedio <= 45:
    print("Su categoria es obesidad mórbida.")
elif promedio > 45 :
    print("Su categoria es obesidad híper-mórbida.")


#Ejercicio 8

d = int(input("Ingrese un dia correspondiente al 2014: "))
if d > 0 and d < 31:
    m = int(input("Ingrese un numero de mes correspondiente al 2014: "))
    if m > 0 and m <=12 :
        diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        i = 0
        acumulador = 0
        while i <= m - 1:
            acumulador = acumulador + diasMes[i]
            i = i + 1
        total = acumulador + d
        print("\n EL total de dias que han transcurrido desde el 1 de enero del 20154 hasta la fecha que solicito es: ", total)

#Ejercicio 9

m = int(input("Ingrese un numero entre el 1 y el 12: "))
if m > 0 and m <= 12 :
    if m == 1 :
        print("Enero")
    elif m ==2 :
        print("Febrero")
    elif m ==3 :
        print("Marzo")
    elif m ==4 :
        print("Abril")
    elif m ==5 :
        print("Mayo")
    elif m ==6 :
        print("Junio")
    elif m ==7 :
        print("Julio")
    elif m ==8 :
        print("Agosto")
    elif m ==9 :
        print("Septiembre")
    elif m ==10 :
        print("Octubre")
    elif m ==11:
        print("Noviembre")
    elif m ==12 :
        print("Diciembre")       
else:
    print("Ingrese un numero valido")

#Ejercicio 10 

c = float(input("Ingrese la cantidad a pagar en el almacen: "))

if c > 1000:
    total = c * 0.80
    print("SU total a pagar aplicando el descuento de la tienda es de: Bs", total)
else:
    print("Su total a pagar es de: Bs", c)

# TEMA 3

#Estructuras Iterativas

#Ejercicio 1

import math
n = int(input("ingrese un numero entero: "))
if n > 0:
    digitos = int(math.log10(n))+1
    print(digitos)
elif n == 0:
    digitos = 1
    print(digitos)
elif n < 0:
    print("Ingrese un numero valido")

#Ejercicio 2

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

def capicua(numero):
    return numero == invertir_numero(numero)

numeros = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for numero in numeros:
    es_capicua = capicua(numero)
    print(f"El número {numero} es capicúa? {es_capicua}")

#Ejercicio 3

def es_primo(num):
    contador = 0

    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
    
    if contador == 2:
        print("Es un numero primo")
        return True
    else:
        print("No es un numero primo")
        return False
n = int(input("Ingrese un numero primo positico: "))
if n > 0:
    print(es_primo(n))  

#Ejercicio 4:

n = int(input("Ingrese un numero entero: "))
if n >= 0 :
    x = 1
    f = 1
    while x <= n:
        f = f *x 
        x += 1
    print("El factorial de ",n," es: ",f)
else:
    print("No se pudo calcular el factorial")

#Ejercicio 5:

def validar(valor):
    	return False

valido = 0
while not valido:
    password = input("Introduzca una contraseña con al menos 10 digitos: ")
    valido = len(password) >= 10
print("\n has ingresado la contraseña correcta")