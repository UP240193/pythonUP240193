import random
import string

# Ejercicios: Nivel 1
# Generar un ID de usuario aleatorio de 6 caracteres
def id_usuario_aleatorio():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Generar IDs de usuario según entrada del usuario
def generar_id_por_usuario():
    num_caracteres = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Número de IDs a generar: "))
    ids = []
    for _ in range(num_ids):
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_caracteres))
        ids.append(id)
    for id in ids:
        print(id)
    return ids

# Generar color RGB aleatorio
def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Ejercicios: Nivel 2
# Generar lista de colores hexadecimales
def lista_colores_hex(n):
    colores = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

# Generar lista de colores RGB
def lista_colores_rgb(n):
    return [generar_color_rgb() for _ in range(n)]

# Generar colores según tipo
def generar_colores(tipo, cantidad):
    if tipo == 'hexa':
        return lista_colores_hex(cantidad)
    elif tipo == 'rgb':
        return lista_colores_rgb(cantidad)
    else:
        return []

# Ejercicios: Nivel 3
# Mezclar una lista
def mezclar_lista(lista):
    copia = lista[:]
    random.shuffle(copia)
    return copia

# Generar lista de siete números aleatorios únicos entre 0 y 9
def siete_numeros_unicos():
    return random.sample(range(10), 7)