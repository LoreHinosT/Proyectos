#Importacion
#Definicion de variables 
#Definicion de funciones #de clases
#La llamada de funciones y la instanciacion de las clases

#################LIBRERIAS##############
#pyshorteners para crear un objeto que vamos a ir acortando
#pyperclip generamos una copia del enlace cortado para generar un boton
#tkinter modulo de interfaces graficas

import pyshorteners
from tkinter import * #se importa todo
from tkinter import ttk  #si o si hay que importar el modulo ttk
import webbrowser #porque vamos a recibir una url
import pyperclip 
#########################################
#########################################

#Vamos a crear el esqueleto
ventana=Tk()
ventana.minsize(400,310)
ventana.title("Acortador de enlaces") #titulo de la ventana
ventana.resizable(0,0)#false y false, no se agrande ni se achica, queda fija 

short=pyshorteners.Shortener() #short es de la clase Shorteners de la biblioteca pyshorteners

def acortamiento():
    acortado=short.tinyurl.short(acortar_entry.get()) #acorta una URL utilizando el servicio TinyURL y asigna el resultado a la variable acortado
    #tinyurl es el atributo y short es el metodo
    resultado_etiqueta=Label(ventana,text=acortado) #label es una clase de tkinter 
    resultado_etiqueta.grid(row=8,column=0) #grid posiciones en la ventana, grid es un metodo de mi clase
    resultado_etiqueta.config(
        fg="black",#color del texto
        bg="#16a596", #color de fondo
        font=("Arial",20), #fuente y tamaño
        padx=210, #tamaño de borde entre la letra ey el rectangulo
        pady=20
        ) 
    boton=Button(ventana,text="Abrir enlace",command=abrir_enlace)#command tiene que llamar a esa funcion
    boton.grid(row=9,column=0)

    boton=Button(ventana,text="Copiar enlace", command=copiar_enlace)#command tiene que llamar a esa funcion
    boton.grid(row=10,column=0)

def abrir_enlace():
    webbrowser.open(short.tinyurl.short(acortar_entry.get()))

def copiar_enlace():
    pyperclip.copy(short.tinyurl.short(acortar_entry.get())) #generamos una copia del enlace cortado

etiqueta_home = Label(ventana,text="Acortador de enlace") #titulo de la ventana adentro
etiqueta_home.config(
    fg="white",
    bg="#8000ff",
    font=("Arial", 20), #fuentes de google docs
    padx=210,
    pady=20
)
etiqueta_home.grid(row=0,column=0)
acortar_etiqueta=Label(ventana,text="Ingresar enlace", bg="#16a596") #son los parametros de config pero los voy a colocar aca
acortar_entry=Entry(ventana) #la clase entry genera el rectangulo para ingresar texto
acortar_etiqueta.grid(row=1,column=0,padx=5,pady=5)
acortar_entry.grid(row=2,column=0,padx=5,pady=5)

boton=Button(ventana,text="¡Acortar!",command=acortamiento)
boton.grid(row=5, column=0)

ventana.configure(bg="#16a596")


ventana.mainloop()#fin de la interfaz grafica