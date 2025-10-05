"""
    Escribe un programa en Python que permita al 
    usuario ingresar notas (números decimales) indefinidamente. 
    El programa debe calcular y mostrar el promedio, 
    la nota mínima y la nota máxima de las notas ingresadas. 
    Asegúrate de manejar correctamente casos donde el usuario ingrese valores inválidos.
"""
def promedio(list):
    suma_cal = 0.0
    promedio = 0.0
    for i in list:
        suma_cal+=i
    promedio = suma_cal / len(list)    
    return print("El promedio de las notas es:" , promedio)

def nota_minima(list):
    nota_minima = list[0] # Suponemos el primer elemento de la lista como la nota mínima
    for nota in list:
        if nota < nota_minima:
            nota_minima = nota
    return print("La nota mínima es:", nota_minima)
def nota_maxima(list):
    nota_maxima = list[0] # Suponemos el primer elemento de la lista como la nota máxima
    for nota in list:
        if nota > nota_maxima:
            nota_maxima = nota
    return print("La nota máxima es:", nota_maxima)

def pedir_notas():
    global list
    list = []
    while True:
        contador = 0
        respuesta = input("Ingresa tu nota: [Escribe <Fin> para finalizar el programa] ")
        if respuesta == "Fin":
            break
        list.append(float(respuesta))
        contador+=1
    return list

def pedir_opcion(list):
    print("""
Si quieres realizar algún cálculo estadístico con las notas que ingresaste, elige la opción correspondiente:
1 - Carcular promedio
2 - Calcular la nota máxima
3 - Calcular la nota mínima
4 - Salir del porgrama
""")
    opcion = input("Escribe un número, por favor: ")
    if opcion == "1":
        promedio(list)
    elif opcion == "2":
        nota_maxima(list)
    elif opcion == "3":
        nota_minima(list)
    elif opcion == "4":
        return False
    else: 
        print("La opción elegida no es válida.")
        pedir_opcion()
    return True

# Función principal
def main():
    print("""----------------------------------------
| Calculadora de Estadísticas de Notas | 
----------------------------------------""")
    pedir_notas()
    while pedir_opcion(list):
        pedir_opcion(list)

# APP
main()