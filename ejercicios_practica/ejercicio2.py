# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt
import matplotlib.axes



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

response = requests.get(url)
todos = response.json()
print("Imprimir los datos de la nube")
print(json.dumps(todos, indent=4))


completed_by_user = {}
for todo in todos:
    if todo["completed"]:
        if todo["userId"] in completed_by_user:
            completed_by_user[todo["userId"]] += 1
        else:
            completed_by_user[todo["userId"]] = 1

# Crear el gráfico de barras
plt.bar(completed_by_user.keys(), completed_by_user.values())
plt.xlabel("User ID")
plt.ylabel("Libro leído")
plt.title("Libros leídos por UserID")
plt.show()

# x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# y = list(map( +=1 if data["completed"] == True and data["userId"] == x else 0 for x in x))








    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
'''
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x, y)
plt.show()
'''
print("terminamos")