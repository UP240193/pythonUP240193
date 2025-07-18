# Crea un diccionario vacío llamado perro
dog = {}
# Agrega nombre, color, raza, piernas, edad al diccionario
perro = {}
perro['nombre'] = 'Buddy'
perro['color'] = 'Marrón'
perro['raza'] = 'Labrador'
perro['piernas'] = 4
perro['edad'] = 5
print('Diccionario de perro:', perro)

# Crea un diccionario de estudiante con las claves requeridas
estudiante = {
    'primer_nombre': 'Ana',
    'apellido': 'Lopez',
    'genero': 'Femenino',
    'edad': 21,
    'estado_civil': 'Soltera',
    'habilidades': ['Python', 'Excel'],
    'pais': 'México',
    'ciudad': 'CDMX',
    'direccion': 'Calle Falsa 123'
}
# Imprime el diccionario de estudiante
print('Diccionario de estudiante:', estudiante)

print('Longitud del diccionario de estudiante:', len(estudiante))

# Obtén el valor de habilidades y verifica el tipo de dato
habilidades = estudiante['habilidades']
print('Habilidades:', habilidades)
print('Tipo de habilidades:', type(habilidades))

# Modifica el valor de habilidades agregando una o dos habilidades
estudiante['habilidades'].extend(['SQL', 'PowerPoint'])
print('Habilidades actualizadas:', estudiante['habilidades'])

# Obtén las claves del diccionario como una lista
print('Claves:', list(estudiante.keys()))

# Obtén los valores del diccionario como una lista
print('Valores:', list(estudiante.values()))

# Cambia el diccionario a una lista de tuplas usando el método items()
print('Elementos como tuplas:', list(estudiante.items()))

# Elimina uno de los elementos del diccionario
del estudiante['direccion']
print('Después de eliminar dirección:', estudiante)

# Elimina uno de los diccionarios
del perro