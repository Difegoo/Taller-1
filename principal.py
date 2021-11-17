from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import numpy as np
from werkzeug.utils import redirect

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "basedatos"
)
myCursor = mydb.cursor() #Se almacena en mycursor

app = Flask(__name__)

@app.route("/") #decorador
def inicio():
    #return "<p>Hello, World!</p>"
    #return render_template("formularios.html")

    #nombre = "juan"
    #edad = "22"
    #genero = "masculino"
    #telefono = "7777777" 
    #query = f"INSERT INTO users (nombre, edad, genero, telefono) VALUES('{nombre}',{edad},'{genero}','{telefono}')"
    #myCursor.execute(query)
    #mydb.commit()#Confirma los cambios
    #return "<p>Hello, World!</p>"
    return render_template('registroweb.html')

@app.route("/indato", methods=["POST", "GET"]) #decorador
def indato():

    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        genero = request.form['genero']
        telefono = request.form['telefono']
        query = f"INSERT INTO users (nombre, edad, genero, telefono) VALUES('{nombre}',{edad},'{genero}','{telefono}')"
        myCursor.execute(query)
        mydb.commit()#Confirma los cambios
        #return "EL USUARIO HA SIDO REGISTRADO CORRECTAMENTE"
        return redirect(url_for('inicio'))

    else: 
        return "bad request"


@app.route("/ruta1") #decorador
def leerdato():
    query = "SELECT * FROM users"
    myCursor.execute(query) #Ejecutamos el query
    result = myCursor.fetchall() #Devuelve un arreglo de tuplas (Cada fila de la base de datos)
    #print(result[0][1]) #imprime la posicion 0 de la base de datos y la posicion 1 del vector

    #mat= np.array(result) #Captura las matrices de datos de la base
    #newArray = np.delete(mat, (1,3), axis=1) # "mat" borra la columna 1y3, axis=1 elimina columnas; si es 0= elimina filas
    #print(newArray)
    #return "lectura"

    return render_template("formularios.html", people = result)

@app.route("/ruta2") #decorador
def leerdato2():
    query = "SELECT * FROM users"
    myCursor.execute(query) #Ejecutamos el query
    result = myCursor.fetchall() #Devuelve un arreglo de tuplas (Cada fila de la base de datos)
    return render_template("formularios2.html", people = result)

@app.route("/ruta3") #decorador
def leerdato3():
    query = "SELECT * FROM users"
    myCursor.execute(query) #Ejecutamos el query
    result = myCursor.fetchall() #Devuelve un arreglo de tuplas (Cada fila de la base de datos)
    
    mat= np.array(result) #Captura las matrices de datos de la base
    #newArray = np.delete(mat, (1,3), axis=1) # "mat" borra la columna 1y3, axis=1 elimina columnas; si es 0= elimina filas
    print(mat)
    return "¡Se imprimio por consola TODA la informacion de los usuarios!"


@app.route("/ruta4") #decorador
def leerdato4():
    query = "SELECT * FROM users"
    myCursor.execute(query) #Ejecutamos el query
    result = myCursor.fetchall() #Devuelve un arreglo de tuplas (Cada fila de la base de datos)
    
    mat= np.array(result) #Captura las matrices de datos de la base
    newArray = np.delete(mat, (1,2), axis=1) # "mat" borra la columna 1y2, axis=1 elimina columnas; si es 0= elimina filas
    print(newArray)
    return "¡Se imprimio por consola el NOMBRE y TELEFONO de los usuarios!"
    
if __name__ == "__main__":
    app.run()