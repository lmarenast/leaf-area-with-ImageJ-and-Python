#Librerías necesarias
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import numpy as np
import cv2
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

def area_foliar():
    

    #Abrimos imagen y cambiamos su espacio de color a HSV para una mejor detección
    Tk().withdraw() 
    img_src = askopenfilename()
    img = cv2.imread(img_src)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    #Definimos el umbral para el color verde en el espacio HSV
    umbral_bajo = (30,100,0)
    umbral_alto = (55,255,255)

    #Hacemos la máscara y filtramos la imagen original


    mask = cv2.inRange(img_hsv,umbral_bajo,umbral_alto)
    res = cv2.bitwise_and(img,img,mask=mask)

    plt.xticks([])
    plt.yticks([])
    plt.imshow(mask,cmap='gray')
    

    ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    plt.imshow(thresh, cmap='gray')
    area_px = cv2.countNonZero(thresh)

    #Se necesitará el dato de ImageJ sobre la escala de pixeles, es decir, cuantos pixeles es un cm en cada imagen.
    set_scale_imageJ = float(input('Ingrese la escala arrojada por ImageJ:' ))
    set_scale_imageJ = int(np.floor(set_scale_imageJ))
    area_cm = area_px/(set_scale_imageJ**2)
    area_cm = round(area_cm,2)

    return  print( f"El área en centímetros es: {area_cm} cm2"), plt.show()

area_foliar()
