import pygame
import time
import random

class ModoClasico:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.puntuacion_jugador1 = 0
        self.puntuacion_jugador2 = 0
        self.ancho_ventana = 800
        self.alto_ventana = 600
        self.color_fondo = (0, 0, 0)
        self.color_bola = (255, 255, 255)
        self.color_paleta_jugador1 = (0, 0, 255)  # Azul
        self.color_paleta_jugador2 = (255, 0, 0)  # Rojo
        self.velocidad_bola = [5, 5]
        self.corriendo = True
        self.tiempo_inicio = time.time()
        self.duracion_partida = 10 * 60  # 10 minutos en segundos
        self.puntuacion_maxima = 5

        # Crear la bola y las paletas
        self.bola = pygame.Rect(self.ancho_ventana // 2 - 10, self.alto_ventana // 2 - 10, 20, 20)
        self.paleta_jugador1 = pygame.Rect(30, self.alto_ventana // 2 - 60, 10, 100)
        self.paleta_jugador2 = pygame.Rect(self.ancho_ventana - 40, self.alto_ventana // 2 - 60, 10, 100)

    def reiniciar_bola(self, direccion=None):
        """Reinicia la posición de la bola y establece su dirección."""
        self.bola.x = self.ancho_ventana // 2 - 10
        self.bola.y = self.alto_ventana // 2 - 10

        # Si no se especifica una dirección, se elige aleatoriamente
        if direccion is None:
            direccion_x = random.choice([-1, 1])  # Izquierda o derecha
        else:
            direccion_x = direccion  # Dirección hacia el jugador que recibió el gol

        direccion_y = random.choice([-1, 1])  # Arriba o abajo
        self.velocidad_bola = [5 * direccion_x, 5 * direccion_y]

    def mover_bola(self):
        self.bola.x += self.velocidad_bola[0]
        self.bola.y += self.velocidad_bola[1]

        # Rebote en los bordes superior e inferior
        if self.bola.top <= 0 or self.bola.bottom >= self.alto_ventana:
            self.velocidad_bola[1] = -self.velocidad_bola[1]

        # Rebote en las paletas
        if self.bola.colliderect(self.paleta_jugador1) or self.bola.colliderect(self.paleta_jugador2):
            self.velocidad_bola[0] = -self.velocidad_bola[0]

        # Punto para el jugador 2
        if self.bola.left <= 0:
            self.puntuacion_jugador2 += 1
            self.reiniciar_bola(direccion=1)  # Bola hacia el jugador 2

        # Punto para el jugador 1
        if self.bola.right >= self.ancho_ventana:
            self.puntuacion_jugador1 += 1
            self.reiniciar_bola(direccion=-1)  # Bola hacia el jugador 1

    def mover_paletas(self, teclas):
        # Movimiento del jugador 1 (W y S)
        if teclas[pygame.K_w] and self.paleta_jugador1.top > 0:
            self.paleta_jugador1.y -= 7
        if teclas[pygame.K_s] and self.paleta_jugador1.bottom < self.alto_ventana:
            self.paleta_jugador1.y += 7

        # Movimiento del jugador 2 (Flechas arriba y abajo)
        if teclas[pygame.K_UP] and self.paleta_jugador2.top > 0:
            self.paleta_jugador2.y -= 7
        if teclas[pygame.K_DOWN] and self.paleta_jugador2.bottom < self.alto_ventana:
            self.paleta_jugador2.y += 7

    def dibujar_elementos(self, pantalla):
        pantalla.fill(self.color_fondo)
        # Dibujar líneas de la cancha
        # Dibujar línea central
        pygame.draw.line(pantalla, (255, 255, 255), (self.ancho_ventana // 2, 0), (self.ancho_ventana // 2, self.alto_ventana), 2)
        
        # Dibujar círculo central
        pygame.draw.circle(pantalla, (255, 255, 255), (self.ancho_ventana // 2, self.alto_ventana // 2), 50, 2)
    
        pygame.draw.rect(pantalla, self.color_paleta_jugador1, self.paleta_jugador1)
        pygame.draw.rect(pantalla, self.color_paleta_jugador2, self.paleta_jugador2)
        pygame.draw.ellipse(pantalla, self.color_bola, self.bola)

        # Dibujar puntuaciones
        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"{self.puntuacion_jugador1} - {self.puntuacion_jugador2}", True, (255, 255, 255))
        pantalla.blit(texto_puntuacion, (self.ancho_ventana // 2 - texto_puntuacion.get_width() // 2, 20))

        # Dibujar temporizador
        tiempo_restante = max(0, self.duracion_partida - int(time.time() - self.tiempo_inicio))
        minutos = tiempo_restante // 60
        segundos = tiempo_restante % 60
        texto_tiempo = fuente.render(f"Tiempo: {minutos:02}:{segundos:02}", True, (255, 255, 255))
        pantalla.blit(texto_tiempo, (10, 10))
    
    def conteo_regresivo(self, pantalla):
        for i in range(5, 0, -1):
            pantalla.fill(self.color_fondo)
            fuente = pygame.font.Font(None, 100)
            texto = fuente.render(str(i), True, (255, 255, 255))
            pantalla.blit(texto, (self.ancho_ventana // 2 - texto.get_width() // 2, self.alto_ventana // 2 - texto.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(1000)  # Esperar 1 segundo

    def verificar_fin_partida(self):
        tiempo_transcurrido = time.time() - self.tiempo_inicio
        if self.puntuacion_jugador1 >= self.puntuacion_maxima or self.puntuacion_jugador2 >= self.puntuacion_maxima:
            return True
        if tiempo_transcurrido >= self.duracion_partida:
            return True
        return False

    def mostrar_resultado(self, pantalla):
        pantalla.fill(self.color_fondo)
        fuente = pygame.font.Font(None, 48)
        if self.puntuacion_jugador1 > self.puntuacion_jugador2:
            texto = f"Ganador: {self.jugador1}"
        elif self.puntuacion_jugador2 > self.puntuacion_jugador1:
            texto = f"Ganador: {self.jugador2}"
        else:
            texto = "Empate"
        texto_renderizado = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(texto_renderizado, (self.ancho_ventana // 2 - texto_renderizado.get_width() // 2, self.alto_ventana // 2 - 50))

        texto_opciones = fuente.render("Presiona R para reiniciar o M para volver al menú", True, (255, 255, 255))
        pantalla.blit(texto_opciones, (self.ancho_ventana // 2 - texto_opciones.get_width() // 2, self.alto_ventana // 2 + 50))
        pygame.display.flip()

    def jugar(self):
        pantalla = pygame.display.get_surface()
        reloj = pygame.time.Clock()
        self.conteo_regresivo(pantalla)

        while self.corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            teclas = pygame.key.get_pressed()
            self.mover_paletas(teclas)
            self.mover_bola()
            self.dibujar_elementos(pantalla)

            if self.verificar_fin_partida():
                self.corriendo = False

            pygame.display.flip()
            reloj.tick(60)

        # Mostrar resultado y opciones
        while True:
            self.mostrar_resultado(pantalla)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:  # Reiniciar
                        self.__init__(self.jugador1, self.jugador2)
                        self.jugar()
                    elif evento.key == pygame.K_m:  # Volver al menú
                        return