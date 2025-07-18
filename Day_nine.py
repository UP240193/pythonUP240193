# Ejercicios: Nivel 1
# Obtener la edad del usuario
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Ya tienes edad suficiente para aprender a conducir.")
else:
    print(f"Necesitas esperar {18 - edad} años más para aprender a conducir.")

# Comparar mi edad y tu edad
mi_edad = 25
tu_edad = int(input("Ingresa tu edad: "))
diferencia = abs(mi_edad - tu_edad)
if tu_edad > mi_edad:
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif tu_edad < mi_edad:
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")

# Obtener dos números y compararlos
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

# Ejercicios: Nivel 2
# Asignar calificación según el puntaje
puntaje = int(input("Ingresa el puntaje del estudiante: "))
if 80 <= puntaje <= 100:
    print("A")
elif 70 <= puntaje <= 89:
    print("B")
elif 60 <= puntaje <= 69:
    print("C")
elif 50 <= puntaje <= 59:
    print("D")
elif 0 <= puntaje <= 49:
    print("F")
else:
    print("Puntaje inválido")

# Verificar la estación
mes = input("Ingresa el mes: ").capitalize()
if mes in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación es Otoño.")
elif mes in ["Diciembre", "Enero", "Febrero"]:
    print("La estación es Invierno.")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print("La estación es Primavera.")
elif mes in ["Junio", "Julio", "Agosto"]:
    print("La estación es Verano.")
else:
    print("Mes inválido")

# Lista de frutas
frutas = ['plátano', 'naranja', 'mango', 'limón']
nueva_fruta = input("Ingresa una fruta: ").lower()
if nueva_fruta in frutas:
    print("Esa fruta ya existe en la lista")
else:
    frutas.append(nueva_fruta)
    print("Lista modificada de frutas:", frutas)

# Ejercicios: Nivel 3
persona = {
    'primer_nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Space street',
        'código_postal': '02210'
    }
}
# Verificar si tiene la clave habilidades y mostrar la habilidad del medio
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    medio = habilidades[len(habilidades)//2]
    print('Habilidad del medio:', medio)
    # Verificar si tiene Python
    print('¿Tiene Python?', 'Python' in habilidades)
    # Verificar tipo de desarrollador
    if habilidades == ['JavaScript', 'React']:
        print('Es desarrollador front end')
    elif all(x in habilidades for x in ['Node', 'Python', 'MongoDB']):
        print('Es desarrollador backend')
    elif all(x in habilidades for x in ['React', 'Node', 'MongoDB']):
        print('Es desarrollador fullstack')
    else:
        print('Título desconocido')
# Verificar si está casado y vive en Finlandia
if persona.get('casado') and persona.get('país') == 'Finlandia':
    print(f"{persona['primer_nombre']} {persona['apellido']} vive en Finlandia. Está casado.")