import random, csv, math

opi=0
asig=0

#multiplacr todo despues raiz de 10
#**0.5 <--- raiz cuadrada creo
#math.sqrt(total numeroes, n) creo


trabajadores=[
    {'nombre':'Juan Perez','sueldo':[]},
    {'nombre':'Maria Garcia','sueldo':[]},
    {'nombre':'Carlos Lopez','sueldo':[]},
    {'nombre':'Ana Martinez','sueldo':[]},
    {'nombre':'Pedro Rodriguez','sueldo':[]},
    {'nombre':'Laura Hernandez','sueldo':[]},
    {'nombre':'Miguel Sanchez','sueldo':[]},
    {'nombre':'Isabel Gomez','sueldo':[]},
    {'nombre':'Francisco Diaz','sueldo':[]},
    {'nombre':'Elena Fernandez','sueldo':[]}
]

trabajadores_menor=[]
trabajadores_intermedio=[]
trabajadores_mayor=[]

sueldo_total=[]
sueldo_menor=[]
sueldo_intermedio=[]
sueldo_mayor=[]

def reporte():
    with open('reporte.csv','w',newline='') as reporte_csv:
        reporte_write=csv.writer(reporte_csv)
        primera_row=['Nombre empleado\t','Sueldo Base\t','Descuento Salud\t','Descuento AFP\t','Sueldo Liquido\t']
        reporte_write.writerow(primera_row)
        for i in range(0,len(trabajadores)):
            row=[f'{trabajadores[i]['nombre']}\t',f'{sueldo_total[i]}\t',f'{round(sueldo_total[i]*0.07)}\t',f'{round(sueldo_total[i]*0.12)}\t',f'{round(sueldo_total[i]-(sueldo_total[i]*0.07)-(sueldo_total[i]*0.12))}\t']
            reporte_write.writerow(row)
    return "El reporte se a generado."

def asignar_sueldos():
    for i in range(0,len(trabajadores)):
        sueldo_total.append(random.randint(300000,2500000))
        trabajadores[i]['sueldo'].append(sueldo_total[i])
        if sueldo_total[i]<800000:
            trabajadores_menor.append(trabajadores[i]['nombre'])
            sueldo_menor.append(sueldo_total[i])
        elif sueldo_total[i]>=800000 and sueldo_total[i]<=2000000:
            trabajadores_intermedio.append(trabajadores[i]['nombre'])
            sueldo_intermedio.append(sueldo_total[i])
        elif sueldo_total[i]>2000000:
            trabajadores_mayor.append(trabajadores[i]['nombre'])
            sueldo_mayor.append(sueldo_total[i])
    return "Los sueldos se han asignado."

def clas_sueldos():
    
    print("Sueldos menores a $800.000 TOTAL: ", len(sueldo_menor))
    print("")
    print("Nombre empleado\tSueldo")
    for i in range(0,len(trabajadores_menor)):
        print(f"{trabajadores_menor[i]}\t${sueldo_menor[i]}")
    print("")
    
    
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ", len(sueldo_intermedio))
    print("")
    print("Nombre empleado\tSueldo")
    for i in range(0,len(trabajadores_intermedio)):
        print(f"{trabajadores_intermedio[i]}\t${sueldo_intermedio[i]}")
    print("")
    
    
    print("Sueldos mayores a $2.000.000 TOTAL: ", len(sueldo_mayor))
    print("")
    print("Nombre empleado\tSueldo")
    for i in range(0,len(trabajadores_mayor)):
        print(f"{trabajadores_mayor[i]}\t${sueldo_mayor[i]}")
    print("")
    
    
    return f"TOTAL SUELDOS: ${sum(sueldo_total)}"

def estadisticas():
    print(f"El sueldo mas bajo es: ${min(sueldo_total)}")
    print(f"El sueldo mas alto es: ${max(sueldo_total)}")
    print(f"El promedio entre los sueldos es: ${round(sum(sueldo_total)/len(sueldo_total))}")
    mult=1
    
    for i in range(0,len(sueldo_total)):
        mult*=sueldo_total[i]
    
    return f"La media grafica de los sueldos es de: ${round(mult**(1/10))}"

while True:
    print("*****MENU*****")
    print("1. Asignar sueldos aleatorios.")
    print("2. Clasificar sueldos.")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos.")
    print("5. Salir del programa.")
    print("**************")
    while True:
        try:
            opi=int(input(">"))
        except ValueError:
            print("Solamente ocupe numeros enteros.")
        else:
            if opi>5 or opi<1:
                print("Solamente ocupe numeros entre 1-5.")
            else:
                break
    match opi:
        case 1:
            if asig==0:
                print(asignar_sueldos())
                asig=1
            else:
                print("Los sueldos ya fueron asignados.")
        case 2:
            if asig==0:
                print("Asigne los sueldos antes de clasificarlos.")
            else:
                print(clas_sueldos())
        case 3:
            if asig==0:
                print("Asigne los sueldos antes de ver sus estadisticas.")
            else:
                print(estadisticas())
        case 4:
            if asig==0:
                print("Asigne los sueldos antes de generar un reporte.")
            else:
                print(reporte())
        case 5:
            print("Finalizando programa...")
            print("Desarrollador Simon Segovia.")
            print("RUT 21.818.090-6")
            break