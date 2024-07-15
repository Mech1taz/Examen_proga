from os import system
system("cls")
import random
import statistics
import csv
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
    f=open("lista_trabajadores.csv","w")
    #no logrado guardar
    return sueldos
def clasificar_sueldo():
    i=0
    total=0
    total_sueldos=0
    print(f"\nSueldos menores a $800.000")
    print("Nombre empleado\tSueldo")
    for i in range(10):
        if sueldos[i]<800000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
            total+=1
            total_sueldos+=sueldos[i]
        else:
            pass
    print(f"\nSueldos entre $800.000 y $2.000.000")
    print("Nombre empleado\tSueldo")
    for i in range(10):
        if sueldos[i]>=800000 and sueldos[i]<=2000000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
            total_sueldos+=sueldos[i]
            pass
        else:
            pass
    print(f"\nSueldos superiores a $2.000.000")
    print("Nombre empleado\tSueldo")
    for i in range(10):
        if sueldos[i]>2000000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
            total_sueldos+=sueldos[i]
            pass
        else:
            pass
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")
def estadistica():
    print("no lista")
def reporte():
    i=0
    print("Nombre Empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Liquido")
    for i in range(10):
        dsalud=sueldos[i]*0.07
        afp=sueldos[i]*0.12
        desc=afp+dsalud
        liquido=(sueldos[i]-desc)
        print(f"{trabajadores[i]}\t\t${sueldos[i]}\t\t${dsalud}\t\t${afp}\t${liquido}")
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
            estadistica()
        case "4":
            reporte()
        case "5":
            salir()
            break
        