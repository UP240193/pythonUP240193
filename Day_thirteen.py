# Filtrar solo negativos y ceros usando comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numbers if n <= 0]
print(negativos_y_ceros)

# Aplanar lista de listas de listas a una lista de una dimensión
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(lista_aplanada)

# Crear lista de tuplas usando comprensión de listas
lista_tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(lista_tuplas)

# Aplanar lista de países a nueva lista
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output_countries = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(output_countries)

# Cambiar lista a lista de diccionarios
output_dicts = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(output_dicts)

# Cambiar lista de listas a lista de strings concatenados
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output_names = [name[0][0] + ' ' + name[0][1] for name in names]
print(output_names)

# Lambda para pendiente y ordenada al origen de funciones lineales
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
ordenada = lambda x1, y1, m: y1 - m * x1
# Ejemplo de uso:
print('Pendiente:', pendiente(1, 2, 3, 6))
print('Ordenada al origen:', ordenada(1, 2, pendiente(1, 2, 3, 6)))