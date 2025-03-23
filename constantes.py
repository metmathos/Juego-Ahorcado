import os

'''Constantes de pantalla''' 
TITULO = "Ahorcado"
#Dimensiones de pantalla
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 650

'''Constantes de directorio de imagenes'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

'''Constantes de escena de inicio'''
#Colores de escena de intro
COLOR_FONDO_INTRO =  (63, 219, 214) 
COLOR_ELEMENTO_INTRO = (255, 255, 255)
#Posiciones de widgets de escena de intro
POS_TITULO_Y = 200
POS_BOTON_Y = 350
#Tamaño de widgets de escena de intro
ANCHO_BORDE_RECT = 2
#Tiempos
TIEMPO_ALTERNANCIA_BOTON = 500 #Tiempo en milisegundos
#Constantes de textos de escena de intro
TEXTO_PRINCIPAL = "JUEGO DEL AHORCADO"
TEXTO_SECUNDARIO_1 = "CLIQUEAR ACA PARA SEGUIR AL JUEGO"
TAMAÑO_FUENTE_TITULO = 70
TAMAÑO_FUENTE_BOTON = 35

'''Constantes de escena principal'''
#Colores de escena principal
COLOR_FONDO_PRINCIPAL = (240, 184, 56)
COLOR_PRINCIPAL= (81, 73, 55)
COLOR_FUENTE_ERRONEAS = (238, 42, 7)
#Puntos de referencia de estructura de horca
COMIENZO_BASE_HORCA = (50, 450)
FINAL_BASE_HORCA = (400, 450)
DIMENSIONES_RECTANGULO_HORCA = (100, 352, 100, 100)
COMIENZO_LINEA1_HORCA = (150, 150)
FINAL_LINEA1_HORCA = (150,352)
COMIENZO_LINEA2_HORCA = (150, 150)
FINAL_LINEA2_HORCA = (320, 150)
COMIENZO_LINEA3_HORCA = (320, 150)
FINAL_LINEA3_HORCA = (320, 180)
#Ancho de linea de dibujos en escena principal
ANCHO_LINEA_PR = 5
#Etapas de dibujo de Ahorcado
CENTRO_ETAPA_0 = (320, 205)     #Constante #1 de formacion de cabeza
RADIO_ETAPA_0 = 25              #Constante #2 de formacion de cabeza
COMIENZO_ETAPA_1 = (320, 230)   #Constante #1 de formacion de cuello
FINAL_ETAPA_1 = (320, 245)      #Constante #2 de formacion de cuello
COMIENZO_ETAPA_2 = (320, 245)   #Constante #1 de formacion de cuerpo y formacion de brazos
FINAL_ETAPA_2 = (320, 290)      #Constante #2 de formacion de cuerpo
FINAL_ETAPA_3 = (290, 275)      #Constante #1 de formacion de brazo izquierdo
FINAL_ETAPA_4 = (350, 275)      #Constante #2 de formacion de brazo derecho
FINAL_ETAPA_5 = (290, 320)      #Constante #1 de formacion de pie izquierdo
FINAL_ETAPA_6 = (350, 320)      #Constante #2 de formacion de pie derecho
#Tamaños de fuentes de escena principal
TAMAÑO_FUENTE_ADIVINADAS = 45
TAMAÑO_FUENTE_ERRONEAS = 35
TAMAÑO_FUENTE_INTENTOS = 60
#Cantidad de elementos para horca y ahorcado
CANTIDAD_SEGMENTOS_HORCA = 5
CANTIDAD_ETAPAS_COLGADO = 7

'''Constantes escena victoria'''
#Colores de escena de victoria
COLOR_GANAR = (25, 242, 245)
COLOR_TEXTO_GANAR = (0, 0 ,0)
#Constantes de texto de victoria
TAMAÑO_TEXTO_GANAR = 120
TEXTO_GANAR = "GANASTE!"
#Etapas extras de dibujo de ahorcado
FINAL_ETAPA_3_GANAR = (290, 220)    #Brazo izquierdo levantado
FINAL_ETAPA_4_GANAR = (350, 220)    #Brazo derecho levantado
#Etapas de dibujo de ahorcado en centro de pantalla
SEG_CENTRO_ETAPA_0 = (500, 265)     #Constante #1 de formacion de cabeza
SEG_RADIO_ETAPA_0 = 25              #Constante #2 de formacion de cabeza
SEG_COMIENZO_ETAPA_1 = (500, 290)   #Constante #1 de formacion de cuello
SEG_FINAL_ETAPA_1 = (500, 305)      #Constante #2 de formacion de cuello
SEG_COMIENZO_ETAPA_2 = (500, 305)   #Constante #1 de formacion de cuerpo y formacion de brazos
SEG_FINAL_ETAPA_2 = (500, 350)      #Constante #2 de formacion de cuerpo
SEG_FINAL_ETAPA_3 = (470, 280)      #Constante #1 de formacion de brazo izquierdo
SEG_FINAL_ETAPA_4 = (530, 280)      #Constante #2 de formacion de brazo derecho
SEG_FINAL_ETAPA_5 = (470, 380)      #Constante #1 de formacion de pie izquierdo
SEG_FINAL_ETAPA_6 = (530, 380)      #Constante #2 de formacion de pie derecho

'''Constantes escena derrota'''
#Colores de escena de derrota
COLOR_PERDER = (255, 0, 0)
COLOR_TEXTO_PERDER = (0, 0 ,0)
#Constantes de texto de derrota
TAMAÑO_TEXTO_PERDER = 120
TEXTO_PERDER = "PERDISTE"

'''Constantes funcion opciones de final de juego'''
#Dimensiones de botones
DIMENSIONES_BOTON_VOLVER_EMPEZAR = (100, 250, 250, 200)
DIMENSIONES_BOTON_SALIR = (600, 250, 250, 200)
#Colores
COLOR_OPCIONES = (0, 0, 0)
#Constantes de texto
TITULO_PRINCIPAL_OPCIONES = "Que deseas hacer?"
OPCION_VOLVER_EMPEZAR = "VOLVER A JUGAR"
OPCION_SALIR = "SALIR"
TAMAÑO_TITULO_OPCIONES = 70
TAMANO_TEXTO_OPCIONES = 30
POS_TIT_OPC_Y = 100
POS_OP_OPC_Y = 340
POS_X_BOTON_VOLVER_MITAD = 225
POS_X_BOTON_SALIR_MITAD = 725

'''Base de datos para las palabras a adivinarse'''
LISTA_PALABRAS = ["elefante","perro","cocina","lavarropas","murcielago","camioneta","televisor","computadora", \
                   "anillo", "gato", "raton", "automovil", "departamento", "gaviota", "tobogan", "radio", \
                   "estetoscopio", "estratosfera","zorro", "electricidad", "maquillaje", "casa", "guitarra", \
                    "plato", "comida", "manzana" , "banana" , "cama" , "lapicera" , "escoba" , "agua"]
