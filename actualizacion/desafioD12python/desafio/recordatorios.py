recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output
print(recordatorios)

print("para ver la eliminacion del 1-5-21, sacar el #".upper())
# fecha_recordar=str(input("Ingrese fecha para revisar en recordatorio: "))

# for fecha_recordar in recordatorios:
#     if fecha_recordar in recordatorios:
#         print (recordatorios)
#     else:
#         recordatorios.append(input("Ingrese fecha para agregar a recordatorio: "))
    


#insertar dia 2/2/21 6am *empezar el año*
nueva_fecha_recordatorio=['2021-02-02', "06:00", "Empezar el Año"]
recordatorios.append(nueva_fecha_recordatorio)

#modificar fecha de 15 al 16
for fecha in recordatorios:
    if fecha[0] == '2021-07-15': #comprueba
        fecha[0] = '2021-07-16' #asigna


#se elimina el evento indicado
#recordatorios.remove(['2021-05-01', "15:00", "Eliminado el dia del trabajo"])


#insertar dia 24/12/21 22hrs *cena navidad*
nueva_fecha_cena_navidad=['2021-12-24', "22:00", "Cena Navidad"]
recordatorios.append(nueva_fecha_cena_navidad)

#insertar dia 31/12/21 22hrs *cena año nuevo*
nueva_fecha_cena_añonuevo=['2021-12-31', "22:00", "Cena Año Nuevo"]
recordatorios.append(nueva_fecha_cena_añonuevo)

#ordenar la nueva lista
recordatorios.sort()

#imprimir
for evento in recordatorios:
    print(evento)
    
