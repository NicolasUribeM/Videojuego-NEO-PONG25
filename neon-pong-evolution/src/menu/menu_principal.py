# Contenido del archivo /neon-pong-evolution/neon-pong-evolution/src/menu/menu_principal.py

import pygame
import random
from configuracion.ajustes import Ajustes
from utils.herramientas import dibujar_texto
from menu.menu_records import MenuRecords

class MenuPrincipal:
    def __init__(self, pantalla, ajustes):
        self.pantalla = pantalla
        self.ajustes = ajustes
        self.opciones = ['Modo Clásico', 'Modo Supervivencia', 'Records', 'Salir']
        self.seleccion = 0
        self.modo_seleccionado = None
        self.particulas = []  # Lista para almacenar partículas
        self.tiempo_cambio_color = 0  # Controlar la velocidad del cambio de color del recuadro RGB
        self.color_recuadro = (255, 0, 0)  # Color inicial del recuadro

    def generar_particulas(self):
        """Genera partículas RGB para el fondo."""
        for _ in range(1):  # Generar menos partículas por frame
            x = random.randint(0, self.ajustes.ancho_ventana)
            y = self.ajustes.alto_ventana  # Comienzan desde la parte inferior
            color = tuple(random.randint(0, 255) for _ in range(3))  # Generar color RGB como tupla
            velocidad = random.uniform(0.5, 1.0)  # Velocidad más lenta
            tamano = random.randint(2, 5)  # Tamaño aleatorio entre 2 y 5 píxeles
            self.particulas.append({'x': x, 'y': y, 'color': color, 'velocidad': velocidad, 'tamano': tamano})

    def actualizar_particulas(self):
        """Actualiza la posición de las partículas."""
        for particula in self.particulas:
            particula['y'] -= particula['velocidad']  # Mover hacia arriba lentamente
        self.particulas = [p for p in self.particulas if p['y'] > 0]  # Eliminar partículas fuera de pantalla

    def dibujar_particulas(self):
        """Dibuja partículas en el fondo del menú principal."""
        for particula in self.particulas:
            pygame.draw.circle(self.pantalla, particula['color'], (int(particula['x']), int(particula['y'])), particula['tamano'])

    def mostrar_menu(self):
        while self.modo_seleccionado is None:
            self.pantalla.fill(self.ajustes.color_fondo)  # Fondo negro

            # Dibujar partículas
            self.generar_particulas()
            self.actualizar_particulas()
            self.dibujar_particulas()

            # Dibujar título
            self.dibujar_titulo()

            # Dibujar opciones
            self.dibujar_opciones()

            pygame.display.flip()
            self.gestionar_eventos()

        return self.modo_seleccionado

    def dibujar_titulo(self):
        """Dibuja el título del juego."""
        fuente_titulo = pygame.font.Font(None, 100)  # Fuente grande
        texto_titulo = fuente_titulo.render("NEO-PONG25", True, (255, 255, 255))  # Letras llamativas
        self.pantalla.blit(texto_titulo, (self.ajustes.ancho_ventana // 2 - texto_titulo.get_width() // 2, 50))

    def dibujar_opciones(self):
        """Dibuja las opciones del menú con un recuadro RGB."""
        fuente_opciones = pygame.font.Font(None, 50)
        for i, opcion in enumerate(self.opciones):
            color = (255, 255, 255)  # Color blanco para las opciones
            texto_opcion = fuente_opciones.render(opcion, True, color)
            x = self.ajustes.ancho_ventana // 2 - texto_opcion.get_width() // 2
            y = 200 + i * 60

            # Dibujar recuadro RGB alrededor de la opción seleccionada
            if i == self.seleccion:
                self.tiempo_cambio_color += 1
                if self.tiempo_cambio_color % 10 == 0:  # Cambiar color cada 10 frames
                    self.color_recuadro = tuple(random.randint(0, 255) for _ in range(3))
                pygame.draw.rect(self.pantalla, self.color_recuadro, (x - 10, y - 10, texto_opcion.get_width() + 20, texto_opcion.get_height() + 20), 3)

            self.pantalla.blit(texto_opcion, (x, y))

    def gestionar_eventos(self):
        """Gestiona los eventos del menú."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.seleccion = (self.seleccion - 1) % len(self.opciones)
                elif evento.key == pygame.K_DOWN:
                    self.seleccion = (self.seleccion + 1) % len(self.opciones)
                elif evento.key == pygame.K_RETURN:
                    if self.seleccion == 0:
                        self.modo_seleccionado = 'clasico'
                    elif self.seleccion == 1:
                        self.modo_seleccionado = 'supervivencia'
                    elif self.seleccion == 2:
                        self.modo_seleccionado = 'records'
                    elif self.seleccion == 3:
                        pygame.quit()
                        exit()