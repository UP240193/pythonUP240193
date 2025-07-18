# Ejercicios: Nivel 1
# Iterar de 0 a 10 usando for
for i in range(11):
    print(i)
# Iterar de 0 a 10 usando while
j = 0
while j <= 10:
    print(j)
    j += 1

# Iterar de 10 a 0 usando for
for i in range(10, -1, -1):
    print(i)
# Iterar de 10 a 0 usando while
k = 10
while k >= 0:
    print(k)
    k -= 1

# Triángulo con print()
for i in range(1, 8):
    print('#' * i)

# Cuadrado con bucles anidados
for fila in range(8):
    for columna in range(8):
        print('#', end=' ')
    print()

# Patrón de multiplicación
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# Iterar lista de tecnologías
tecnologias = ['Python', 'Numpy','Pandas','Django', 'Flask']
for tecnologia in tecnologias:
    print(tecnologia)

# Números pares del 0 al 100
for i in range(101):
    if i % 2 == 0:
        print(i)

# Números impares del 0 al 100
for i in range(101):
    if i % 2 != 0:
        print(i)

# Ejercicios: Nivel 2
# Suma de todos los números del 0 al 100
suma_total = 0
for i in range(101):
    suma_total += i
print('La suma de todos los números es', suma_total)

# Suma de pares e impares
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print('La suma de los pares es', suma_pares)
print('La suma de los impares es', suma_impares)

# Ejercicios: Nivel 3
# Extraer países con "land" de countries.py
# from data.countries import countries
# for pais in countries:
#     if 'land' in pais:
#         print(pais)

# Invertir lista de frutas
frutas = ['plátano', 'naranja', 'mango', 'limón']
for i in range(len(frutas)-1, -1, -1):
    print(frutas[i])

# Trabajar con countries_data.py
# from data.countries_data import countries_data
# total_idiomas = set()
# for pais in countries_data:
#     for idioma in pais['languages']:
#         total_idiomas.add(idioma)
# print('Total de idiomas:', len(total_idiomas))
# # Diez idiomas más hablados
# from collections import Counter
# contador_idiomas = Counter()
# for pais in countries_data:
#     contador_idiomas.update(pais['languages'])
# print('Diez idiomas más hablados:', contador_idiomas.most_common(10))
# # Diez países más poblados
# paises_mas_poblados = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
# print('Diez países más poblados:')
# for pais in paises_mas_poblados:
#     print(pais['name'], pais['population'])