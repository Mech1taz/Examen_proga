from os import system
system("cls")
import random
import statistics
trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodriguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
def sueldo_aleatorio():
    i=0
    for i in range(10):
        sueldo= random.randint(300000,2500000)
        sueldos.append(sueldo)
    print(sueldos)
    print("Empleado\tSueldo")
    for i in range(10):
        print(f"{trabajadores[i]}\t${sueldos[i]}")
    return sueldos
def clasificar_sueldo():
    i=0
    total=0
    total_sueldos=0
    print("Nombre empleado\tSueldo")
    for i in range(10):
        if sueldos[i]<800000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
            total+=1
            total_sueldos+=sueldos[i]
        else:
            pass
    print(f"\nSueldos menores a $800.000 TOTAL: {total}")
    print(f"TOTAL SUELDOS: ${total_sueldos}")
def limpiar():
    system("cls")
def sueldo():
    pass
def salir():
    print('''
Finalizando programa...
Desarrollado por Matias Astudillo
RUT 21.370.593-8
''')
    import sys
    sys.exit()
#menu
#recordar
### diccionario={"persona":persona,"rut":rut}
### diccionarios.append(diccionario)
#f.open("archivo.csv","w")
#f.write{f"diccionario['persona']}
while True:
    op=input('''
            Ingrese opcion preferida
            1. Asignar sueldos aleatorios
            2. Clasificar sueldos
            3. Ver estadisticas.
            4. Reporte de sueldos
            5. Salir del programa
            ''')
    match op:
        case "1":
            sueldo_aleatorio()
        case "2":
            clasificar_sueldo()
        case "3":
            pass
        case "4":
            pass
        case "5":
            salir()
            break
        