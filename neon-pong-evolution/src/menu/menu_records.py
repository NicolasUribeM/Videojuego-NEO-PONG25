import pygame
import os
from configuracion.ajustes import Ajustes
from utils.herramientas import cargar_imagen, dibujar_texto

class MenuRecords:
    def __init__(self, pantalla, puntuaciones):
        self.pantalla = pantalla
        self.puntuaciones = puntuaciones
        self.fuente = None  # Aquí se puede cargar una fuente personalizada
        self.color_texto = (255, 255, 255)  # Color blanco para el texto

    def cargar_fuente(self, ruta_fuente, tamaño):
        self.fuente = pygame.font.Font(ruta_fuente, tamaño)

    def mostrar_records(self):
        self.pantalla.fill((0, 0, 0))  # Fondo negro
        fuente_titulo = pygame.font.Font(None, 50)
        fuente_texto = pygame.font.Font(None, 36)

        # Título
        titulo = fuente_titulo.render("Records de Supervivencia", True, (255, 255, 255))
        self.pantalla.blit(titulo, (self.pantalla.get_width() // 2 - titulo.get_width() // 2, 50))

        # Tabla de records
        for i, puntuacion in enumerate(sorted(self.puntuaciones, key=lambda x: x['puntos'], reverse=True)):
            texto = f"{i + 1}. {puntuacion['nombre']} - {puntuacion['puntos']} segundos"
            texto_renderizado = fuente_texto.render(texto, True, (255, 255, 255))
            self.pantalla.blit(texto_renderizado, (50, 120 + i * 40))

        pygame.display.flip()

    def agregar_puntuacion(self, nombre, puntos):
        self.puntuaciones.append({'nombre': nombre, 'puntos': puntos})

    def guardar_records(self, ruta_archivo):
        with open(ruta_archivo, 'w') as archivo:
            for puntuacion in self.puntuaciones:
                archivo.write(f"{puntuacion['nombre']},{puntuacion['puntos']}\n")

    def guardar_record_supervivencia(self, nombre, tiempo):
        """Guarda el tiempo sobrevivido en el archivo de records del modo supervivencia."""
        with open("records_supervivencia.txt", "a") as archivo:
            archivo.write(f"{nombre},{tiempo}\n")

    def cargar_records(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r') as archivo:
                self.puntuaciones = []
                for linea in archivo:
                    nombre, puntos = linea.strip().split(',')
                    self.puntuaciones.append({'nombre': nombre, 'puntos': int(puntos)})
        except FileNotFoundError:
            self.puntuaciones = []  # Si no existe el archivo, inicializa la lista vacía