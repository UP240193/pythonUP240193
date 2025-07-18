# Ejercicios: Nivel 1
# Declarar una función que suma dos números
def sumar_dos_numeros(a, b):
    return a + b

# Área de un círculo
def area_circulo(radio):
    import math
    return math.pi * radio * radio

# Sumar todos los números (argumentos arbitrarios)
def sumar_todos(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números."

# Convertir °C a °F
def convertir_celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

# Verificar estación
def verificar_estacion(mes):
    mes = mes.capitalize()
    if mes in ["Septiembre", "Octubre", "Noviembre"]:
        return "Otoño"
    elif mes in ["Diciembre", "Enero", "Febrero"]:
        return "Invierno"
    elif mes in ["Marzo", "Abril", "Mayo"]:
        return "Primavera"
    elif mes in ["Junio", "Julio", "Agosto"]:
        return "Verano"
    else:
        return "Mes inválido"

# Calcular pendiente de una ecuación lineal
def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Resolver ecuación cuadrática
def resolver_ecuacion_cuadratica(a, b, c):
    import math
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2

# Imprimir elementos de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

# Invertir una lista usando bucle
def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

# Capitalizar elementos de una lista
def capitalizar_lista(lista):
    return [str(x).capitalize() for x in lista]

# Agregar elemento a una lista
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

# Eliminar elemento de una lista
def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

# Sumar números en un rango
def suma_de_numeros(n):
    return sum(range(n+1))

# Sumar impares en un rango
def suma_de_impares(n):
    return sum(x for x in range(n+1) if x % 2 != 0)

# Sumar pares en un rango
def suma_de_pares(n):
    return sum(x for x in range(n+1) if x % 2 == 0)

# Ejercicios: Nivel 2
# Contar pares e impares
def pares_e_impares(n):
    pares = sum(1 for x in range(n+1) if x % 2 == 0)
    impares = sum(1 for x in range(n+1) if x % 2 != 0)
    print(f"El número de impares es {impares}.")
    print(f"El número de pares es {pares}.")

# Factorial
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# Verificar si está vacío
def esta_vacio(valor):
    return not bool(valor)

# Funciones estadísticas
def calcular_media(lista):
    return sum(lista) / len(lista)
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2
    else:
        return lista_ordenada[n//2]
def calcular_moda(lista):
    from collections import Counter
    return Counter(lista).most_common(1)[0][0]
def calcular_rango(lista):
    return max(lista) - min(lista)
def calcular_varianza(lista):
    media = calcular_media(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)
def calcular_std(lista):
    import math
    return math.sqrt(calcular_varianza(lista))

# Ejercicios: Nivel 3
# Verificar si es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Verificar si todos los elementos son únicos
def todos_unicos(lista):
    return len(lista) == len(set(lista))

# Verificar si todos los elementos son del mismo tipo
def mismo_tipo(lista):
    return all(type(x) == type(lista[0]) for x in lista)

# Verificar si una variable es válida en Python
def variable_valida(nombre):
    import keyword
    return nombre.isidentifier() and not keyword.iskeyword(nombre)

# Funciones para countries_data.py (requiere archivo de datos)
# def idiomas_mas_hablados(countries_data, top=10):
#     from collections import Counter
#     contador = Counter()
#     for pais in countries_data:
#         contador.update(pais['languages'])
#     return contador.most_common(top)
# def paises_mas_poblados(countries_data, top=10):
#     return sorted(countries_data, key=lambda x: x['population'], reverse=True)[:top]