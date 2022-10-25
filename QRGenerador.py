#pip install qrcode
#pip install pillow
import qrcode
import PIL #PARA PROCESO DE IMAGENES
import sys
import time

def generar_codigo():
    print("Bienvenidos,vamos a generar un codigo QR")
    time.sleep(2) #espera dos segundos
    print("En este programa, solicitaremos un enlace y generaremos un codigo qr")
    time.sleep(3)
    codificar=input("Ingrese una palabra o enlace para generar un codigo QR")
    print("Codificando..")
    time.sleep(3)
    img=qrcode.make(codificar)  #se genera la imagen
    f=open("{codificar}_QR.png","wb") #Se ggenera el archivo y la ruta de direccion #IMPORTANTE LA R PARA AGREGAR LINKS
    img.save(f) #Guardamos la imagen en dicho archivo
    print(f"¡Listo! Tenes la imagen creada con el nombre {codificar}_QR.png")
    time.sleep(2)
    preguntar_opcion() #Llamo a la funcion
def preguntar_opcion():
    while True:
        opcion=input("¿Que hacer ahora? Elegir H para hacer otro codigo o S para salir")
        if opcion in "Hh":
            generar_codigo()
            break
        elif opcion in "Ss":
            time.sleep(0.4)
            print("Finalizado.")
            sys.exit()
        else:
            print("No ha elegido una opcion correcta")

generar_codigo()