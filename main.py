'''
JUEGO DE AHORCADO (Version Pygame)

Autor: Matias Herrera
Fecha: 28-10-2024
Version: 1.0

Desarrollado en Pygame

Caracteristicas del juego:
    * Presentacion de escena inicial en metodo "intro()", la cual cuenta con el titulo y un boton de 
      acceso a la escena principal
    * Escena principal en el metodo "principal()" donde se presenta la horca, diseñada con elementos del modulo 
      pygame.draw, la progresion del ahorcado, (tambien realizado con el modulo pygame.draw), la palabra a 
      adivinarse, y las letras erroneamente seleccionadas y la cantidad de intentos remanentes
    * Escena de victoria en el metodo "estado_ganar()" donde se realiza una animacion rudimentaria usando 
      metodos de retardo
    * Escena de derrota en el metodo "estado_perder()" donde se realizan etapas de dibujado con metodos
      de retardo      
    * Opciones de reinicio y salida en las escenas de victoria y derrota


Potenciales mejoras para futuras versiones:
    * Implementar una base de datos de palabras a adivinarse
    * Implementar una base de datos de imagenes para la escena de victoria
    * Implementar una base de datos de imagenes para la escena de derrota
    * Implementar una base de datos de imagenes para la escena de introduccion
    * Implementar una base de datos de imagenes para la escena principal
    * Dividir las palabras por temas y mostrar el tema de la palabra actual en pantalla
    * Implementar un sistema de puntaje
    * Implementar un sistema de guardado de puntajes
'''

import pygame as pg, random as rd, sys, os
from PIL import Image, ImageFilter
from constantes import *

class EstadoJuego():
    def __init__(self):
        self.estado = "intro"
        self.errores = 0
        self.palabra_a_adivinarse = rd.choice(LISTA_PALABRAS)
        self.lista_palabra_a_mostrar = []
        self.lista_letras_erroneas = []
        self.juego_parado = False   #Variable para controlar que se pare la actualizacion de pantalla
        self.letra = ""
        for _ in range(0, len(self.palabra_a_adivinarse)):
            self.lista_palabra_a_mostrar.append("_")

    def gestor_estado(self):
        ''' Metodo para gestionar los escenarios del juego de Ahorcado'''
        if (self.estado == "intro"):
            self.intro()
        elif (self.estado == "principal"):
            self.principal()
        elif (self.estado == "ganar"):
            self.estado_ganar()
        elif (self.estado == "perder"):
            self.estado_perder()

    def aplicar_difuminado(self, superficie):
        """Convierte una surface de Pygame a una imagen PIL, aplica el blur, y devuelve una nueva surface."""
        # Convertir Surface de Pygame a array de Numpy
        raw_str = pg.image.tostring(superficie, "RGB")
        image_pil = Image.frombytes("RGB", (ANCHO_PANTALLA, ALTO_PANTALLA), raw_str)
        # Aplicar filtro Gaussian Blur usando PIL
        image_pil = image_pil.filter(ImageFilter.GaussianBlur(radius=5))
        # Convertir la imagen de vuelta a una Surface de Pygame
        blurred_str = image_pil.tobytes()
        blurred_surface = pg.image.fromstring(blurred_str, (ANCHO_PANTALLA, ALTO_PANTALLA), "RGB")
        return blurred_surface
    
    def opciones_final(self, superficie, color_relleno):
        '''Metodo para mostrar botones de opciones en escena final'''
        fuente_tit_opciones = pg.font.SysFont("A Day In September", TAMAÑO_TITULO_OPCIONES)
        fuente_opciones = pg.font.SysFont("A Day In September", TAMANO_TEXTO_OPCIONES)
        surface_tit_opciones = fuente_tit_opciones.render(TITULO_PRINCIPAL_OPCIONES, True, COLOR_OPCIONES, None)
        surface_boton_volver_emp = fuente_opciones.render(OPCION_VOLVER_EMPEZAR, True, COLOR_OPCIONES, None)
        surface_boton_salir = fuente_opciones.render(OPCION_SALIR, True, COLOR_OPCIONES, None)
        ancho_surface_tit_opc = surface_tit_opciones.get_width()
        ancho_surface_opc_volver = surface_boton_volver_emp.get_width()
        ancho_surface_salir = surface_boton_salir.get_width()
        superficie.fill(color_relleno)
        superficie.blit(surface_tit_opciones, (ANCHO_PANTALLA/2 - ancho_surface_tit_opc/2, POS_TIT_OPC_Y))
        superficie.blit(surface_boton_volver_emp, (POS_X_BOTON_VOLVER_MITAD -ancho_surface_opc_volver/2, POS_OP_OPC_Y))
        superficie.blit(surface_boton_salir, (POS_X_BOTON_SALIR_MITAD -ancho_surface_salir/2, POS_OP_OPC_Y))
        boton_volver = pg.draw.rect(superficie, COLOR_OPCIONES, DIMENSIONES_BOTON_VOLVER_EMPEZAR, width= ANCHO_LINEA_PR)
        boton_salir = pg.draw.rect(superficie, COLOR_OPCIONES, DIMENSIONES_BOTON_SALIR, width= ANCHO_LINEA_PR)
        pg.display.update()

        for evento in pg.event.get():
            if evento.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = evento.pos
                if boton_volver.collidepoint(mouse_pos):
                    self.estado = "principal"
                    self.errores = 0
                    self.palabra_a_adivinarse = rd.choice(LISTA_PALABRAS)
                    self.lista_palabra_a_mostrar = []
                    self.lista_letras_erroneas = []
                    self.letra = ""
                    self.juego_parado = False
                    for _ in range(0, len(self.palabra_a_adivinarse)):
                        self.lista_palabra_a_mostrar.append("_")
                elif boton_salir.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()
    
    def dibujar_horca(self, superficie, segmento):
        if (segmento == 0):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_BASE_HORCA, FINAL_BASE_HORCA, width= ANCHO_LINEA_PR)
        elif (segmento == 1):
            pg.draw.rect(superficie, COLOR_PRINCIPAL, rect=DIMENSIONES_RECTANGULO_HORCA, width= ANCHO_LINEA_PR)
        elif (segmento == 2):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_LINEA1_HORCA, FINAL_LINEA1_HORCA, width= ANCHO_LINEA_PR)
        elif (segmento == 3):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_LINEA2_HORCA, FINAL_LINEA2_HORCA, width= ANCHO_LINEA_PR)
        elif (segmento == 4):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_LINEA3_HORCA, FINAL_LINEA3_HORCA, width= ANCHO_LINEA_PR)
    
    def dibujar_colgado(self, superficie, etapa):
        if (etapa == 0):
            pg.draw.circle(superficie, COLOR_PRINCIPAL, CENTRO_ETAPA_0, RADIO_ETAPA_0, width = ANCHO_LINEA_PR)
        elif (etapa == 1):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_ETAPA_1, FINAL_ETAPA_1, width = ANCHO_LINEA_PR)
        elif (etapa == 2):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_ETAPA_2, FINAL_ETAPA_2, width = ANCHO_LINEA_PR)
        elif (etapa == 3):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_ETAPA_2, FINAL_ETAPA_3, width = ANCHO_LINEA_PR)
        elif (etapa == 4):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_ETAPA_2, FINAL_ETAPA_4, width = ANCHO_LINEA_PR)
        elif (etapa == 5):
            pg.draw.line(superficie, COLOR_PRINCIPAL, FINAL_ETAPA_2, FINAL_ETAPA_5, width = ANCHO_LINEA_PR)
        elif (etapa == 6):
            pg.draw.line(superficie, COLOR_PRINCIPAL, FINAL_ETAPA_2, FINAL_ETAPA_6, width= ANCHO_LINEA_PR)
        elif (etapa == 7):
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_ETAPA_2, FINAL_ETAPA_3_GANAR, width= ANCHO_LINEA_PR)
            pg.draw.line(superficie, COLOR_PRINCIPAL, COMIENZO_ETAPA_2, FINAL_ETAPA_4_GANAR, width= ANCHO_LINEA_PR)
    
    def intro(self):
        '''Escena de introduccion al juego de Ahorcado'''
        raiz.fill(COLOR_FONDO_INTRO)
        fuente_titulo = pg.font.Font(os.path.join(BASE_DIR,"elementos", "fuentes", "MODERNA_.TTF"), TAMAÑO_FUENTE_TITULO)
        fuente_boton = pg.font.Font(os.path.join(BASE_DIR,"elementos", "fuentes", "MODERNA_.TTF"), TAMAÑO_FUENTE_BOTON)
        surface_texto_titulo = fuente_titulo.render(TEXTO_PRINCIPAL, True, COLOR_ELEMENTO_INTRO, None)
        surface_texto_boton = fuente_boton.render(TEXTO_SECUNDARIO_1, True, COLOR_ELEMENTO_INTRO, None)
        surface_texto_boton_alt = fuente_boton.render(TEXTO_SECUNDARIO_1, True, COLOR_FONDO_INTRO, None)
        ancho_texto_titulo = surface_texto_titulo.get_width()
        ancho_texto_boton = surface_texto_boton.get_width()
        alto_texto_boton = surface_texto_boton.get_height()
        raiz.blit(surface_texto_titulo, (ANCHO_PANTALLA/2 - ancho_texto_titulo/2, POS_TITULO_Y))
        if ((pg.time.get_ticks() // TIEMPO_ALTERNANCIA_BOTON) % 2 == 0):
            rectangulo_texto = pg.draw.rect(raiz, COLOR_ELEMENTO_INTRO, rect=(ANCHO_PANTALLA/2 - ancho_texto_boton/2, \
            POS_BOTON_Y, ancho_texto_boton, alto_texto_boton), width = ANCHO_BORDE_RECT) 
            raiz.blit(surface_texto_boton, (ANCHO_PANTALLA/2 - ancho_texto_boton/2, POS_BOTON_Y))
        else:
            rectangulo_texto = pg.draw.rect(raiz, COLOR_ELEMENTO_INTRO, rect=(ANCHO_PANTALLA/2 - ancho_texto_boton/2, \
            POS_BOTON_Y, ancho_texto_boton, alto_texto_boton)) 
            raiz.blit(surface_texto_boton_alt, (ANCHO_PANTALLA/2 - ancho_texto_boton/2, POS_BOTON_Y))

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if rectangulo_texto.collidepoint(mouse_pos):
                    self.estado = "principal"

    def principal(self):
        '''Escenario principal del juego'''
        if not self.juego_parado:
            evento = pg.event.wait()
            if evento.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if evento.type == pg.KEYUP:
                if pg.key.name(evento.key).isalpha():
                    self.letra = pg.key.name(evento.key)
                    if (self.letra not in self.palabra_a_adivinarse):
                        if (self.letra.upper() not in self.lista_letras_erroneas): 
                            self.errores += 1
                            self.lista_letras_erroneas.append(self.letra.upper())

            raiz.fill(COLOR_FONDO_PRINCIPAL)
            for num in range(0, CANTIDAD_SEGMENTOS_HORCA):
                self.dibujar_horca(raiz, num)

            for index, let in enumerate(self.palabra_a_adivinarse):
                if (let == self.letra):
                    self.lista_palabra_a_mostrar[index] = self.letra.upper()

            letras_erroneas = "-".join(self.lista_letras_erroneas)
            fuente_erroneas = pg.font.SysFont("Arial", TAMAÑO_FUENTE_ERRONEAS)
            surface_letras_erroneas = fuente_erroneas.render(letras_erroneas, True, COLOR_FUENTE_ERRONEAS, None)
            raiz.blit(surface_letras_erroneas, (500,300))

            palabra_a_mostrar = " ".join(self.lista_palabra_a_mostrar)
            fuente_palabra = pg.font.SysFont("Arial", TAMAÑO_FUENTE_ADIVINADAS)
            surface_palabra_mostrada = fuente_palabra.render(palabra_a_mostrar, True, COLOR_PRINCIPAL, None)
            raiz.blit(surface_palabra_mostrada, (500, 100))

            intentos = 7 - self.errores
            texto_intentos = f"QUEDAN {intentos} INTENTOS" if intentos > 1 else f"QUEDAN {intentos} INTENTO"
            fuente_intentos = pg.font.SysFont("Arial", TAMAÑO_FUENTE_INTENTOS)
            surface_intentos = fuente_intentos.render(texto_intentos, True, COLOR_PRINCIPAL, None)
            raiz.blit(surface_intentos, (200,500))

            if(self.errores >= 1):
                self.dibujar_colgado(raiz, 0)
            if(self.errores >= 2):
                self.dibujar_colgado(raiz, 1)
            if(self.errores >= 3):
                self.dibujar_colgado(raiz, 2)
            if(self.errores >= 4):
                self.dibujar_colgado(raiz, 3)
            if(self.errores >= 5):
                self.dibujar_colgado(raiz, 4)
            if(self.errores >= 6):
                self.dibujar_colgado(raiz, 5)
            if(self.errores >= 7):
                self.dibujar_colgado(raiz, 6)
                
            pg.display.update()

            if('_' not in self.lista_palabra_a_mostrar):
                self.estado = "ganar"
                    
            if(self.errores >= 7):
                self.estado = "perder"

        else:
             for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
    
    def estado_ganar(self):

        if not self.juego_parado:
            raiz.fill(COLOR_GANAR)
            for num in range(0, CANTIDAD_SEGMENTOS_HORCA):
                self.dibujar_horca(raiz, num)                
            for num in range(0, CANTIDAD_ETAPAS_COLGADO):
                self.dibujar_colgado(raiz, num)
            pg.display.update()
            pg.event.pump()
            pg.time.wait(1000)

            for num in range(0, CANTIDAD_SEGMENTOS_HORCA):
                raiz.fill(COLOR_GANAR)
                for ind in range(num, CANTIDAD_SEGMENTOS_HORCA):
                    self.dibujar_horca(raiz, ind)
                for et in range(0, CANTIDAD_ETAPAS_COLGADO):
                    self.dibujar_colgado(raiz, et)
                pg.display.update()
                pg.time.wait(500)
            
            raiz.fill(COLOR_GANAR)
            for et in range(0, CANTIDAD_ETAPAS_COLGADO):
                self.dibujar_colgado(raiz, et)
            pg.display.update()
            pg.event.pump()
            pg.time.wait(1000)

            raiz.fill(COLOR_GANAR)
            for et in range(0, CANTIDAD_ETAPAS_COLGADO):
                if (et != 3 and et != 4): 
                    self.dibujar_colgado(raiz, et)
            self.dibujar_colgado(raiz, 7)
            pg.display.update()
            pg.time.wait(1000)

            raiz.fill(COLOR_GANAR)
            pg.draw.circle(raiz, COLOR_PRINCIPAL, SEG_CENTRO_ETAPA_0, SEG_RADIO_ETAPA_0, width = ANCHO_LINEA_PR)
            pg.draw.line(raiz, COLOR_PRINCIPAL, SEG_COMIENZO_ETAPA_1, SEG_FINAL_ETAPA_1, width = ANCHO_LINEA_PR)
            pg.draw.line(raiz, COLOR_PRINCIPAL, SEG_COMIENZO_ETAPA_2, SEG_FINAL_ETAPA_2, width = ANCHO_LINEA_PR)
            pg.draw.line(raiz, COLOR_PRINCIPAL, SEG_COMIENZO_ETAPA_2, SEG_FINAL_ETAPA_3, width = ANCHO_LINEA_PR)
            pg.draw.line(raiz, COLOR_PRINCIPAL, SEG_COMIENZO_ETAPA_2, SEG_FINAL_ETAPA_4, width = ANCHO_LINEA_PR)
            pg.draw.line(raiz, COLOR_PRINCIPAL, SEG_FINAL_ETAPA_2, SEG_FINAL_ETAPA_5, width = ANCHO_LINEA_PR)
            pg.draw.line(raiz, COLOR_PRINCIPAL, SEG_FINAL_ETAPA_2, SEG_FINAL_ETAPA_6, width= ANCHO_LINEA_PR)
            pg.display.update()
            pg.time.wait(1000)

            superficie_difuminada = self.aplicar_difuminado(raiz)    
            raiz.blit(superficie_difuminada, (0, 0))  
            pg.display.update()

            pg.time.wait(2000)

            fuente6 = pg.font.Font(os.path.join(BASE_DIR,"elementos", "fuentes", "MODERNA_.TTF"), TAMAÑO_TEXTO_GANAR)
            surface_texto_ganar = fuente6.render(TEXTO_GANAR, True, COLOR_TEXTO_GANAR, None)
            ancho_texto_ganar = surface_texto_ganar.get_width()
            alto_texto_ganar = surface_texto_ganar.get_height()
            raiz.blit(surface_texto_ganar, (ANCHO_PANTALLA/2 - ancho_texto_ganar/2, ALTO_PANTALLA/2 -alto_texto_ganar/2))
            pg.display.update()
            pg.time.wait(2000)

            self.juego_parado = True
        else:
            self.opciones_final(raiz, COLOR_GANAR)

    def estado_perder(self):

        if not self.juego_parado:
                raiz.fill(COLOR_PERDER)
                for num in range(0, CANTIDAD_SEGMENTOS_HORCA):
                    self.dibujar_horca(raiz, num)
                
                for num in range(0, CANTIDAD_ETAPAS_COLGADO):
                    self.dibujar_colgado(raiz, num)

                pg.display.update()

                pg.time.wait(1000)

                superficie_difuminada = self.aplicar_difuminado(raiz)    
                raiz.blit(superficie_difuminada, (0, 0))  
                pg.display.update()
                
                pg.time.wait(2000)

                fuente5 = pg.font.Font(os.path.join(BASE_DIR,"elementos", "fuentes", "MODERNA_.TTF"), TAMAÑO_TEXTO_PERDER)
                surface_texto_perder = fuente5.render(TEXTO_PERDER, True, COLOR_TEXTO_PERDER, None)
                ancho_texto_perder = surface_texto_perder.get_width()
                alto_texto_perder = surface_texto_perder.get_height()
                raiz.blit(surface_texto_perder, (ANCHO_PANTALLA/2 - ancho_texto_perder/2, ALTO_PANTALLA/2 -alto_texto_perder/2))
                pg.display.update()
                pg.time.wait(2000)

                self.juego_parado = True
        else:
            self.opciones_final(raiz, COLOR_PERDER)

pg.init()

raiz = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pg.display.set_caption(TITULO)
juego = EstadoJuego()

while True:
    try:
        juego.gestor_estado()
    except Exception as e:
    # Si hay algún error, imprime el mensaje del error
        print(f"Ocurrió un error: {e}")