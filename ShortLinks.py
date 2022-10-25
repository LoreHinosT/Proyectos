#EL CODIGO QUE FUNCIONA NUNCA SE BORRA, SE COMENTA
# #Mostrar un proyecto en un archivo .py
##No se dividen en celdas, no podemos segmentar el programa
#Podemos "segmentar" con comentarios
#############################################
#Las funciones cuando las llamamos debemos imprimirlas
#def func():
  #return 1
#print(func())
############################################
#Siempre la importancion de modulos y paquetes va al comienzo, en orden alfabetico y por renglon
#import sys,time MAL

#Import sys
#import time BIEN
############################################
#Guardar y correr
#Podemos importar la libreria desde el cmd o desde la terminal del programa
############################################
#ORDEN
 #4 Importancion de modulos y paquetes
 #3 La definicion de variables
 #2 La definicion de las funciones
 #1 La definicion de las clases
#############################################
#DESCARGA DE LIBRERIAS  DESDE LA TERMINAL
  #pip install pyshorteners
  #pip install pyperclip
#############################################
import pyshorteners
from tkinter import *  #TKINTER PARA INTERFAZ GRAFICA
from tkinter import ttk
import webbrowser
import pyperclip

ventana=Tk() #esqueleto de nuestra interfaz grafica
ventana.minsize(400,310)
ventana.title("Acortador de enlaces") #TITULO DE VENTANA
ventana.resizable(0,0) #La ventana se queda fija 

short=pyshorteners.Shortener() #Accedemos a los metodos y atributos

def acortamiento(): #Acorta el enlace y luego nos genera dos botones uno de abrir y uno de copiar
    acortado=short.tinyurl.short(acortar_entry.get())
    resultado_etiqueta=Label(ventana,text=acortado)
    resultado_etiqueta.grid(row=8,column=0)
    ##TODo LO QUE SE VA A VER
    resultado_etiqueta.config(  
        fg="black",
        bg="#16a596",
        font=("Arial",20),
        padx=210,
        pady=20
    )
    boton=Button(ventana,text="Abrir enlace",command=abrir_enlace) #command llama a la funcion abrir_enlace
    boton.grid(row=9,column=0)

    boton=Button(ventana,text="Copiar enlace",command=copiar_enlace)
    boton.grid(row=10,column=0)

def abrir_enlace():
    webbrowser.open(short.tinyurl.short(acortar_entry.get())) #ABRE LA URL

def copiar_enlace():
    pyperclip.copy(short.tinyurl.short(acortar_entry.get())) #SE GENERA LA COPIA


etiqueta_home=Label(ventana, text="¡Acortador de enlaces!")
etiqueta_home.config(
    fg="white",
    bg="#8000ff",
    font=("Candara",30),
    padx=210,
    pady=0
)
etiqueta_home.grid(row=0,column=0)

acortar_etiqueta=Label(ventana,text="Ingresar enlace:",bg="#16a596")
acortar_entry=Entry(ventana) #Genera un cuadradito para escribir
acortar_etiqueta.grid(row=1,column=0,padx=5,pady=5)
acortar_entry.grid(row=2,column=0,padx=5,pady=5)

boton=Button(ventana,text="¡Acortar!",command=acortamiento)
boton.grid(row=5,column=0)

ventana.configure(bg="#16a596")

#El archivo .py es el software y el .exe es el ejecutable son dos cosas completamente distintas
#y para pasar de .py a .exe necesito otras librerias(las librerias depende del SO) 

ventana.mainloop()