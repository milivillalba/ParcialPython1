#En este Ejercicio tengo que realizar un anàlisis bàsico sobre estas listas de ventas.

#importar pandas
import pandas as pd

import matplotlib.pyplot as plt
#Lista de ventas mensuales

ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

#CREAR UN dataFrame para relizar utilizar la lista en mi analisis
df= pd.DataFrame(ventas_mensuales,columns=['mes', 'total_ventas', 'año'])
#Agrupara los datos por trimestre 

#perdon profe no pude agrupar por trimestre:(
primer_cuatrimestre=[
    {"mes": "Enero", "total_ventas": 15000, "año": 2023},
    {"mes": "Febrero", "total_ventas": 18000, "año": 2023},
    {"mes": "Marzo", "total_ventas": 22000, "año": 2023},
]

segundo_cuatrimestre=[
    {"mes": "Abril", "total_ventas": 19000, "año": 2023},
    {"mes": "Mayo", "total_ventas": 25000, "año": 2023},
    {"mes": "Junio", "total_ventas": 28000, "año": 2023},
]
tercer_cuatrimestre= [
    {"mes": "Julio", "total_ventas": 32000, "año": 2023},
    {"mes": "Agosto", "total_ventas": 30000, "año": 2023},
    {"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
 ]


agrupar_datos = df.groupby('mes').sum()
print(agrupar_datos)
#Filtrar y mostrar solos los meses donde las ventas superen los 2000

ventas_mayor= df[df['total_ventas']>2000]
print(ventas_mayor)

#calcular el promedio de ventas mensuales
print(df['total_ventas'].mean())



#Crear un dataFrame que incluya dos columnas , una para los meses y otra para el total
DataFrame= pd.DataFrame({
    'Meses': ['enero', 'febrero', 'marzo', 'abril','mayo','juni','julio','agosto','septiembre','octubre','nobiembre','diciembre'],
    'Total_ventas': [100000,200000,250000,300000,450000,500000,550000,600000,650000,700000,750000,800000]
})


plt.plot(DataFrame['Meses'], DataFrame['Total_ventas'])
plt.title("Tendecia de ventas a lo largo de los meses")
plt.xlabel("Meses")
plt.ylabel("Total de ventas de cada mes")
plt.show()


